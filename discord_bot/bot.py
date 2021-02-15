import discord
from time import sleep
import json
from typing import List, Dict


CONFIG = json.loads(open("../config.json",'r').read())

class Bot(discord.Client):
    def __init__(self, getMsg=False, getAll=False, users=[], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.getMsg = getMsg
        self.getAll = getAll
        self.users_ = users

    async def on_ready(self):
        print('bot on !')
        if self.getMsg : await self.get_msgs(self.getAll)
        if self.users_:
            print("calling self.get_users fonction")
            await self.get_users(self.users_)
        try : await self.logout()
        except: pass
    
    async def get_msgs(self, getAll=False):
        channel = self.get_channel(CONFIG["channelid"])
        msg_hst = channel.history(limit=(None if getAll else 200))#.flatten()
        
        # get all messages
        open("../data/history.json",'w').write(json.dumps([
            {
                "message_id":message.id,
                "author_id":message.author.id,
                "content":message.content,
                "date":list(message.created_at.timetuple())[:6],
            } async for message in msg_hst
        ]))
    
    async def get_users(self, users):
        print("in function users: ", users)
        dUsers = [await self.fetch_user(user) for user in users]
        print("in function dUsers",dUsers)
        open("../com/users.json", "w").write(
            json.dumps(
                {
                    user.id : {
                        "avatar_url":   str(user.avatar_url),
                        "name":         user.display_name,
                        "discriminator":user.discriminator,
                        "id":           user.id,
                    } for user in dUsers 
                } 
            )
        )

def get_hst(getAll=False, force=False, update=False):
    # TODO make this code more clear
    if force and update:
        try : data = json.loads(open("../data/users.json").read())
        except FileNotFoundError: data = {}
        hst = json.loads(open("../data/history.json").read())
        users = list({message["author_id"] for message in hst})
        nUsers = [user for user in users if user not in data]
        print("Users that are not in data : ", nUsers)
        if not update or not nUsers: return data
        print("updating the users...")
        Bot(getMsg=True, getAll=getAll, users=nUsers).run(CONFIG["token"])
        print("users updated !")
        open("../data/users.json",'w').write(json.dumps(dict(data,**json.loads(open("../com/users.json",'r').read()))))
        print("users successfuly writed")
    elif force: Bot(getMsg=True, getAll=getAll).run(CONFIG["token"])
    elif update:
        try : data = json.loads(open("../data/users.json").read())
        except FileNotFoundError: data = []
        hst = json.loads(open("../data/history.json").read())
        users = list({message["author_id"] for message in hst})
        nUsers = [user for user in users if user not in data]
        print("Users that are not in data : ", nUsers)
        if not update or not nUsers: return data
        print("updating the users...")
        Bot(users=nUsers).run(CONFIG["token"])
    return json.loads(open("../data/history.json").read())

def run_bot():
    Bot().run(CONFIG["token"])

if __name__ == "__main__":
    get_hst(force=True, update=True)