release: python manage.py migrate
worker: python ./discord_bot/bot.py stayOn Listen
web: gunicorn backend.wsgi --log-file -
