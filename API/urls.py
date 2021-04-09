from django.urls import path

from . import views

urlpatterns = [
    # path('', .index, name='index'),
    # Message data
    path('message/history', views.get_history, name='history'),
    path('message/usermsg', views.user_msgs, name='user messages'),
    path('message/datemsg', views.date_msgs, name='date messages'),
    # path('message/userdate', views.user_date, name='user date message'),
    path('message/inter', views.inter_msg, name="nb message by interval"),
    path('message', views.messages, name="Messages"),
    # user data
    path('user/users', views.users_data, name='users'),
    path('user/user', views.user_data, name='user'),
    path('user', views.users, name="user"),
    # write
    path('write/history', views.write_history, name='write history'),
    path('write/users', views.write_users, name="write users"),
]
