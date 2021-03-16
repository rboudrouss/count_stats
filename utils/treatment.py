from datetime import datetime

from .constants import DELAY_COUNT_UPDATE
from .getData import get_all_users, get_users_data, get_history, get_count
from .writeData import write_count


def users_not_in_data():
    usersData = get_users_data()
    users = get_all_users(fast=False)
    return list({user for user in users if str(user) not in usersData})

def create_count():
    history=get_history()
    count = {}
    for msg in history:
        if str(msg["author_id"]) in count: count[str(msg["author_id"])] +=1
        else: count[str(msg["author_id"])] = 1
    return count

def create_classement(count_dic=create_count()):
    return {f"top{i+1}":k for i,k in enumerate(sorted(count_dic, key=count_dic.get, reverse=True))}

def update_count():
    delta = datetime.now()-datetime(*get_count()["last_update"])
    if delta.seconds>DELAY_COUNT_UPDATE:
        count = create_count()
        write_count({
            "last_update"   : list(datetime.now().timetuple())[:6],
            "count"         : count,
            "podium"        : create_classement()
        })
