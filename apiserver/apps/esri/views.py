from rest_framework import generics
import re
from decimal import Decimal
from django.db.models import Q
from rest_framework.response import Response
from .models import EsriInterview
from .serializers import EsriInterviewSerializer


class EsriDataListApiView(generics.ListAPIView):
    queryset = EsriInterview.objects.all()
    serializer_class = EsriInterviewSerializer

    def get_queryset(self) :
        # import pdb; pdb.set_trace()
        # user = self.request.user
        qs = EsriInterview.objects.all()
        qp = self.request.query_params
        query = qp.get('q')
        if not query:
            return qs
        else:
            sp_pattern = r'\s+(?=([^"]*"[^"]*")*[^"]*$)'
            if_dq_pattern = r'^[^"].*[^"]$'
            dq_pattern = r'"([^"]*)"'
            split_list = re.split(sp_pattern, query)
            for qstr in split_list:
                if bool(re.match(if_dq_pattern, qstr)):
                    qs = qs.filter(
                        Q(block__icontains=qstr) |
                        Q(usi_code__icontains=qstr) |
                        Q(length_km__icontains=qstr) |
                        Q(acquisition_year__icontains=qstr) |
                        Q(processing_year__icontains=qstr) |
                        Q(region__icontains=qstr)
                    )
                else:
                    quoted_text = re.findall(dq_pattern, qstr)[0]
                    if qstr[0] in ['-', '–']:
                        qs = qs.filter(
                            ~Q(block__icontains=quoted_text) |
                            ~Q(usi_code__icontains=quoted_text) |
                            ~Q(region__icontains=quoted_text)
                        )
                    elif '..' in quoted_text:
                        ranges = quoted_text.split("..")
                        qs = qs.filter(
                            Q(length_km__range=(Decimal(ranges[0]), Decimal(ranges[1]))) |
                            Q(acquisition_year__range=(int(ranges[0]), int(ranges[1]))) |
                            Q(processing_year__range=(int(ranges[0]), int(ranges[1])))
                        )
                    elif "*" in quoted_text:
                        qtexts = quoted_text.split(" ")
                        for qtext in qtexts:
                            qs = qs.filter(
                                Q(block__iregex=f"{qtext}")
                            )

                    else:
                        qs = qs.filter(
                            Q(block__exact=quoted_text) |
                            Q(usi_code__exact=quoted_text) |
                            Q(region__exact=quoted_text)
                        )
            return qs
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        # import pdb; pdb.set_trace()
        queryset = self.get_queryset()
        # page = self.paginate_queryset(queryset, request)
        serializer = EsriInterviewSerializer(queryset, many=True)
        count = len(serializer.data)
        return Response({
            'count': count,
            'results': serializer.data
        })

