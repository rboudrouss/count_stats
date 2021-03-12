import discord
import sys
import os

sys.path.insert(0,'../')

from utils.writeData import append_history, write_history, append_users
from utils.treatment import users_not_in_data
from utils.getData import get_all_users
from utils.constants import CHANNEL_ID
from utils.filePaths import TOKEN_PATH 

TOKEN = os.environ["TOKEN"] if not TOKEN_PATH.exists() else TOKEN_PATH.read_text()
class Bot(discord.Client):
    def __init__(self, getMsg=True, getAll=False, stayOn=False, updateAll=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.getMsg = getMsg
        self.getAll = getAll
        self.stayOn = stayOn
        self.updateAll = updateAll
        self.nUsers = users_not_in_data()

    async def on_ready(self):
        print('bot on !')

        if self.getMsg : await self.get_msgs(self.getAll)
        if self.nUsers: await self.update_users(self.nUsers)
        if self.updateAll: await self.update_users(get_all_users())
        if not self.stayOn: await self.logout()
    
    async def get_msgs(self, getAll=False):
        channel = self.get_channel(CHANNEL_ID)
        msg_hst = channel.history(limit=(None if getAll else 200))#.flatten()
        
        # get all messages
        write_history([
            {
                "message_id":message.id,
                "author_id":message.author.id,
                "content":message.content,
                "date":list(message.created_at.timetuple())[:6],
            } async for message in msg_hst
        ])
    
    async def update_users(self, users):
        print("users not in data: ", users)
        dUsers = [await self.fetch_user(int(user)) for user in users]
        append_users({
            user.id : {
                "avatar_url":   str(user.avatar_url),
                "name":         user.display_name,
                "discriminator":user.discriminator,
                "id":           str(user.id),
            } for user in dUsers 
        })
        print("Users updated")
    
    async def on_message(self, message):
        if message.channel.id == CHANNEL_ID: 
            print(f"new message from channel !\n content : {message.content}")
            print(f"user : {message.author.display_name}")
            append_history({
                "message_id":message.id,
                "author_id":message.author.id,
                "content":message.content,
                "date":list(message.created_at.timetuple())[:6],
            })
            print("message added successfully")

if __name__ == "__main__":
    Bot(stayOn=True, getAll=False).run(TOKEN)