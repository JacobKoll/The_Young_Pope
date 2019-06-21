import os
import socket
import subprocess
import discord
import mcstatus
import asyncio
from discord.ext import commands

# The start server handles starting the server machine and launching the game server.
async def start_server(ctx, shell):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    await ctx.send('Starting server machine...')
    shell.stdin.write(b'wakeonlan \n')
    shell.stdin.flush()
    while(sock.connect_ex(('', ))):
        pass
    await ctx.send('Connecting to the server machine...')
    shell.stdin.write(b'ssh \n')
    shell.stdin.flush()
    await ctx.send('Connected to the server machine.')
    await ctx.send('Launching game server...')
    shell.stdin.write(b'cd Test\n')
    shell.stdin.flush()
    shell.stdin.write(b'python3 wait.py\n')
    shell.stdin.flush()
    #shell.stdin.write(b'cd Servers/MinecrapServers/MinecrapLITV/LITV-Serverpack-1.11/\n')
    #shell.stdin.flush()
    #shell.stdin.write(b'bash LaunchServer.sh\n')
    #shell.stdin.flush()
    await ctx.send('Launched game server.')

# The shutdown loop handles automatically shutting down the server and the machine when no one is online.
async def shutdown_loop(ctx, shell):
    await asyncio.sleep(20)
    #server = mcstatus.MinecraftServer.lookup("")
    #players = server.status().players.online
    #while(players > 0):
    #    await ctx.send('Checking server population...')
    #    await asyncio.sleep(10)
    #    players = server.status().players.online
    #    await ctx.send(players)
    #    if players == 0:
    #        await ctx.send('No one is online shutting down server in 15 minutes unless someone gets online...')
    #        await asyncio.sleep(10)
    #        players = server.status().players.online
    await ctx.send('Shutting down game server...')
    await asyncio.sleep(5)
    shell.stdin.write(b'end\n')
    shell.stdin.flush()
    await asyncio.sleep(5)
    #shell.stdin.write(b'/stop\n')
    #shell.stdin.flush()
    await ctx.send('Game server shutdown.')
    #await asyncio.sleep(30)
    await ctx.send('Shutting down server machine...')
    shell.stdin.write(b'sudo shutdown -h now\n')
    shell.stdin.flush()
    await ctx.send('Server machine shutdown.')
      
class CigPope(discord.Client):
    gaurd = False
    shell = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE)

    # This commands the game server to start and then automatically shutdown when no one is on.
    #async def start(self, shell=shell):
    #    start_server_task = asyncio.create_task(start_server(ctx, shell))
    #    shutdown_loop_task = asyncio.create_task(shutdown_loop(ctx, shell))
    #    await start_server_task
    #    await shutdown_loop_task

    # This command is a test of the bot commands.
    async def on_message(self, message):
        
        if message.content.startswith('<<'):
            command = message.content[2:]
            if command == 'start':
                if self.gaurd:
                    await message.channel.send('Server is running...')
                    return
                self.gaurd = True
                await message.channel.send('Starting the server...')
            else:
                await message.channel.send('Shut the fuck up!')
bot = CigPope()
bot.run('')
