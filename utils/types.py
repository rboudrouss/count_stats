from typing import List, TypedDict, Dict, Union

# MaxLen : 6
DateList = List[int]

# TODO FALSE, correct this


class UserData(TypedDict):
    discriminator: str
    user_id: str
    name: str
    avatar_url: str


class MessageData(TypedDict):
    message_id: str
    author_id: str
    content: str
    date: DateList


UsersData = List[UserData]

UserId = Union[str, int]

Count = Dict[str, int]

Podium = Dict[str, str]


class AllCount(TypedDict):
    last_update: DateList
    count: Count
    podium: Podium


MsgCount = List[Union[str, int]]
