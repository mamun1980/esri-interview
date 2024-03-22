from django.urls import path
from .views import EsriDataListApiView


urlpatterns = [
    path('esri/', EsriDataListApiView.as_view())
]