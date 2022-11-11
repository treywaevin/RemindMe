# This file includes all functions related to the Discord Bot

# Import Modules
import discord
from discord.ext import commands, tasks
import re
import datetime
from datetime import date
from reminder import *

TOKEN = 'ENTER TOKEN HERE'

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = ".",intents=intents)

# Get current time and date
today = date.today()

remtime = today.strftime("%m/%d/%Y")

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
    if ctx.message.author == client.user:
        return
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
        
        if is_present(split_msg[1:]):
            await ctx.send("Assignment name already exists")
            return 0


    # Create New Assignment Object
    add_assignment(" ".join(split_msg[1:]),split_msg[0])

    await ctx.send("Assignment successfully added!")

@client.command(
    name="list", description="lists all assignments sorted by due date"
)

async def list(ctx):
    if ctx.message.author == client.user:
        return
    # Print Out All Assignments
    for i in list_subjects():
        await ctx.send(i)

@client.command(
    name="remove", description="Removes entry from assignment list"
)

async def remove(ctx):
    if ctx.message.author == client.user:
        return
    
    embed = discord.Embed(
        title="Please Enter title of assignment you'd like to remove",
    )
    sent = await ctx.send(embed=embed)

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if is_present(msg.content):
        del_assignment(msg.content)
        await ctx.send("Assignment Deleted")
    else:
        await ctx.send("Assignment does not exist")


@client.command(
    name="notify", description="Toggles assignment notification"
)

async def notify(ctx, enabled="start"):
    if enabled.lower() == "stop":
        alertUser.stop()
        await ctx.send("Notifications have been disabled")
    elif enabled.lower() == "start":
        alertUser.start(ctx)
        await ctx.send("Notifications have been enabled")

@tasks.loop(hours = 12)
async def alertUser(ctx):
    # Check if current date matches due date of one of your assignments
    for i in asgns:
        print(i.due_date, remtime)
        if i.due_date == remtime:
            await ctx.send("The assignment: {}, is due today!".format(i.name))



# Runs Bot
client.run(TOKEN) 