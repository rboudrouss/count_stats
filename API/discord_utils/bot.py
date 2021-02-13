import discord
from time import sleep
import json
import asyncio

CONFIG = json.loads(open("./config.json",'r').read())

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
        msg_hst = channel.history(limit=(None if getAll else 50))#.flatten()
        
        # get all messages
        open("data/history.json",'w').write(json.dumps([
            {
                "message_id":message.id,
                "author_id":message.author.id,
                "content":message.content,
                "date":list(message.created_at.timetuple()),
            } async for message in msg_hst
        ], indent=(4 if not getAll else None)))
    
    async def get_users(self, users):
        print("in function users: ", users)
        dUsers = [await self.fetch_user(user) for user in users]
        print("in function dUsers",dUsers)
        open("com/users.json", "w").write(
            json.dumps([
                {
                    user.id : {
                        "avatar_url":   str(user.avatar_url),
                        "color":        user.color.value,
                        "name":         user.display_name,
                        "discriminator":user.discriminator,
                    }
                } for user in dUsers 
            ], indent=4)
        )
    # FIXME
    def start_async(self, *args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.start(*args, **kwargs))
        except KeyboardInterrupt:
            loop.run_until_complete(self.logout())
            # cancel all tasks lingering
        finally:
            loop.close()

if __name__ == "__main__":
    Bot().run(CONFIG["token"])