from typing import List, TypedDict, Dict, Union, Tuple, Optional
from datetime import datetime
# TODO FALSE, correct this

Tuple
Optional


class UserData(TypedDict, total=False):
    discriminator: str
    user_id: str
    name: str
    avatar_url: str
    ghost: bool
    nb_msg: int
    top: int


class MessageData(TypedDict):
    message_id: str
    author_id: str
    content: str
    date: str


UsersData = List[UserData]

UserId = Union[str, int]

Count = Dict[str, int]

Podium = Dict[str, str]


class AllCount(TypedDict):
    last_update: datetime  # ?
    count: Count
    podium: Podium


MsgCount = List[Union[str, int]]
