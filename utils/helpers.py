from datetime import datetime

def date_from_msg(msg):
    if msg is list:
        return datetime(*msg)
    else:
        return datetime(*msg["date"])