from typing import List, TypedDict, Dict, Annotated

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