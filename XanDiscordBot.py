# TamaBot.py Script

# ======================[ IMPORTS AND INITIALIZATIONS ]======================

import warnings
import discord
from discord.utils import get
from discord.ext import commands
import asyncio
from kasa import SmartBulb
import openai
import tracemalloc
import os
from config import BotToken



tracemalloc.start()

# ======================[ GLOBAL VARIABLES ]================================
user_message_logs = {}

Token = BotToken

# ======================[ BOT SETUP ]======================

# Define the bot
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.chatlog_dir = "logs/"



# Inside your code, before the warning occurs, you can suppress it like this:
warnings.filterwarnings("ignore", category=UserWarning)


# ======================[ EVENT HANDLERS ]======================


## ---- On Ready Event ----

@client.event
async def on_ready():
    pass

## ---- On Message Event ----

@client.event
async def on_message(message):
    # Check if the message starts with '!'
    if message.content.startswith('!'):
        await client.process_commands(message)  # Process the command





# ======================[ Load and Reload COGS]======================

@client.command()
async def reload(ctx, extension):
    extension_name = f'Cogs.{extension}'
    # First try to unload the extension if it's already loaded
    if extension_name in client.extensions:
        try:
            await client.unload_extension(extension_name)
        except Exception as e:
            await ctx.send(f'Could not unload the extension {extension}. Error: {e}')
            return  # Stop the command if unloading fails
    else:
        await ctx.send(f'The extension {extension} is not loaded, attempting to load...')
 # Now try to load the extension
    try:
        await client.load_extension(extension_name)
        await ctx.send(f'Reloaded {extension} successfully!')
    except Exception as e:
        # Send a different message if it's now being loaded for the first time
        if extension_name not in client.extensions:
            await ctx.send(f'Loaded {extension} successfully!')
        else:
            await ctx.send(f'Could not load the extension {extension}. Error: {e}')

async def load():
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'Cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename[:-3]}')

# =====================
# Main Async Function
# =====================

async def main():
    # This function will be called from the main.py, so it should be an async function
    # and should not start the event loop itself.
    await load()  # This loads any necessary components, e.g., Cogs.
    print("Bot Online!")
    await client.start(Token)

# The following block allows the script to run independently.
if __name__ == "__main__":
    asyncio.run(main())

