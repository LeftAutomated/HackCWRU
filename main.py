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

#################
# Links command #
#################
    
@client.command()
async def links(ctx):
  messageLinks = discord.Embed(title="Psych Central", url="https://psychcentral.com/", description="Psych Central is one of the oldest websites about mental health. The award winning website has been around ever since 1995 and has touched the lives of many. As is quite evident from the name the blog keenly focuses on the psych of a person.", color=0xFFA500)
  messageLinks2 = discord.Embed(title="Headspace", url="https://www.headspace.com/", description="If you are finding it hard to focus on your life-goals all because you are stressed, then you should definitely check Headspace out. It contains hundreds of articles and blogs about mental health.", color=0xFFFFFF)
  messageLinks3 = discord.Embed(title="Therapy Tribe", url="https://support.therapytribe.com/", description="Therapy Tribe takes peer-to-peer mental health support to the next level. Apart from a range of resources, it offers dedicated domains or Tribes for many different issues.", color=0xBF40BF)
  messageLinks4 = discord.Embed(title="Calm Sage", url="https://www.calmsage.com/", description="If you like the idea of sharing your personal stories and discovering people with the same experiences, try out Calm Sage. The website is more educational than a place to connect, but it does welcome guest posts about mental health triumphs.", color=0xFFFF00)
  messageLinks5 = discord.Embed(title="Doxy", url="https://www.calmsage.com/", description="doxy.me is a free, secure, simple online platform for telemedicine. Telemedicine will change the world by making it easier and more affordable for healthcare providers to care for their patients anywhere, including rural and underserved areas. We believe everyone should have access to care through telemedicine.", color=0xADD8E6)
  await ctx.send("**We recommend the following links to help with sadness, anxiety, depression or any sort of negativity:**")
  await ctx.send(embed = messageLinks)
  await ctx.send(embed = messageLinks2)
  await ctx.send(embed = messageLinks3)
  await ctx.send(embed = messageLinks4)
  await ctx.send(embed = messageLinks5)    

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
