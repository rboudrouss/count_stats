# from django.shortcuts import render
from utils.treatment import update_count
from django.http import HttpResponse, JsonResponse

from utils.getData import get_history, get_user_msgs, get_msgs_date, \
    get_user_date, get_messages, get_user_data, get_users_data, get_count, \
    get_users, get_nb_msg_inter

# Create your views here.
def index(request):
    return HttpResponse("""
    <h1>fromage</h1>
    <p>history</p><p>users</p><p>user</p><p>usermsg</p><p>datemsg</p><p>userdate</p>
    """)

def chat_history(request):
    return JsonResponse(get_history(), safe=False)

def user_msgs(request):
    return JsonResponse(get_user_msgs(id=request.GET.get("id",None)),safe=False)
 
def date_msgs(request):
    return JsonResponse(get_msgs_date(
        mind=request.GET.get("mind",None),
        maxd=request.GET.get("maxd",None),
    ), safe=False)

def user_date(request):
    return JsonResponse(get_user_date(
        mind=request.GET.get("mind",None),
        maxd=request.GET.get("maxd",None),
        id=request.GET.get("id",None)
    ), safe=False)

def msg_info(request):
    return JsonResponse(get_messages(
        mind=request.GET.get("mind",None),
        maxd=request.GET.get("maxd",None),
        id=request.GET.get("id",None),
        infos= request.GET.get("info",None),
    ), safe=False)

def inter_msg(request):
    return JsonResponse(get_nb_msg_inter(
        id=request.GET.get("id",None),
        inter=request.GET.get("inter",None),
        empty=True if request.GET.get("empty", "False").lower()!="false"else False,
        max=request.GET.get("max",None),
    ), safe=False)

def messages(request):
    # TODO update this one
    return JsonResponse(get_messages(
        mind=request.GET.get("mind",None),
        maxd=request.GET.get("maxd",None),
        id=request.GET.get("id",None),
        infos= request.GET.get("info",None),
    ), safe=False)

# Users
def users(request):
    # TODO update this one
    return JsonResponse(get_users(id=request.GET.get("id",None)))

def users_data(request):
    return JsonResponse(get_users_data())

def user_data(request):
    return JsonResponse(get_user_data(id=request.GET.get("id",None)))

# Count
def count(request):
    update_count()
    return JsonResponse(get_count())