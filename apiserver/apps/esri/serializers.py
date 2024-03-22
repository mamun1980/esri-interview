from rest_framework import serializers
from .models import EsriInterview



class EsriInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsriInterview
        fields = ['id', 'block', 'usi_code', 'region', 'length_km', 'acquisition_year', 'processing_year']


