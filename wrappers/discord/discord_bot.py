# bot.py
import importlib
import os
import random
import shlex
import shutil
import subprocess
import psutil
import discord
import sugaroid_commands as scom
from datetime import datetime
from nltk import word_tokenize
import sugaroid as sug
from sugaroid import sugaroid, ver
from dotenv import load_dotenv
import time
from datetime import timedelta

process = psutil.Process()
init_cpu_time = process.cpu_percent()




load_dotenv()
token = os.getenv('DISCORD_TOKEN')
sg = sugaroid.Sugaroid()
sg.toggle_discord()
client = discord.Client()
interrupt_local = False
start_time = datetime.now()


async def update_sugaroid(message):
    # initiate and announce to the user of the upgrade
    await message.channel.send(
        "Updating my brain with new features :smile:"
        "(https://github.com/srevinsaju/sugaroid)"
    )

    # execute pip3 install
    pip=shutil.which('pip')
    pip_popen_subprocess = subprocess.Popen(
        shlex.split(
            f'{pip} install -U '
            f'https://github.com/srevinsaju/sugaroid/archive/master.zip'
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # process information from the pip installer from Popen
    ecode = pip_popen_subprocess.wait(10000)
    out, err = pip_popen_subprocess.communicate()
    stdout, stderr = out.decode(), err.decode()
    await message.channel.send(
        f"I updated my brain. ```{stdout}``` "
        f"stderr=```{stderr}```. Exited with {ecode}"
    )

    # reload modules
    os.chdir('/')
    importlib.reload(sug)
    importlib.reload(sugaroid)
    importlib.reload(ver)

    # updating the bot
    os.chdir(os.path.dirname(sug.__file__))
    git=shutil.which('git')
    # reset --hard
    git_reset_popen_subprocess = subprocess.Popen(
        shlex.split(f'{git} reset --hard origin/master'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).wait(500)
    # git pull
    git_pull_popen_subprocess = subprocess.Popen(
        shlex.split(f'{git} pull'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # process information from the git
    ecode = git_pull_popen_subprocess.wait(10000)
    out, err = git_pull_popen_subprocess.communicate()
    stdout, stderr = out.decode(), err.decode()

    importlib.reload(scom)

    # announce to the users
    await message.channel.send(
        f"I updated the bot. ```{stdout}``` "
        f"stderr=```{stderr}``` Exited with {ecode}"
    )

    await client.change_presence(
        activity=discord.Game(
            name='v{} since {:02d}:{:02d} UTC'.format(
                ver.version().get_commit()[:10],
                datetime.utcnow().hour,
                datetime.utcnow().minute
            )
        )
    )
    await message.channel.send("Update completed. :smile:")
    return



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    os.chdir(os.path.dirname(sug.__file__))
    await client.change_presence(activity=discord.Game(name='v{} since {:02d}:{:02d} UTC'
                                 .format(ver.version().get_commit()[:10], datetime.utcnow().hour,
                                         datetime.utcnow().minute)))




@client.event
async def on_message(message):
    if message.author == client.user:
        print("Ignoring message sent by another Sugaroid Instance")
        return
    global interrupt_local

    if any((
        message.content.startswith('<@684746563540484099>'),
        message.content.startswith('<@!684746563540484099>'),
        message.content.startswith('!S')
    )):
        # clean the message
        msg = message.content\
            .replace('<@684746563540484099>', '')\
            .replace('<@!684746563540484099>', '')\
            .replace('!S', '')\
            .strip()

        command_processor = scom.SugaroidDiscordCommands(client)

        is_valid_command = await command_processor.call_command(msg, message)
        print("Recv")
        if is_valid_command:
            return

        elif 'update' in msg and len(msg) <= 7:
            if str(message.author) == 'srevinsaju#8324':
                update_sugaroid(message)
            else:
                # no permissions
                await message.channel.send(
                    f"I am sorry @{message.author}. I would not be able to update myself.\n"
                    f"Seems like you do not have sufficient permissions"
                )
            return

        elif 'stop' in message.content and 'learn' in message.content:
            if str(message.author) == 'srevinsaju#8324':
                global interrupt_local
                interrupt_local = False
                await message.channel.send("InterruptAdapter terminated")
            else:
                await message.channel.send(
                    f"I am sorry @{message.author}. I would not be able to update myself.\n"
                    f"Seems like you do not have sufficient permissions"
                )
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
