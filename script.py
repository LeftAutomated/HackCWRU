import discord
from discord.ext import commands
import requests
import os
import random
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

@client.command()
async def quote(ctx):
    response = requests.get("https://type.fit/api/quotes")
    quote_arr = response.json()
    rand = random.randint(0, len(quote_arr))
    quote = quote_arr[rand]['text'] + " \n- " + quote_arr[rand]['author']
    await ctx.send(quote)

client.run(token)
