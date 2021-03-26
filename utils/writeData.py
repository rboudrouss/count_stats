import json
# from .branches import USERS, HISTORY, COUNT
from .fbinit import db
from .getData import get_history, get_users_data
from .types import MessageData, List, UsersData

def write_history(data:List[MessageData])->None:
    """
    TODO
    """
    if type(data) is not list:
        data = json.loads(data)
    db.child("history").set(data)

def append_history(data:List[MessageData])->None:
    history = get_history()

    if type(data) is list: history = data + history
    else: history.insert(0, data)

    write_history(history)

def write_users(data:UsersData)->None:
    if type(data) is not dict:
        data = json.loads(data)
    db.child("users").set(data)

def append_users(data:UsersData)->None:
    users = dict(get_users_data(), **data)
    write_users(users)

def write_count(data)->None:
    if type(data) is not dict:
        data = json.loads(data)
    db.child("count").set(data)