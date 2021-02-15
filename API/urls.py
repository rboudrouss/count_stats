from API.getData import get_messages
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # Message data
    path('message/history',views.chat_history, name='history'),
    path('message/usermsg', views.user_msgs, name='user messages'),
    path('message/datemsg', views.date_msgs, name='date messages'),
    path('message/userdate', views.user_date, name='user date message'),
    path('message/msginfo', views.msg_info, name="message info selection"),
    path('message', views.messages, name="Messages"),
    # user data
    path('user/users',views.users_data, name='users'),
    path('user/user', views.user_data, name='user'),
    path('user', views.users, name="user"),
]