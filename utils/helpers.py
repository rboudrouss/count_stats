from datetime import datetime
from discord import User, Message
from .types import UserData, MessageData


# def date_from_msg(msg: MessageData) -> datetime:
#     return datetime(*msg["date"])


def str_from_date(date: datetime, is_hour: bool = True,
                  is_minute: bool = True) -> str:
    return f"{date.day}-{date.month}"+(f"-{date.hour}"if is_hour else "") \
        + (f"-{date.minute}" if is_minute else "")


def data_from_message(message: Message) -> MessageData:
    return {
        "message_id": str(message.id),
        "author_id": str(message.author.id),
        "content": message.content,
        "date": message.created_at.isoformat(),
    }


def data_from_user(user: User) -> UserData:
    return {
        "avatar_url":   str(user.avatar_url),
        "name":         user.display_name,
        "discriminator": user.discriminator,
        "user_id":           str(user.id),
    }
