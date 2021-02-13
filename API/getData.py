import json
import datetime

def get_history():
    return json.loads(open("data/history.json").read())

def get_users():
    return json.loads(open("data/users.json").read())

def get_user(id):
    return json.loads(open("data/users.json").read()).get(str(id),{"Error":"404 User not found"})

def get_user_msgs(id):
    history = get_history()
    user_msgs = [msg for msg in history if msg["author_id"]==int(id)]
    return user_msgs

def get_msgs_date(mind,maxd):
    """
    max min must respect format : <Y>-<M>-<?D>-<?H>-<?S>-<?MS>
    """
    history = get_history()

    if not mind and not maxd : return history
    if not mind :
        l = list(map(int, maxd.split('-')))
        mind = datetime.datetime(*l)
        l[-1]+=1
        maxd = datetime.datetime(*l)
    if not maxd:
        l = list(map(int, mind.split('-')))
        mind = datetime.datetime(*l)
        l[-1]+=1
        maxd = datetime.datetime(*l)
        
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
            
    return history[min_index:max_index]

def get_user_date(mind,maxd,id):
    if not id: return []
    history = get_msgs_date(mind,maxd)
    return [msg for msg in history if msg["author_id"]==int(id)]