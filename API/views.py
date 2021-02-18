# from django.shortcuts import render
from utils.treatment import update_count
from django.http import HttpResponse, JsonResponse

from utils.getData import get_history, get_user_msgs, get_msgs_date, \
    get_user_date, get_messages, get_user_data, get_users_data, get_count, \
    get_users

# Create your views here.
def index(request):
    return HttpResponse("""
    <h1>fromage</h1>
    <p>history</p><p>users</p><p>user</p><p>usermsg</p><p>datemsg</p><p>userdate</p>
    """)

def chat_history(request):
    return JsonResponse(get_history(), safe=False)

def user_msgs(request):
    return JsonResponse(get_user_msgs(id=request.GET.get("id",False)),safe=False)
 
def date_msgs(request):
    min_ = request.GET.get("mind",False)
    max_ = request.GET.get("maxd",False)
    if not min_ and not max_ : return JsonResponse([], safe=False)
    return JsonResponse(get_msgs_date(
        mind=min_,
        maxd=max_,
    ), safe=False)

def user_date(request):
    return JsonResponse(get_user_date(
        mind=request.GET.get("mind",False),
        maxd=request.GET.get("maxd",False),
        id=request.GET.get("id",False)
    ), safe=False)

def msg_info(request):
    return JsonResponse(get_messages(
        mind=request.GET.get("mind",False),
        maxd=request.GET.get("maxd",False),
        id=request.GET.get("id",False),
        infos= request.GET.get("info",False),
    ), safe=False)

def messages(request):
    # TODO update this one
    return JsonResponse(get_messages(
        mind=request.GET.get("mind",False),
        maxd=request.GET.get("maxd",False),
        id=request.GET.get("id",False),
        infos= request.GET.get("info",False),
    ), safe=False)

# Users
def users(request):
    # TODO update this one
    return JsonResponse(get_users(id=request.GET.get("id",False)))

def users_data(request):
    return JsonResponse(get_users_data())

def user_data(request):
    return JsonResponse(get_user_data(id=request.GET.get("id",False)))

# Count
def count(request):
    update_count()
    return JsonResponse(get_count())