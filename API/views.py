# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getData import *

# Create your views here.
def index(request):
    return HttpResponse("fromage")

def chat_history(request):
    return JsonResponse(get_history(), safe=False)

def users_data(request):
    return JsonResponse(get_users())

def user_data(request):
    return JsonResponse(get_user(id=request.GET.get("id",False)))

def user_msgs(request):
    return JsonResponse(get_user_msgs(id=request.GET.get("id",False)),safe=False)
 
def date_msgs(request):
    min_ = request.GET.get("min",False)
    max_ = request.GET.get("max",False)
    if not min_ and not max_ : return JsonResponse([], safe=False)
    return JsonResponse(get_msgs_date(
        mind=min_,
        maxd=max_,
    ), safe=False)

def user_date(request):
    return JsonResponse(get_user_date(
        mind=request.GET.get("min",False),
        maxd=request.GET.get("max",False),
        id=request.GET.get("id",False)
    ), safe=False)