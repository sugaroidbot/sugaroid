# bot.py
import os
import random
from datetime import datetime

import sugaroid
import discord
from dotenv import load_dotenv
from sugaroid.ver import version
from sugaroid.sugaroid import Sugaroid

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
sg = Sugaroid()
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    os.chdir(os.path.dirname(sugaroid.__file__))
    await client.change_presence(activity=discord.Game(name='v{} since {:02d}:{:02d} UTC'
                                 .format(version().get_commit(), datetime.utcnow().hour, datetime.utcnow().minute)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<@684746563540484099>') or message.content.startswith('<@!684746563540484099>'):
        msg = message.content.replace('<@684746563540484099>', '').replace('<@!684746563540484099>', '')
        response = sg.parse(msg)
        if len(str(response)) > 1999:
            response = str(response)[:1999]
        await message.channel.send(response)
    else:
        print(message.content)

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'general':
            await channel.send(channel, 'Welcome {}'.format(str(member)))

client.run(token)