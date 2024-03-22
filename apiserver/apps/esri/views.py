from rest_framework import generics
from .models import EsriInterview
from .serializers import EsriInterviewSerializer


class EsriDataListApiView(generics.ListAPIView):
    queryset = EsriInterview.objects.all()
    serializer_class = EsriInterviewSerializer
