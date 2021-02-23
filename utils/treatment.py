from datetime import datetime

from .getData import get_all_users, get_users_data, get_history
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
        else: count[str(msg["author_id"])] = 0
    return count

# TODO create a get_count function and replace create_count
def create_classement(count_dic=create_count(),top=3):
    cands = [[0,0]]*top
    for user,nb in count_dic.items():
        for i in range(len(cands)):
            if nb > cands[i][1]:
                cands[i] = [user,nb]
    return {
        f"top{j+1}":cands[j][0] for j in range(len(cands))
    }

def update_count():
    # TODO update at 5 min interval
    count = create_count()
    write_count({
        "last_update"   : list(datetime.now().timetuple())[:6],
        "count"         : count,
        "podium"        : create_classement()
    })
