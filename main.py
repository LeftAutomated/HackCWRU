import discord
from discord.ext import commands
import requests
import os
import random
from dotenv import load_dotenv
from jokeapi import Jokes

load_dotenv()

token = os.getenv('TOKEN')
prefix = os.getenv('PREFIX')

client = commands.Bot(command_prefix = prefix)

##########
# events #
##########

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)

#################
# quote command #
#################

@client.command('quote')
async def quote_command(ctx):
    response = requests.get("https://type.fit/api/quotes")
    quote_arr = response.json()
    rand = random.randint(0, len(quote_arr))
    quote = quote_arr[rand]['text'] + " \n- " + quote_arr[rand]['author']
    await ctx.send(quote)


####################
# hotlines command #
####################

hotline_names = ["SAMSHA National Helpline", 
                 "NAMI", 
                 "National Suicide Prevention Hotline", 
                 "Boys Town Hotline"]
hotline_links = ["https://www.samhsa.gov/find-help/national-helpline", 
                 "https://www.nami.org/help", 
                 "https://suicidepreventionlifeline.org/", 
                 "https://www.boystown.org/hotline/Pages/default.aspx"]
hotline_numbers = ["1-800-662-4357", 
                   "1-800-950-6264",
                   "1-800-273-8255",
                   "1-800-448-3000"]

@client.command('hotlines')
async def hotlines_command(ctx):
    embed = discord.Embed()

    title = "Hotlines"
    desc = ""
    color = discord.Color.blue();

    for i in range(len(hotline_names)):
        desc += hotline_numbers[i] + " -- "
        desc += "[" + hotline_names[i] + "]"
        desc += "(" + hotline_links[i] + ")"
        desc += "\n"

    embed.title = title
    embed.description = desc
    embed.color = color

    await ctx.send(embed=embed)


################
# joke command #
################

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


################
# meme command #
################

@client.command('meme')
async def meme_command(ctx):
    base_url = "https://meme-api.herokuapp.com/gimme"
    r = requests.get(base_url)
    r = r.json()
    image_url = r["url"]
    await ctx.send(image_url)


client.run(token)
