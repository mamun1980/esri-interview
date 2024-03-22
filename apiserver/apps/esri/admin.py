from django.contrib import admin, messages
from django.urls.resolvers import URLPattern
from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.urls import path, reverse
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from pathlib import Path
import pandas as pd

from .models import EsriInterview


@admin.register(EsriInterview)
class EsriInterviewAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ['block', 'usi_code', 'region', 'length_km', 'acquisition_year', 'processing_year']
    list_filter = ['region']
    search_fields = ['block']

    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        custom_urls = [
            path('load-data/', self.admin_site.admin_view(self.load_esri_data), name='load_data'),
        ]
        return custom_urls + urls

    @button(html_attrs={'style': 'background-color:#1995dc;color:black'})
    def upload_esri_data(self, request):
        context = dict(
            self.admin_site.each_context(request)
        )
        return TemplateResponse(request, 'admin/load_esri_data.html', context)
    
    def load_esri_data(self, request):
        if request.method == 'POST':
            data_file_name = request.FILES['esri_data_file']
            obj_list = []
            if data_file_name:
                try:
                    df = pd.read_excel(data_file_name)
                    for index, row in df.iterrows():
                        block = row['BLOCK']
                        usi_code = row['USI_CODE']
                        region = row['REGION']
                        length_km = row['LENGTH_KM']
                        acquisition_year = row['ACQUISITION_YEAR']
                        processing_year = row['PROCESSING_YEAR']

                        obj = EsriInterview(
                            block=block,
                            usi_code=usi_code,
                            region=region,
                            length_km=length_km,
                            acquisition_year=acquisition_year,
                            processing_year=processing_year
                        )
                        obj_list.append(obj)
                        
                    esri_datas = EsriInterview.objects.bulk_create(obj_list)
                except Exception as e:
                    print(e)
            return HttpResponseRedirect('/admin/esri/esriinterview/')
        