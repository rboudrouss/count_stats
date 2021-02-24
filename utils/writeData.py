import json
# from .branches import USERS, HISTORY, COUNT
from .fbinit import db
from .getData import get_history, get_users_data

def write_history(data):
    if type(data) is not list:
        data = json.loads(data)
    db.child("history").set(data)

def append_history(data):
    history = get_history() + data
    write_history(history)

def write_users(data):
    if type(data) is not dict:
        data = json.loads(data)
    db.child("users").set(data)

def append_users(data):
    users = dict(get_users_data(), **{str(k):v for k,v in data.items()})
    write_users(users)

def write_count(data):
    if type(data) is not dict:
        data = json.loads(data)
    db.child("count").set(data)