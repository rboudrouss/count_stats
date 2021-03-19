release: python manage.py migrate
worker: python ./discord_bot/bot.py stayOn getMsg
web: gunicorn backend.wsgi --log-file -
