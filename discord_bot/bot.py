import discord
import json
import sys

sys.path.insert(0,'../')

from utils.writeData import write_history, append_users
from utils.treatment import users_not_in_data

CONFIG = json.loads(open("./config.json",'r').read())

class Bot(discord.Client):
    def __init__(self, getMsg=True, getAll=False, stayOn=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.getMsg = getMsg
        self.getAll = getAll
        self.stayOn = stayOn

    async def on_ready(self):
        print('bot on !')

        if self.getMsg : await self.get_msgs(self.getAll)
        self.nUsers = users_not_in_data()
        if self.nUsers:
            await self.get_users(self.nUsers)
        if not self.stayOn: await self.logout()
    
    async def get_msgs(self, getAll=False):
        channel = self.get_channel(CONFIG["channelid"])
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
    
    async def get_users(self, users):
        print("users not in data: ", users)
        dUsers = [await self.fetch_user(user) for user in users]
        append_users({
            user.id : {
                "avatar_url":   str(user.avatar_url),
                "name":         user.display_name,
                "discriminator":user.discriminator,
                "id":           user.id,
            } for user in dUsers 
        })


def run_bot(getAll = False, stayOn = True):
    Bot(getAll=getAll, stayOn=stayOn).run(CONFIG["token"])

if __name__ == "__main__":
    run_bot(getAll = False, stayOn = False)