import json
from .constants import USERS_FILE, HISTORY_FILE
from .getData import get_history, get_users_data

def write_history(data):
    if type(data) is list:
        data = json.dumps(data)
    if not HISTORY_FILE.exists():
        HISTORY_FILE.parent.mkdir(exist_ok=True)
        HISTORY_FILE.touch(exist_ok=True) 
    HISTORY_FILE.write_text(data)

def append_history(data):
    if type(data) is str:
        data = json.loads(data)
    history = get_history() + data
    write_history(history)

def write_users(data):
    if type(data) is dict:
        data = json.dumps(data)
    if not USERS_FILE.exists():
        USERS_FILE.parent.mkdir(exist_ok=True)
        USERS_FILE.touch(exist_ok=True)
    USERS_FILE.write_text(data)

def append_users(data):
    if type(data) is str:
        data = json.loads(data)
    users = dict(get_users_data(), **{str(k):v for k,v in data.items()})
    write_users(users)