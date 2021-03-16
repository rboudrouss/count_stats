from typing import List, TypedDict, Dict, Annotated, Union, Optional

# MaxLen : 6
DateList = List[int]

class UserData(TypedDict):
    avatar_url: str
    author_id : int
    content   : str
    date      : DateList

class MessageData(TypedDict):
    message_id: int
    author_id : int
    content   : str
    date      : DateList

UsersData = Dict[int, UserData]

UserId = Union[str,int]

Count = Dict[str,int]

Podium = Dict[str,str]

class AllCount(TypedDict):
    last_update:DateList
    count:Count
    podium: Podium

MsgCount = List[Union[str,int]]