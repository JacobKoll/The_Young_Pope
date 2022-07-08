import os
import asyncio
from Env_Vars import *

class Discord():

    def __init__(self):
        self.name = "Discord API Wraper"

    def auth(self):
        return self.name

class CigPope():

    def __init__(self):
        self.name = "CigPope"
        self.bot_key = os.environ.get('OFICIAL_BOT_KEY')
        self.disco = Discord()

    def start(self):
        print(self.name)
        print(self.bot_key)
        print(self.disco.auth())

pope = CigPope()
pope.start()
