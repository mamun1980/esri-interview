from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)


SECRET_KEY = 'django-insecure-xzht*x1h-+(%jezrv$j*3g1dowf+y4ht&se1248%x@36f4cju!'


ALLOWED_HOSTS = [
    '52.221.250.122'
    '52.221.250.122:8000'
]


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': config('DB_NAME', ''),
        'USER': config('DB_USER_NAME', ''),
        'PASSWORD': config('DB_USER_PASSWORD', ''),
        'HOST': config('DB_HOST', ''),
        'PORT': config('DB_PORT', default=5432, cast=int)
    }
}