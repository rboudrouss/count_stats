# useless but i may need it later
from . import fbinit

DATABASE = fbinit.db

DATA = DATABASE.child("data")

HISTORY = DATA.child("history")

USERS = DATA.child("users")

COUNT = DATA.child("count")
