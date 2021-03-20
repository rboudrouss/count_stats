from datetime import datetime, timedelta

from .constants import DELAY_COUNT_UPDATE
from .getData import get_all_users, get_users_data, get_history, get_count
from .writeData import write_count
from .types import Count, List, Dict, Podium


def users_not_in_data()->List[int]:
    usersData = get_users_data()
    users = get_all_users(fast=False)
    return list({user for user in users if str(user) not in usersData})

def create_count(history=get_history())->Count:
    count = {}
    for msg in history:
        if str(msg["author_id"]) in count: count[str(msg["author_id"])] +=1
        else: count[str(msg["author_id"])] = 1
    return count

def create_classement(count_dic=create_count())->Podium:
    return {f"top{i+1}":k for i,k in enumerate(sorted(count_dic, key=count_dic.get, reverse=True))}

def update_count()->None:
    lastUpdate = get_count().get("last_update", False)
    if lastUpdate: delta = datetime.now()-datetime(*lastUpdate)
    else: delta = timedelta(seconds=DELAY_COUNT_UPDATE+1)
    if delta.seconds>DELAY_COUNT_UPDATE:
        count = create_count()
        write_count({
            "last_update"   : list(datetime.now().timetuple())[:6],
            "count"         : count,
            "podium"        : create_classement()
        })
