
#!/bin/bash

python manage.py migrate --no-input
python manage.py collectstatic --noinput


gunicorn core.wsgi --user www-data --timeout 60 --bind 0.0.0.0:8010 --log-level=error &
nginx -g "daemon off;"