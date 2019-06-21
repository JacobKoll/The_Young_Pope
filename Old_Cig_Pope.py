import time
import socket
import subprocess
import discord
from discord.ext import commands

class CigPope():
    bot = commands.Bot(command_prefix='>')
    shell = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE)

    @bot.command()
    async def start(ctx, shell=shell):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        await ctx.send('Starting server...')
        shell.stdin.write(b'\n')
        shell.stdin.flush()
        while(sock.connect_ex(('', ))):
            pass

        shell.stdin.write(b'ssh \n')
        shell.stdin.flush()
        await ctx.send('Server started launching game server...')
        shell.stdin.write(b'cd Servers/MinecrapServers/MinecrapLITV/LITV-Serverpack-1.11/\n')
        shell.stdin.flush()
        shell.stdin.write(b'bash LaunchServer.sh\n')
        shell.stdin.flush()


    @bot.command()
    async def shutdown(ctx, shell=shell):
        await ctx.send('Shutting down server...')
        shell.stdin.write(b'/stop\n')
        shell.stdin.flush()
        time.sleep(10)
        shell.stdin.write(b'sudo shutdown -h now\n')
        shell.stdin.flush()
        await ctx.send('...Server shutdown')

    @bot.command()
    async def kill(ctx, shell=shell):
        await ctx.send('Killing server')
        shell.kill()
    
    @bot.command()
    async def ssh(ctx, shell=shell):
        await ctx.send('Blah...')
        shell.stdin.write(b'ssh \n')
        shell.stdin.flush()
        await ctx.send('ssh...')

    @bot.command()
    async def ifconfig(ctx, shell=shell):
        await ctx.send('Blah...')
        shell.stdin.write(b'ifconfig\n')
        shell.stdin.flush()
        await ctx.send('ifconfig...')

    bot.run('')

CigPope()
