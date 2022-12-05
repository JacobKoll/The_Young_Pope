import random
import discord
from discord.ext import commands
from Env_Vars import *

# This example requires the 'message_content' intent.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

token = os.environ.get('BOT_TOKEN')
client.run(token)
