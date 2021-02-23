release: python manage.py migrate; python manage.py collectstatic
worker : python ./discord_bot/bot.py
web: gunicorn backend.wsgi --log-file -
