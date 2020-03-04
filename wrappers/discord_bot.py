# bot.py
import os
import random

import discord
from dotenv import load_dotenv

from sugaroid.sugaroid import Sugaroid

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
sg = Sugaroid()
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

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


client.run(token)