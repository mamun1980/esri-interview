from decouple import config

ENV = config('SITE_ENV', 'dev')

if ENV == 'production':
    print(f"{'*' * 10} loading {ENV} evironment settings {'*' * 10}")
    from .production import *

elif ENV == 'dev':
    print(f"{'*' * 10} loading {ENV} evironment settings {'*' * 10}")
    from .dev import *