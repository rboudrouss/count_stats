import json
from .filePaths import USERS_FILE, HISTORY_FILE, COUNT_FILE
from .getData import get_history, get_users_data

def create_file(file_path):
    if not file_path.exists():
        file_path.parent.mkdir(exist_ok=True)
        file_path.touch(exist_ok=True)

def write_history(data):
    if type(data) is list:
        data = json.dumps(data)
    create_file(HISTORY_FILE)
    HISTORY_FILE.write_text(data)

def append_history(data):
    if type(data) is str:
        data = json.loads(data)
    history = get_history() + data
    write_history(history)

def write_users(data):
    if type(data) is dict:
        data = json.dumps(data)
    create_file(USERS_FILE)
    USERS_FILE.write_text(data)

def append_users(data):
    if type(data) is str:
        data = json.loads(data)
    users = dict(get_users_data(), **{str(k):v for k,v in data.items()})
    write_users(users)

def write_count(data):
    if type(data) is dict:
        data = json.dumps(data)
    create_file(COUNT_FILE)
    COUNT_FILE.write_text(data)