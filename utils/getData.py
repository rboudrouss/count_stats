import json
import datetime
from .filePaths import HISTORY_FILE, USERS_FILE, COUNT_FILE


# message
def get_history():
    if HISTORY_FILE.exists() : return json.loads(HISTORY_FILE.read_text())
    return []

def get_user_msgs(id=None):
    history = get_history()
    if not id: return history
    user_msgs = [msg for msg in history if msg["author_id"]==int(id)]
    return user_msgs

def get_msgs_date(mind=None,maxd=None):
    """
    max min must respect format : <Y>-<M>-<D>-<?H>-<?S>-<?MS>
    """
    history = get_history()

    if not mind and not maxd : return history
    elif not mind :
        l = list(map(int, maxd.split('-')))
        mind = datetime.datetime(*l)
        l[-1]+=1
        maxd = datetime.datetime(*l)
    elif not maxd:
        l = list(map(int, mind.split('-')))
        mind = datetime.datetime(*l)
        l[-1]+=1
        maxd = datetime.datetime(*l)
    else:
        mind = datetime.datetime(*map(int, mind.split('-')))
        maxd = datetime.datetime(*map(int, maxd.split('-')))
    if mind>maxd : mind,maxd = (maxd,mind) # HACK

    max_index = 0; max_ = False
    min_index = 0; min_ = False

    for index,message in enumerate(history):
        msg_date = datetime.datetime(*message["date"])
        if msg_date<mind and not max_:
            max_index=index
            max_ = True
        if msg_date<maxd and not min_:
            min_index=index
            min_=True
        if min_ and max_ :
            break
    if min_ and not max_: max_index = index+1 #HACK kinda

    return history[min_index:max_index]

def get_user_date(mind=None,maxd=None,id=None):
    history = get_msgs_date(mind,maxd)
    if not id: return history
    return [msg for msg in history if msg["author_id"]==int(id)]

def get_msg_info(mind=None,maxd=None,id=None,infos=None):
    history = get_user_date(mind, maxd, id)
    if not infos: return history
    return [msg.get(infos) for msg in history]

def get_messages(mind,maxd,id,infos): return get_msg_info(mind, maxd, id, infos)

# Users
def get_users(id=None): return get_user_data(id)

def get_users_data():
    if USERS_FILE.exists(): return json.loads(USERS_FILE.read_text())
    return {}

def get_user_data(id=None):
    users = get_users_data()
    if not id : return users
    return users.get(str(id),{"Error":"404 User not found"})

def get_all_users(fast=True):
    if fast: return [user.id for user in get_user_data()]
    return list({msg["author_id"] for msg in get_history()})

# Classement

def get_count():
    if COUNT_FILE.exists(): return json.loads(COUNT_FILE.read_text())
    return {}