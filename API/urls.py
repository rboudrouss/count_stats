from django.urls import path

from .views import *

urlpatterns = [
    # path('', .index, name='index'),
    # Message data
    path('message/history',chat_history, name='history'),
    path('message/usermsg', user_msgs, name='user messages'),
    path('message/datemsg', date_msgs, name='date messages'),
    path('message/userdate', user_date, name='user date message'),
    path('message/msginfo', msg_info, name="message info selection"),
    path('message/inter', inter_msg, name="nb message by interval"),
    path('message', messages, name="Messages"),
    # user data
    path('user/users',users_data, name='users'),
    path('user/user', user_data, name='user'),
    path('user', users, name="user"),
    # count data
    path('count', count, name="count"),
]