release: python manage.py migrate
worker: python ./discord_bot/bot.py
web: gunicorn backend.wsgi --log-file -
