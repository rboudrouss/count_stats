from datetime import datetime
from discord import User, Message
from .types import UsersData, MessageData, List

def date_from_msg(msg:List[int])->datetime:
    if msg is list:
        return datetime(*msg)
    else:
        return datetime(*msg["date"])


def str_from_date(date:datetime, is_hour:bool=True, is_minute:bool=True)->str:
    return f"{date.day}-{date.month}"+(f"-{date.hour}"if is_hour else "") + (f"-{date.minute}" if is_minute else "")

def data_from_message(message:Message)->MessageData:
    return {
        "message_id":message.id,
        "author_id":message.author.id,
        "content":message.content,
        "date":list(message.created_at.timetuple())[:6],
    }

def data_from_user(user:User)->UsersData:
    return {
        str(user.id) : {
            "avatar_url":   str(user.avatar_url),
            "name":         user.display_name,
            "discriminator":user.discriminator,
            "id":           str(user.id),
        }
    }