import discord
import time
# from secret_things import TESTERS, BOT_TOKEN, CHANNEL_ID
import json

CONFIG = json.loads(open("config.json",'r').read())

class Bot(discord.Client):
    def __init__(self, getMsg=False, getAll=False, getUsers=[], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.getMsg = getMsg
        self.getAll = getAll
        self.getUsers = getUsers

    async def on_ready(self):
        print('bot on !')
        if self.getMsg : await self.get_msgs(self.getAll)
        if self.getUsers:
            for userID in self.getUsers:
                await self.get_user(userID)
        await self.logout()
    
    async def get_msgs(self, getAll=False):
        while not self.is_ready: time.sleep(.5)
        channel = self.get_channel(CONFIG["channelid"])
        msg_hst = channel.history(limit=(None if getAll else 10))#.flatten()
        
        # get all messages
        open("temp/history.json",'w').write(json.dumps([
            {
                "message_id":message.id,
                "author_id":message.author.id,
                "content":message.content,
                "date":list(message.created_at.timetuple()),
             } async for message in msg_hst
        ], indent=(4 if not getAll else None)))
    
    async def get_user(self, id):
       pass 
        


def get_hst(getAll=False):
    client = Bot(getMsg=True, getAll=getAll)
    # messages = await client.get_msgs()
    client.run(CONFIG["token"])
    return open("test.json",'r').read()

def get_users(users=CONFIG["testers"]):
    pass

if __name__ == "__main__":
    print(get_hst())
