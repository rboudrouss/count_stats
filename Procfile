release: python manage.py migrate; python manage.py collectstatic
web: gunicorn backend.wsgi --log-file -
worker : python discord_bot/bot.py
