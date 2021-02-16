from .getData import get_msg_info, get_users_data

def users_not_in_data():
    usersData = get_users_data()
    users = get_msg_info(infos="author_id")
    return list({user for user in users if str(user) not in usersData})
