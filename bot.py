# This file includes all functions related to the Discord Bot

# Import Modules
import discord
from discord.ext import commands
import re
from reminder import Assignment, add_assignment, list_subjects

TOKEN = 'MTAxMjU3NzgwNDMzODA5MDAwNQ.GAU-D0.NUOenrKIB41npiu1lJ4UxNvkOdswS0GvD5H2Gw'

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = ".",intents=intents)


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

    await client.process_commands(message)
    
# This command allows the user to add an assignment
@client.command(
    name="add", description="Adds new assignment to list"
)

async def add(ctx):
    # Comparable to check if date is formatted correctly
    date_format = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"

    # Compile regular express
    date = re.compile(date_format)

    
    embed = discord.Embed(
        title="Please Enter Due Date (DD/MM/YYYY) and Assignment Name",
    )
    sent = await ctx.send(embed=embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)

    if msg:
        split_msg = msg.content.split(" ")

        # Check if date matches
        match = re.fullmatch(date,split_msg[0])

        if match is None:
            await ctx.send("Date not valid")
            return 0

        if len(split_msg) == 1:
            await ctx.send("Assignment name not inputted")
            return 0

    # Create New Assignment Object
    add_assignment(" ".join(split_msg[1:]),split_msg[0])


# Runs Bot
client.run(TOKEN) 