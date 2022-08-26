# This file includes all functions related to the Discord Bot

# Import Discord API
import discord

TOKEN = 'MTAxMjU3NzgwNDMzODA5MDAwNQ.GbEPvB.Dium6fMViGBtplen4FSpTBl9HasKfyJ18bTGPU'

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    # Bot has been properly initialized
    print("{0.user} has been initialized".format(client))

# Runs Bot
client.run(TOKEN) 