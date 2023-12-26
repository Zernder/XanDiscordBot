# TamaBot.py Script

# ======================[ IMPORTS AND INITIALIZATIONS ]======================

import warnings
import os
import asyncio
import tracemalloc
import discord
from discord.utils import get
from discord.ext import commands
import openai
from kasa import SmartBulb
from config import BotToken, OpenAIKey, APIprompt, Channel


tracemalloc.start()
UserMessageLogs = {}


# ======================[ BOT SETUP ]======================
# Your OpenAI API key and Bot Token
openai.api_key = OpenAIKey
Token = BotToken
OpenAIPrompt = APIprompt
Channel = Channel

# Define the bot
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.chatlog_dir = "logs/"



# Inside your code, before the warning occurs, you can suppress it like this:
warnings.filterwarnings("ignore", category=UserWarning)


# =====================
# Main Async Function
# =====================


## ---- On Ready Event ----

@client.event
async def on_ready():
    try:
        print("on_ready Triggered")
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
            add_message_to_log(message.author.id, message.content)

    except Exception as e:
        print(f"An error occurred in on_ready: {e}")



# ==========================
# Message Logging
# ==========================


def add_message_to_log(author_id, content):
    if author_id not in UserMessageLogs:
        UserMessageLogs[author_id] = [{"role": "system", "content": OpenAIPrompt}]
    UserMessageLogs[author_id].append({"role": "user", "content": content})



## ---- On Message Event ----

@client.event
async def on_message(message):
    try:
        # Check if the message starts with '!'
        if message.content.startswith('!'):
            await client.process_commands(message)  # Process the command
            return  # Exit the function without further processing for OpenAI
        
        # Ignore messages from bots
        if message.author.bot:
            return

        # Check if the message is in 'tamachat' channel or is a DM
        if isinstance(message.channel, discord.DMChannel) or message.channel.name == Channel:
            # Add the received message to the log
            add_message_to_log(message.author.id, message.content)

            # Check if there's enough messages for a proper conversation
            if len(UserMessageLogs[message.author.id]) >= 2:
                # Make an OpenAI API call to get the completion
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=UserMessageLogs[message.author.id],
                    max_tokens=75,
                    temperature=0.7
                )

                # Get the text response from the API call
                response_text = completion.choices[0].message['content']

                # If the message is too long, trim it
                if len(response_text.split()) > 50:
                    response_text = ". ".join(response_text.split(". ")[:-1]) + "."

                # Add the response to the log
                UserMessageLogs[message.author.id].append({"role": "assistant", "content": response_text})

                # Send the text response
                await message.channel.send(response_text)

    except Exception as e:
        print(f"Error in on_message: {str(e)}")

    await client.process_commands(message)




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

async def LoadCogs():
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'Cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename[:-3]}')



async def main():
    await LoadCogs() 
    print("Bot Online!")
    await client.start(Token)


if __name__ == "__main__":
    asyncio.run(main())

