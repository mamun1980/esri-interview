import json
from django.utils import timezone
from django.core.management.base import BaseCommand
from pathlib import Path
import pandas as pd
from apps.esri.models import EsriInterview


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


class Command(BaseCommand):
    help = "Load Data"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, default=None)

    def handle(self, *args, **options):
        start_time = timezone.datetime.now().replace(microsecond=0)
        
        file_path = options.get('path')
        if not file_path:
            file_path = BASE_DIR / 'data'

        data_file_name = file_path / 'seismicDataForExam.xlsx'
        obj_list = []

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

        end_time = timezone.datetime.now().replace(microsecond=0)

        execution_time = (end_time - start_time)
        self.stdout.write(f"Start Time: {str(start_time)}")
        self.stdout.write(f"End Time: {str(end_time)}")
        self.stdout.write(f"Execution Time: {str(execution_time)}")