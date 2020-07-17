import discord
import psutil
import time
from datetime import timedelta

process = psutil.Process()
init_cpu_time = process.cpu_percent()


class SugaroidDiscordCommands:
    def __init__(self, client):
        self.commands = {
            "stat": self.stat
        }
        self.client = client

    async def call_command(self, command, message):
        print("Call")
        command = str(command).lower().strip()
        print("Received command: ", command)
        return await self.commands.get(command, self.do_nothing)(message)
    
    async def do_nothing(self, message):
        return False

    async def stat(self, message):
        # get and send stats
        # Modified from 
        # https://github.com/SwagLyrics/SwagLyrics-discord-bot/blob/50d05b60c913981db80c223e57bba2c5b8c6dded/SwagLyricsBot/dev_commands.py#L23-$6
        info = await self.client.application_info()
        total_ram = (psutil.virtual_memory().total >> 30) + 1
        embed = discord.Embed(
            title="Sugaroid Stats",
            description=f"Running on a Heroku server with {total_ram}GB RAM \n.")
        embed.add_field(name="**__General Info__**", inline=False, value="\u200b")
        embed.add_field(name="Latency", value=f"{self.client.latency*1000:.03f}ms")
        embed.add_field(name="Guild Count", value=f"{len(self.client.guilds):,}")
        embed.add_field(name="User Count", value=f"{len(self.client.users):,}")
        embed.add_field(name="**__Technical Info__**", inline=False, value="\u200b")
        embed.add_field(name="System CPU Usage", value=f"{psutil.cpu_percent():.02f}%")
        embed.add_field(name="System RAM Usage",
                        value=f"{psutil.virtual_memory().used/1048576:.02f} MB")
        embed.add_field(name="System Uptime",
                        value=f'{timedelta(seconds=int(time.time() - psutil.boot_time()))}')
        embed.add_field(name="Bot CPU Usage", value=f"{process.cpu_percent():.02f}%")
        embed.add_field(name="Bot RAM Usage", value=f"{process.memory_info().rss / 1048576:.02f} MB")
        embed.add_field(name="Bot Uptime",
                        value=f'{timedelta(seconds=int(time.time() - process.create_time()))}')
        embed.set_footer(text=f'Made by {info.owner}', icon_url=info.owner.avatar_url)
        await message.channel.send(embed=embed)
        return True
