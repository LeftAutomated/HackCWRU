import discord
from discord.ext import commands, tasks
import requests
import os
import random
from dotenv import load_dotenv
from jokeapi import Jokes
from datetime import datetime, timedelta
import asyncio


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

def create_embed(title, url, description):
    return discord.Embed(title=title, url=url, description=description, color=0xFF5733)

# Command invoked with !hotline
@client.command("hotline")
async def command_hotlines(ctx):
    hotlines = {
        "SAMSHA National Helpline": "1-800-662-4357",
        "NAMI": "1-800-950-6264",
        "National Suicide Prevention Hotline": "1-800-273-8255",
        "Boys Town Hotline": "1-800-448-3000"
    }
    hotline_message = "**Here are several mental health hotlines to call:** \n\n"
    for name, number in hotlines:
        hotline_message += hotline + '\n'
    await ctx.send(hotline_message)

@client.command('joke')
async def joke_command(ctx):
    j = await Jokes()
    joke = await j.get_joke(blacklist=['nsfw', 'racist', 'sexist', 'religious'])
    joke_message = ""
    if joke["type"] == "single": # Print the joke
        joke_message += joke["joke"]
    else:
        joke_message += joke["setup"]
        joke_message += joke["delivery"]
    await ctx.send(joke_message)

@client.command('meme')
async def command_meme(ctx):
    base_url = "https://meme-api.herokuapp.com/gimme"
    r = requests.get(base_url)
    r = r.json()
    image_url = r["url"]
    await ctx.send(image_url)

@tasks.loop(seconds=10)
async def command_quote():
    channel = client.get_channel(954837807187247255)
    r = requests.get("https://zenquotes.io/api/random").json()
    quote = r[0]["q"]
    author = r[0]["a"]
    await channel.send(quote + "\n --" + author)

@command_quote.before_loop
async def before():
    now = datetime.now()
    target = datetime(*now.timetuple()[0:3], hour=16, minute=11)

    if target < now:  # if the target is before now, add one day
        target += datetime.timedelta(days=1)

    diff = target - now
    await asyncio.sleep(diff.seconds)
    await client.wait_until_ready()
    print("Finished waiting")

command_quote.start()
client.run(token)
