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

# Logging
tracemalloc.start()
# Warning Suppression
warnings.filterwarnings("ignore", category=UserWarning)

# ======================[ BOT SETUP ]======================
# Your Bot Token and url
Token = BotToken
url = 'http://127.0.0.1:11434/api/chat'

# Define the bot
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
client.chatlog_dir = "logs/"




# ======================[ EVENT HANDLERS ]======================


## ---- On Ready Event ----

@client.event
async def on_ready():
    try:
        print("Message Triggered")
        guild = discord.utils.get(client.guilds, name='The Dark Void of Gaming')
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

UserMessageLog = {}
    
# Message Logging
def MessageLog(author_id, content):
    if author_id not in UserMessageLog:
        UserMessageLog[author_id] = []

    UserMessageLog[author_id].append({"role": "user", "content": content})


@client.event
async def on_message(message):
    
    try:
        # Check if the message starts with '!'
        if message.content.startswith('!'):
            await client.process_commands(message)  # Process the command
            return
        
        # Ignore messages from bots
        if message.author.bot:
            return

        # Check if the message is in 'tamachat' channel or is a DM
        if isinstance(message.channel, discord.DMChannel) or message.channel.name == 'tamachat':

            # Parameters for the POST request
            payload = {"model": "Tamaki", "messages": [{"role": "user", "content": message.content}], "stream": False,}
            # Send the POST request
            response = requests.post(url, json=payload)
            response_data = response.json()
            # Get the text response from the API call
            response_text = response_data.get("message", {}).get("content")
            # Send the text response
            await message.channel.send(response_text)

    except Exception as e:
        print(f"Error in on_message: {str(e)}")

    await client.process_commands(message)


# ======================[ Reload COGs]======================

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

async def LoadCogs():
    # Finds the Cogs
    for filename in os.listdir('./Cogs'):
        # Selects ONLY the Cog Files
        if filename.endswith('.py'):
            # Loads the Cogs
            await client.load_extension(f'Cogs.{filename[:-3]}')
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

