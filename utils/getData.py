from datetime import datetime, timedelta
# from time import sleep

from .fbinit import db
from .helpers import date_from_msg, str_from_date
from .types import MessageData, List, DateList, Optional, Union, MsgCount
from .constants import INTER

# message
def get_history()->List[MessageData]:
    """
    TODO
    """
    history = db.child("history").get().val()
    # sleep(5)
    return list(history) if history is not None else [] 

def get_user_msgs(id:Optional[Union[str,int]]=None)->List[MessageData]:
    """
    TODO
    """
    history = get_history()
    if not id: return history
    user_msgs = [msg for msg in history if msg["author_id"]==int(id)]
    return user_msgs

def get_msgs_date(mind:Optional[str]=None, maxd:Optional[str]=None)->List[MessageData]:
    """
    max min must respect format : <Y>-<M>-<D>-<?H>-<?S>-<?MS>
    """
    history = get_history()

    if not mind and not maxd : return history
    elif not mind :
        l = list(map(int, maxd.split('-')))
        mind = datetime(*l)
        l[-1]+=1
        maxd = datetime(*l)
    elif not maxd:
        l = list(map(int, mind.split('-')))
        mind = datetime(*l)
        l[-1]+=1
        maxd = datetime(*l)
    else:
        mind = datetime(*map(int, mind.split('-')))
        maxd = datetime(*map(int, maxd.split('-')))
    if mind>maxd : mind,maxd = (maxd,mind) # HACK

    max_index = 0; max_ = False
    min_index = 0; min_ = False

    for index,message in enumerate(history):
        msg_date = datetime(*message["date"])
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

def get_user_date(mind=None,maxd=None,id=None)->List[MessageData]:
    """
    TODO
    """
    history = get_msgs_date(mind,maxd)
    if not id: return history
    return [msg for msg in history if msg["author_id"]==int(id)]

def get_msg_info(mind=None,maxd=None,id=None,infos=None)->List[Union[MessageData, str, int, DateList]]:
    """
    TODO
    """
    history = get_user_date(mind, maxd, id)
    if not infos: return history
    return [msg.get(infos) for msg in history]

def get_messages(mind,maxd,id,infos)->List[MessageData]:
    """
    TODO
    """
    return get_msg_info(mind, maxd, id, infos)

def get_nb_msg_inter(id:int=None, inter:str=None, max:Union[int, str]=None, empty:bool=False)->List[MsgCount]:
    """
    inter format DD-HH-MM
    """
    if not inter: inter=INTER
    if max and type(max) is not int: max=int(max)

    history=get_history()
    startd = date_from_msg(history[0])

    inter=list(map(int, inter.split("-")))

    is_minute = bool(inter[2])
    is_hour = bool(inter[1])

    if not is_minute:
        startd = startd.replace(minute=1)
        is_hour=False
    if not is_hour:
        startd.replace(hour=1)

    inter=timedelta(days=inter[0], hours=inter[1], minutes=inter[2])

    rep = [[str_from_date(startd,is_hour,is_minute),0]]
    #FIXME return is decalé by inter except today
    for msg in history:
        msg_date = date_from_msg(msg)
        if startd-inter>msg_date:
            while startd-inter>msg_date:
                rep.append([str_from_date(startd,is_hour,is_minute),0])
                startd-=inter
        else:
            # TODO optimize this
            if id :
                if msg["author_id"]==int(id):
                    rep[-1][1]+=1
            else:
                rep[-1][1]+=1

    #TODO not optimized
        if max and len(rep)>max:
            return [i for i in rep if i[1]!=0] if empty else rep

    return [i for i in rep if i[1]!=0] if empty else rep

# Users
def get_users(id=None): return get_user_data(id)

def get_users_data():
    users = db.child("users").get().val()
    return dict(users) if users is not None else []

def get_user_data(id=None):
    users = get_users_data()
    if not id : return users
    return users.get(str(id),{"Error":"404 User not found"})

def get_all_users(fast=True):
    if fast: return [user_id for user_id in get_users_data()]
    return list({msg["author_id"] for msg in get_history()})

# Classement

def get_count():
    count = db.child("count").get().val()
    return dict(count) if count is not None else {}