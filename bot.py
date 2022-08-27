# This file includes all functions related to the Discord Bot

# Import Discord API
import discord
from discord.ext import commands

TOKEN = 'MTAxMjU3NzgwNDMzODA5MDAwNQ.GAU-D0.NUOenrKIB41npiu1lJ4UxNvkOdswS0GvD5H2Gw'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)


@client.event
async def on_ready():
    # Bot has been properly initialized
    print("{0.user} has been initialized".format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
# Runs Bot
client.run(TOKEN) 