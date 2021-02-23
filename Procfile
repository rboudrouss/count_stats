release: python manage.py migrate
disbot : python ./discord_bot/bot.py
web: gunicorn backend.wsgi --log-file -
