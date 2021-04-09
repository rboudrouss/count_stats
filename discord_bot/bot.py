import sys

if __name__ == "__main__":
    args = [arg.lower() for arg in sys.argv[1:]]
    if "help" in args or not args:
        print("""gets optionnal arguments (default False):
        StayOn    : bot'll stays on and listens to new message
        GetMsg    : bot'll get old messages (it'll overwrite all data)
        GetAll    : bot'll fetch ALL messages on start (recommended)
        UpdateAll : bot'll update all users data
        Listen : bot'll listen to new messages and add them to DB
        """)
        exit(0)

sys.path.insert(0, '../')

print("Importing...")
if 1:  # HACK a little hack for my formatter ;v
    import os
    import requests
    from discord import User, Client, Message, errors

    from utils.types import List
    from utils.helpers import data_from_message, data_from_user
    from utils.filePaths import TOKEN_PATH
    from utils.constants import CHANNEL_ID

print("imported & ready to init")

TOKEN = os.environ["TOKEN"] if not TOKEN_PATH.exists(
) else TOKEN_PATH.read_text()
URL = "https://count-stats.herokuapp.com/api/"


def get_all_users() -> List[int]:
    response = requests.get(URL+"user/users")
    return [user["user_id"] for user in response.json()]


def users_not_in_data() -> List[int]:
    response = requests.get(URL+"user/users")
    return [user["user_id"] for user in response.json() if user.get("ghost")]


class Bot(Client):
    def __init__(self, getMsg=True, getAll=False, stayOn=False,
                 updateAll=False, listen=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.getMsg = getMsg
        self.getAll = getAll
        self.stayOn = stayOn
        self.updateAll = updateAll
        self.listen = listen
        print("Connecting to discord...")

    async def on_ready(self):
        print('Connected to discord !')

        if self.getMsg:
            await self.get_msgs(self.getAll)
        self.allUsers = get_all_users()
        self.nUsers = users_not_in_data()
        if self.nUsers:
            await self.update_users_id(self.nUsers)
        if self.updateAll:
            await self.update_users_id(self.allUsers)
        self.allUsers = get_all_users()
        del self.nUsers  # Don't need it anymore
        if not self.stayOn:
            await self.logout()

    async def get_msgs(self, getAll: bool = False):
        print("Fetching new messages...")
        channel = self.get_channel(CHANNEL_ID)
        msg_hst = channel.history(
            limit=(None if getAll else 200),
        )  # .flatten()

        # get all messages
        data = [
            data_from_message(message) async for message in msg_hst
        ]
        response = requests.post(URL+"write/history", json=data)
        print(response.status_code)
        if response.status_code == 200:
            print("message fetched !")
        else:
            print("Something went wrong >.>\n", response.text)

    async def update_users_id(self, users: List[int]):
        print("users not in data: ", users)
        dUsers = []
        for user in users:
            try:
                dUsers.append(await self.fetch_user(user))
            except errors.NotFound:
                print(f"ALERTE user {user} Not Found !")
        self.update_users(dUsers)
        print("Users updated")

    def update_users(self, users: List[User]):
        if type(users) is not list:
            users = [users]
        users = [data_from_user(user) for user in users]
        reponse = requests.post(URL+"write/users", json=users)
        print(reponse.text)

    async def on_message(self, message: Message):
        if not self.listen:
            return
        if message.channel.id == CHANNEL_ID:
            print(f"new message from channel !\n content : {message.content}")
            print(f"user : {message.author.display_name}")
            if str(message.author.id) not in self.allUsers:
                print("New user detected")
                self.update_users(message.author)
                self.allUsers = get_all_users()
                print("User added to DB")
            response = requests.post(
                URL+"write/history", json=data_from_message(message))
            print(response.text)
            print("message added successfully")

    async def on_user_update(self, user: User):
        await self.update_users(user)


def run_bot(**kwargs):
    Bot(**kwargs).run(TOKEN)


if __name__ == "__main__":
    stayOn = "stayon" in args
    getAll = "getall" in args
    getMsg = "getmsg" in args
    updateAll = "updateall" in args
    listen = "listen" in args
    run_bot(
        stayOn=stayOn,
        getAll=getAll,
        getMsg=getMsg,
        updateAll=updateAll,
        listen=listen
    )
