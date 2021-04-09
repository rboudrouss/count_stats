from datetime import datetime

# from .helpers import date_from_msg, str_from_date
from .constants import DELAY_CACHE
from .types import MessageData, List, Optional, Union, MsgCount
from cachetools import cached, TTLCache

# TODO ?


@cached(cache=TTLCache(maxsize=1, ttl=120))
def get_history() -> List[MessageData]:
    pass


@cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_user_msgs(id: Optional[Union[str, int]] = None) -> List[MessageData]:
    pass


@cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_msgs_date(mind: Optional[str] = None, maxd: Optional[str] = None) \
        -> List[MessageData]:
    pass


@cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_user_date(mind=None, maxd=None, id=None) -> List[MessageData]:
    pass


returnType = List[Union[MessageData, str, int, datetime, None]]


@cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_msg_info(mind=None, maxd=None, id=None, infos=None)\
        -> returnType:
    pass


@ cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_messages(mind, maxd, id, infos) \
        -> List[Union[MessageData, str, int, datetime, None]]:
    pass


@ cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_nb_msg_inter(id: int = None, inter: str = None,
                     max: Union[int, str] = None, empty: bool = False)\
        -> List[MsgCount]:
    pass

# Users


def get_users(id=None): return get_user_data(id)


@ cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_users_data():
    pass


@ cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_user_data(id=None):
    pass


@ cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_all_users(fast=True):
    pass

# Classement


@ cached(cache=TTLCache(maxsize=10, ttl=DELAY_CACHE))
def get_count():
    pass
