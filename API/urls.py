from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history',views.chat_history, name='history'),
    path('users',views.users_data, name='users'),
    path('user', views.user_data, name='user'),
    path('usermsg', views.user_msgs, name='user messages'),
    path('datemsg', views.date_msgs, name='date messages'),
    path('userdate', views.user_date, name='user date message')
]