import os
import socket
import subprocess
import discord
import mcstatus
import asyncio
from discord.ext import commands
from Env_Vars import *

# The start server handles starting the server machine and launching the game server.
async def start_server(ctx, shell):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    await ctx.send('Starting server machine...')
    shell.stdin.write(str.encode('wakeonlan '+os.environ.get('SERVER_MAC')+'\n'))
    shell.stdin.flush()
    while(sock.connect_ex((os.environ.get('SERVER_IP'), int(os.environ.get('SERVER_PORT'))))):
        pass
    await ctx.send('Connecting to the server machine...')
    shell.stdin.write(str.encode('ssh '+os.environ.get('SERVER_SSH_LOGIN')+'\n'))
    shell.stdin.flush()
    await ctx.send('Connected to the server machine.')
    await ctx.send('Launching game server...')
    shell.stdin.write(b'cd Servers/MinecrapServers/MinecrapLITV/LITV-Serverpack-1.11/\n')
    shell.stdin.flush()
    shell.stdin.write(b'bash LaunchServer.sh\n')
    shell.stdin.flush()
    await ctx.send('Launched game server.')

# The shutdown loop handles automatically shutting down the server and the machine when no one is online.
async def shutdown_loop(ctx, shell):
    await asyncio.sleep(900)
    server = mcstatus.MinecraftServer.lookup(os.environ.get('PUBLIC_SERVER_IP')+':'+os.environ.get('PUBLIC_SERVER_PORT'))
    players = server.status().players.online
    while(players > 0):
        await ctx.send('Checking server population...')
        await asyncio.sleep(900)
        players = server.status().players.online
        await ctx.send(players)
        if players == 0:
            await ctx.send('No one is online shutting down server in 15 minutes unless someone gets online...')
            await asyncio.sleep(900)
            players = server.status().players.online

    await ctx.send('Shutting down game server...')
    await asyncio.sleep(5)
    shell.stdin.write(b'/stop\n')
    shell.stdin.flush()
    await ctx.send('Game server shutdown.')
    await asyncio.sleep(30)
    await ctx.send('Shutting down server machine...')
    shell.stdin.write(b'sudo shutdown -h now\n')
    shell.stdin.flush()
    await ctx.send('Server machine shutdown.')
       
class CigPope():
    bot = commands.Bot(command_prefix='>')
    shell = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE)

    # This commands the game server to start and then automatically shutdown when no one is on.
    @bot.command()
    async def start(ctx, shell=shell):
        start_server_task = asyncio.create_task(start_server(ctx, shell))
        shutdown_loop_task = asyncio.create_task(shutdown_loop(ctx, shell))
        await start_server_task
        await shutdown_loop_task

    # This command is a test of the bot commands.
    @bot.command()
    async def hello(ctx):
        await ctx.send('Shut the fuck up!')

    bot.run(os.environ.get('OFICIAL_BOT_KEY'))

asyncio.run(CigPope())
