from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)


SECRET_KEY = 'django-insecure-xzht*x1h-+(%jezrv$j*3g1dowf+y4ht&se1248%x@36f4cju!'


ALLOWED_HOSTS = []


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