import json
import datetime


# message
def get_history():
    return json.loads(open("data/history.json").read())

def get_user_msgs(id=None):
    history = get_history()
    if not id: return history
    user_msgs = [msg for msg in history if msg["author_id"]==int(id)]
    return user_msgs

def get_msgs_date(mind=None,maxd=None):
    """
    max min must respect format : <Y>-<M>-<?D>-<?H>-<?S>-<?MS>
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
    if mind>maxd : mind,maxd = (maxd,mind)

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
    # if type(infos) is list and len(infos)>1: return [{info:msg.get(info, {"Error":"404, Not Found"}) for info in infos} for msg in history]
    # if type(infos) is list :
        # infos = infos[0]
    return [msg.get(infos) for msg in history]

def get_messages(mind,maxd,id,infos): return get_msg_info(mind, maxd, id, infos)

# Users
def get_users(id=None): return get_user_data(id)

def get_users_data():
    return json.loads(open("data/users.json").read())

def get_user_data(id=None):
    users = get_users()
    if not id : return users
    return users.get(str(id),{"Error":"404 User not found"})