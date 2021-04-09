release: python manage.py migrate --run-syncdb
worker: python ./discord_bot/bot.py stayOn Listen
web: gunicorn backend.wsgi --log-file -
