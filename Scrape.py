import os
import sys
import json
import discord
from os import system
from discord.ext import commands

if sys.platform == "linux":
    clear = lambda: system("clear")
else:
    clear = lambda: system("cls")

with open('Config.json') as f:
    config = json.load(f)

Token = config.get('Token')
Bot = config.get('Bot')
intents = discord.Intents.all()
intents.members = True
if Bot == True:
    client = commands.Bot(command_prefix="Luna!", case_insensitive=False, self_bot=True, intents=intents)
else:
    client = commands.Bot(command_prefix="Luna!", case_insensitive=False, intents=intents)

@client.event
async def on_connect():
    clear()
    print('''
     \x1b[38;5;199m    __                     
        / /   __  ______  ____ _
       / /   / / / / __ \/ __ `/
      / /___/ /_/ / / / / /_/ / 
     /_____/\__,_/_/ /_/\__,_/  \x1b[0mBETA\x1b[0m
    ''')
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mAuthenticated Token!")
    try:
        os.remove("Scraped/Members.txt")
        os.remove("Scraped/Channels.txt")
        os.remove("Scraped/Roles.txt")
    except:
        pass

    guild = input(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mGuild\x1b[38;5;199m: \x1b[0m")
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()

    members_ = 0
    f = open("Scraped/Members.txt", "a+")
    for member in members:
        f.write(f"{member.id}\n")
        members_ += 1
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mScraped {members_} Members!")

    channels = 0
    f = open("Scraped/Channels.txt", "a+")
    for channel in guildOBJ.channels:
        f.write(f"{channel.id}\n")
        channels += 1
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mScraped {channels} Channels!")

    roles = 0
    f = open("Scraped/Roles.txt", "a+")
    for role in guildOBJ.roles:
        f.write(f"{role.id}\n")
        roles += 1
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mScraped {roles} Roles!")

try:
    client.run(Token, bot=Bot)
except:
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mInvalid Token!")
    input()
    exit()