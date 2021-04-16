from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta
from itertools import groupby
from tqdm import tqdm

from .serializers import MessageDataSerializer, UserDataSerializer
from .models import MessageData, UserData


@api_view(['GET'])
def get_history(request):
    history = MessageData.objects.all().order_by("date")
    serializer = MessageDataSerializer(history, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def write_history(request):
    data = request.data
    if type(data) is not list:
        data = [data]
    for msg in data:
        exist = MessageData.objects.filter(message_id=msg["message_id"])
        print("\ngot", msg["message_id"])
        if not exist:
            print(msg["message_id"], "does not exist")
            if msg["content"] == '':
                msg["content"] = "NaN"
            serializer = MessageDataSerializer(data=msg)
            if serializer.is_valid():
                serializer.save()
                print(msg["message_id"], "added !")
            else:
                print(
                    f"{serializer.errors}\nyup, that's somme \
                        quality weird data\n{msg}\n")
    return Response(data)


@api_view(["GET"])
def user_msgs(request):
    try:
        user_id = request.GET["id"]
    except KeyError:
        raise ValidationError("we kinda need an id")
    data = MessageData.objects.filter(author_id=user_id)
    serializer = MessageDataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def date_msgs(request):
    try:
        mind = datetime.fromisoformat(request.GET["mind"])
    except KeyError:
        raise ValidationError("we kinda need at least the mind date")
    except ValueError:
        raise ValidationError("eww... weird mind date")

    maxd = request.GET.get("maxd")
    if not maxd:
        maxd = (mind + timedelta(days=1)).isoformat()
    else:
        try:
            maxd = datetime.fromisoformat(maxd)
        except ValueError:
            raise ValidationError("eww... weird maxd date")
    history = MessageData.objects.filter(date__range=[mind, maxd])
    serializer = MessageDataSerializer(history, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def inter_msg(request):
    id = request.GET.get("id")
    if id:
        history = MessageData.objects.filter(author_id=id)
    else:
        history = MessageData.objects.all()

    history = history.order_by("date")

    history_by_date = groupby(history.iterator(), lambda m: m.date.date())

    messages_dict = {}

    for date, group_of_messages in history_by_date:
        dict_key = date.strftime('%Y-%m-%d')
        messages_dict[dict_key] = MessageDataSerializer(
            group_of_messages,
            many=True
        ).data
    return Response([[k, v] for k, v in messages_dict.items()])


def messages(request):
    # TODO update this one
    pass

# Users


@ api_view(['GET'])
def users(request):
    try:
        user_id = request.GET["id"]
        data = UserData.objects.filter(user_id=user_id)
    except KeyError:
        data = UserData.objects.all().order_by("nb_msg")
    serializer = UserDataSerializer(data, many=True)
    return Response(reversed(serializer.data))


@ api_view(['GET'])
def users_data(request):
    history = UserData.objects.all().order_by("nb_msg")
    serializer = UserDataSerializer(history, many=True)
    return Response(reversed(serializer.data))


@ api_view(['POST'])
def write_users(request):
    data = request.data
    if type(data) is not list:
        data = [data]
    for msg in (tqdm(data) if len(data) > 20 else data):
        serializer = UserDataSerializer(data=msg)
        if serializer.is_valid():
            serializer.save()
        else:
            print(f"{serializer.errors}\nWarning, got weird data : \n{msg}\n")
    return Response(data)


@ api_view(["GET"])
def user_data(request):
    try:
        user_id = request.GET["id"]
    except KeyError:
        raise ValidationError("we kinda need an id")
    data = UserData.objects.filter(user_id=user_id)
    serializer = UserDataSerializer(data, many=True)
    return Response(serializer.data)
