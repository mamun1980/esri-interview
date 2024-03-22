from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


REGION = (
    ('Peninsular East', 'Peninsular East'),
    ('Sabah', 'Sabah'),
    ('Sarawak', 'Sarawak')
)

YEAR_CHOICES = []
for r in range(1970, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class EsriInterview(models.Model):
    block = models.CharField(max_length=50)
    usi_code = models.CharField(max_length=100)
    region = models.CharField(max_length=20, choices=REGION)
    length_km = models.DecimalField(max_digits=10, decimal_places=5)
    acquisition_year = models.PositiveIntegerField(
            choices=YEAR_CHOICES, null=True, blank=True,
            validators=[MinValueValidator(1970), MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>"
        )
    processing_year = models.PositiveIntegerField(
            choices=YEAR_CHOICES, null=True, blank=True,
            validators=[MinValueValidator(1970), MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>"
        )