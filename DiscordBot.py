import discord
from discord.ext import commands
from config import TOKEN
import asyncio
import os
from SakiVocab import load_all_vocab_files
import random


# Keep track of conversation history for each user
conversation_history = {}

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.chatlog_dir = "logs/"

# Load all vocab files from the "SakiVocab" directory
vocab_data = load_all_vocab_files()

@client.event
async def on_ready():
    await client.tree.sync()
    print(f'Bot is ready. Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    user_input = message.content.lower()  # Convert user input to lowercase for case-insensitive matching

    # Iterate through all vocab data and check for trigger words and responses
    for vocab_info in vocab_data.items():
        specific_triggers = vocab_info.get("TriggerWords", {})
        random_responses = vocab_info.get("RandomResponses", [])

        # Check if the user's message matches any specific trigger word
        for trigger_word in specific_triggers:
            if trigger_word in user_input:
                response = random.choice(random_responses)
                await message.channel.send(response)
                return

    # If no specific trigger word is matched from any vocab file, send a default response
    default_responses = ["I'm not sure what you mean.", "Could you please clarify?", "Let's talk about something else."]
    response = random.choice(default_responses)
    await message.channel.send(response)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename[:-3]}')

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())
