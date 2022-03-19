import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
prefix = os.getenv('PREFIX')

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)

@client.command()
async def yomom(ctx):
    response = requests.get('https://api.yomomma.info/')
    joke = response.json()
    await ctx.send(joke['joke'])

@client.command()
async def yodad(ctx):
    response = requests.get('https://api.yomomma.info/')
    joke = response.json()
    dadjoke = joke['joke'].replace("mamma", "dadda")
    dadjoke = dadjoke.replace("her", "his")
    dadjoke = dadjoke.replace("she", "he")
    await ctx.send(dadjoke)

client.run(token)
