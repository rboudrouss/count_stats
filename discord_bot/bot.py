import sys
import os
from discord import User, Client, Message, errors

if __name__ == "__main__":
    args = [arg.lower() for arg in sys.argv[1:]]
    if "help" in args:
        print("""gets optionnal arguments (default False):
        StayOn    : bot'll stays on and listens to new message
        GetMsg    : bot'll get old messages (it'll overwrite all data)
        GetAll    : bot'll fetch ALL messages on start (recommended in production)
        UpdateAll : bot'll update all users data 
        Listen : bot'll listen to new messages and add them to DB
        """)
        exit(0)

sys.path.insert(0,'../')

from utils.writeData import append_history, write_history, append_users
from utils.treatment import users_not_in_data
from utils.getData import get_all_users
from utils.constants import CHANNEL_ID
from utils.filePaths import TOKEN_PATH
from utils.helpers import data_from_message, data_from_user
from utils.types import List

TOKEN = os.environ["TOKEN"] if not TOKEN_PATH.exists() else TOKEN_PATH.read_text()

class Bot(Client):
    def __init__(self, getMsg=True, getAll=False, stayOn=False, updateAll=False,listen=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.getMsg = getMsg
        self.getAll = getAll
        self.stayOn = stayOn
        self.updateAll = updateAll
        self.listen = listen
        self.allUsers = get_all_users()

    async def on_ready(self):
        print('bot on !')

        if self.getMsg : await self.get_msgs(self.getAll)
        self.allUsers = get_all_users()
        self.nUsers = users_not_in_data()
        if self.nUsers: await self.update_users_id(self.nUsers)
        if self.updateAll: await self.update_users_id(self.allUsers)
        self.allUsers = get_all_users()
        del self.nUsers # Don't need it anymore
        if not self.stayOn: await self.logout()
    
    async def get_msgs(self, getAll:bool=False):
        print("Fetching new messages...")
        channel = self.get_channel(CHANNEL_ID)
        msg_hst = channel.history(limit=(None if getAll else 200))#.flatten()
        
        # get all messages
        write_history([
            data_from_message(message) async for message in msg_hst
        ])
        print("messages fetched !")
    
    async def update_users_id(self, users:List[int]):
        print("users not in data: ", users)
        if type(users) is not list : users = [users]
        dUsers = []
        for user in users:
            try:
                dUsers.append(await self.fetch_user(user))
            except errors.NotFound:
                print(f"ALERTE user {user} Not Found !")
        self.update_users(dUsers)
        print("Users updated")
    
    def update_users(self, users:List[User]):
        data = {}
        if type(users) is not list : users=[users]
        for user in users:
            data = dict(data, **data_from_user(user))
        append_users(data)
    
    async def on_message(self, message:Message):
        if not self.listen: return 
        if message.channel.id == CHANNEL_ID: 
            print(f"new message from channel !\n content : {message.content}")
            print(f"user : {message.author.display_name}")
            if str(message.author.id) not in self.allUsers:
                print("New user detected")
                self.update_users(message.author)
                self.allUsers = get_all_users()
                print("User added to DB")
            append_history(data_from_message(message))
            print("message added successfully")
    
    async def on_user_update(self, user:User):
        await self.update_users(user)

def run_bot(**kwargs):
    Bot(**kwargs).run(TOKEN)

if __name__ == "__main__":
    listen = stayOn = getAll = getMsg = updateAll = False
    if "stayon" in args: stayOn=True
    if "getall" in args: getAll=True
    if "getmsg" in args: getMsg=True
    if "updateall" in args: updateAll=True
    if "listen" in args: listen=True
    run_bot(
        stayOn=stayOn,
        getAll=getAll,
        getMsg=getMsg,
        updateAll=updateAll,
        listen=listen
    )
