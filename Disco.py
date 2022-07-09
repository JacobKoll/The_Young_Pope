import os
import requests
from Env_Vars import *

class Discord():

    def __init__(self, bot_token):
        self.name = "Discord API Wraper"
        self.base_url = 'https://discord.com/api/users/@me'
        self.bot_token = bot_token
        self.bot_channel_id = "406684281004621824"

    def auth(self):
        headers = {'authorization': self.bot_token, 'user-agent': 'my-app/0.0.1'}
        payload = {"content": "hello world"}
        response = requests.get(self.base_url, headers=headers)
        return response
