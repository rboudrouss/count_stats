from datetime import datetime

def date_from_msg(msg):
    if msg is list:
        return datetime(*msg)
    else:
        return datetime(*msg["date"])


def str_from_date(date:datetime, is_hour=True, is_minute=True):
    return f"{date.month}-{date.day}"+(f"-{date.hour}"if is_hour else "") + (f"-{date.minute}" if is_minute else "")