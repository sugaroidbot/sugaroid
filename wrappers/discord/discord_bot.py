# bot.py
import importlib
import os
import random
import shlex
import shutil
import subprocess
from datetime import datetime

from nltk import word_tokenize

import sugaroid as sug
from sugaroid import sugaroid, ver
import discord
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
sg = sugaroid.Sugaroid()
sg.toggle_discord()
client = discord.Client()
interrupt_local = True


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    os.chdir(os.path.dirname(sug.__file__))
    await client.change_presence(activity=discord.Game(name='v{} since {:02d}:{:02d} UTC'
                                 .format(ver.version().get_commit(), datetime.utcnow().hour,
                                         datetime.utcnow().minute)))


@client.event
async def on_message(message):
    if message.author == client.user:
        print(f'my id is {message.author}')
        return
    global interrupt_local
    if message.content.startswith('<@684746563540484099>') or message.content.startswith('<@!684746563540484099>') or \
            message.content.startswith('!S'):

        msg = message.content\
            .replace('<@684746563540484099>', '')\
            .replace('<@!684746563540484099>', '')\
            .replace('!S', '')\
            .strip()
        if 'update' in message.content:
            if str(message.author) == 'srevinsaju#8324':
                await message.channel.send(f"Starting Python pip upgrade. Updating sugaroid from "
                                           f"https://github.com/srevinsaju/sugaroid/archive/master.zip")
                pop = subprocess.Popen(
                    shlex.split('{pip} install -U https://github.com/srevinsaju/sugaroid/archive/master.zip'
                                .format(pip=shutil.which('pip'))),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                pop.communicate()
                try:
                    stdout = pop.stdout.read().decode()
                except ValueError:
                    stdout = None
                try:
                    stderr = pop.stderr.read().decode()
                except ValueError:
                    stderr = None

                await message.channel.send(f"pip3 install gives traceback stdout={stdout} "
                                           f"stderr={stderr}")
                os.chdir('/')
                importlib.reload(sug)
                importlib.reload(sugaroid)
                importlib.reload(ver)

                await message.channel.send("Sugaroid reloaded")

                os.chdir(os.path.dirname(sug.__file__))

                await client.change_presence(activity=discord.Game(name='v{} since {:02d}:{:02d} UTC'
                                                                   .format(ver.version().get_commit(),
                                                                           datetime.utcnow().hour,
                                                                           datetime.utcnow().minute)))
                await message.channel.send("version refreshed")
                return
            elif 'stop' in message.content and 'learn' in message.content:
                global interrupt_local
                interrupt_local = False
                await message.channel.send("InterruptAdapter terminated")
            else:
                await message.channel.send(f"I am sorry @{message.author}. I would not be able to update myself.\n"
                                           f"Seems like you do not have sufficient permissions")
                return

        response = sg.parse(msg)
        lim = 1995
        if len(str(response)) >= lim:
            response1 = str(response)[:lim] + '...'
            await message.channel.send(response1)

            if len(str(response)) >= (2 * lim):
                response2 = str(response)[lim:2*lim] + '...'
                await message.channel.send(response2)
                
                if len(str(response)) >= (3*lim):
                    response2 = str(response)[2*lim:3*lim] + '...'
                    await message.channel.send(response2)
                    response2 = str(response)[3 * lim:4 * lim]
                    await message.channel.send(response2)
                else:
                    response2 = str(response)[2 * lim:3 * lim]
                    await message.channel.send(response2)
            else:
                response2 = str(response)[lim:2 * lim]
                await message.channel.send(response2)
        else:
            await message.channel.send(response)
        return

    elif interrupt_local:
        token = word_tokenize(message.content)
        for i in range(len(token)):
            if str(token[i]).startswith('@'):
                token.pop(i)
        if len(token) <= 5:
            messages = ' '.join(token)
            author = message.author.mention
            sg.append_author(author)
            sg.interrupt_ds()
            response = sg.parse(messages)
            print(response, 's'*5)
            await message.channel.send(response)
        return

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'general':
            await channel.send(channel, 'Welcome {}'.format(str(member)))

client.run(token)