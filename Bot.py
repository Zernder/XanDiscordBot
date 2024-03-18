# TamaBot.py Script

# ======================[ IMPORTS AND INITIALIZATIONS ]======================

import os
import warnings
import tracemalloc
import asyncio
import discord
from discord.ext import commands
from config import BotToken
import requests


tracemalloc.start() # Logging
warnings.filterwarnings("ignore", category=UserWarning) # Warning Suppression


# ======================[ BOT SETUP ]======================


Token = BotToken # Your Bot Token and url
url = 'http://127.0.0.1:11434/api/chat'
client = commands.Bot(command_prefix=".", intents=discord.Intents.all()) # Define the bot
client.chatlog_dir = "logs/"


# ======================[ EVENT HANDLERS ]======================

## ---- On Ready Event ----

@client.event
async def on_ready():
    try:
        print("Message Triggered")
        guild = discord.utils.get(client.guilds, name='The Purple Void of Chaos')
        if guild:
            print(f"Guild found: {guild.name}")
        else:
            print("Guild not found")
            return
        channel = discord.utils.get(guild.text_channels, name='tamachat')
        messages = []
        async for message in channel.history(limit=10):
            messages.append(message)
        for message in messages:
            if message.author.bot:
                continue
            MessageLog(message.author.id, message.content)
    except Exception as e:
        print(f"An error occurred in on_ready: {e}")


## ---- On Message Event ----



# Message Logging
UserMessageLog = {}

def MessageLog(author_id, content):
    if author_id not in UserMessageLog:
        UserMessageLog[author_id] = []

    UserMessageLog[author_id].append({"role": "user", "content": content})


@client.event
async def on_message(message):
    try:
        if message.content.startswith('!'): # Check if the message starts with '!'
            await client.process_commands(message)  # Process the command
            return
        if message.author.bot: # Ignore messages from bots
            return
        if isinstance(message.channel, discord.DMChannel) or message.channel.name == 'tamachat': # Check if the message is in 'tamachat' channel or is a DM
            payload = {"model": "Tamaki", "messages": [{"role": "user", "content": message.content}], "stream": False,} # Parameters for the POST request
            response = requests.post(url, json=payload) # Send the POST request
            response_data = response.json() # Get the text response from the API call
            response_text = response_data.get("message", {}).get("content")
            await message.channel.send(response_text) # Send the text response
    except Exception as e:
        print(f"Error in on_message: {str(e)}")
    await client.process_commands(message)


# ======================[ Reload COGs]======================


@client.command()
async def reload(ctx, extension):
    extension_name = f'Cogs.{extension}'
    if extension_name in client.extensions:
        try:
            await client.unload_extension(extension_name)
        except Exception as e:
            await ctx.send(f'Could not unload the extension {extension}. Error: {e}')
            return
    else:
        await ctx.send(f'The extension {extension} is not loaded, attempting to load...')


async def LoadCogs():
    for filename in os.listdir('./Cogs'): # Finds the Cogs
        if filename.endswith('.py'): # Selects ONLY the Cog Files
            await client.load_extension(f'Cogs.{filename[:-3]}') # Loads the Cogs
        else:
            print(f'Unable to load {filename[:-3]}')


# ======================[ MAIN ROUTINE ]======================


# =====================
# Run The Bot
# =====================


async def main():
    # Loads the Cogs
    await LoadCogs()
    # Tells me Tama is Online!  
    print("Tama Online!")
    # Starts the Discord Bot
    await client.start(Token)


if __name__ == "__main__":
    asyncio.run(main())

