# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import socket
from datetime import datetime, time, timedelta



# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Discord bot by: Jake#4526 and tinverse#0593", command_prefix="**", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.

@client.event
async def on_ready():
	print('Logged in as: '+client.user.name)
	print('ID: '+client.user.id)
	print('Connected to '+str(len(client.servers))+' Servers')
	print('Connected to '+str(len(set(client.get_all_members())))+' users')
	print('')
	print('Command Prefix: '+client.command_prefix)
	print('')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('')
	print('Created by Jake#4526 and tinverse#0593 but mostly tinverse')
	await client.change_presence(game=discord.Game(name="with Plebs", type=1))

	

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	
#@client.command()
#async def maple(*args):
#
#    await client.say("Server Checker Starting.")
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    while (True):
#        result = sock.connect_ex(("8.31.99.141", 8484))
#        if result:
#            for connectionAttempt in range(3):
#                if sock.connect_ex(("8.31.99.141", 8484)):
#                    break
#                await asyncio.sleep(10)
#            await client.say("MapleStory is OFFLINE.")
#            while (not result):
#                del result
#                await asyncio.sleep(30)
#                result = sock.connect_ex(("8.31.99.141", 8484))
#            await client.say("@everyone MapleStory is ONLINE.")
#        del result
#        await asyncio.sleep(3600)

#@client.command()
#async def test(*args):
#
#	await client.say("This is a test command")
#	await asyncio.sleep(3)
	

#@client.command()
#async def pst(*args):
#
#	await client.say("PST Timezone is for LOSERS. EST FTW")
#	await asyncio.sleep(3)
	
@client.command()
async def daily(*args):

	today = datetime.utcnow()
	reset = datetime.combine(today.date(), time(0))
	reset = reset + timedelta(days=1)

	dailyStr = "Time till Daily Boss reset:"
	timeStr = str(reset - today)
	await client.say(dailyStr + " " + timeStr)
	await asyncio.sleep(3)

@client.command()
async def weekly(*args):

	today = datetime.utcnow()
	reset = datetime.combine(today.date(), time(0))
	reset = reset+timedelta(days=1)
	
	while reset.date().weekday() != 3:
		reset = reset + timedelta(days=1)

	weeklyStr = "Time till Weekly Boss reset:"
	timeStr = str(reset - today)
	await client.say(weeklyStr + " " + timeStr)
	await asyncio.sleep(3)
	
@client.command()
async def dojo(*args):

	today = datetime.utcnow()
	reset = datetime.combine(today.date(), time(0))
	reset = reset+timedelta(days=1)
	
	while reset.date().weekday() != 0:
		reset = reset + timedelta(days=1)

	weeklyStr = "Time till Guild/Dojo reset:"
	timeStr = str(reset - today)
	await client.say(weeklyStr + " " + timeStr)
	await asyncio.sleep(3)

# After you have modified the code, feel free to delete the line above (line 33) so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('Mzk0ODMyMDgxMDg5MzMxMjAx.DSKDjg.mD12OpX_Esnj_m4R1HCApz2EqPI')

# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.
