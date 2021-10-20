import discord
import os
from discord.ext import commands
import logging
import json
import random

logging.basicConfig(level=logging.DEBUG)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
# intents.members = True

bot = commands.Bot(command_prefix='/')

chuck_norris_jokes = json.loads(open("jokes.json", "r").read())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    logging.error(f"Error: {error}")
    await ctx.send(f"{error}")

@bot.command()
async def hello(ctx):
    try:
        await ctx.send("Hello World")
    except Exception as e:
        logging.error(str(e))


@bot.command()
async def chuck(ctx, arg):
    logging.debug(f"Sending joke")
    random_joke_id = random.randint(0, 99)
    joke = chuck_norris_jokes[random_joke_id]
    await ctx.send(f"{joke}")




bot.run(os.getenv('TOKEN'))
