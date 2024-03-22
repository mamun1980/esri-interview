from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ENV = config('SITE_ENV', 'dev')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d@2149_e&32k)6tq7t6eq$9!_enkq3x18oe+^gk&&4rqez#4z4"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



try:
    from .local import *
except ImportError:
    pass