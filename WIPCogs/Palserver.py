import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from rcon.source import Client as RCONClient

class PalServer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.rcon = RCONClient('192.168.1.100', 25575)

    @commands.Cog.listener()
    async def on_ready(self):
        print("PalServer Ready")
        await self.client.tree.sync()

    # Static method to check for allowed users
    @staticmethod
    async def is_allowed_user(interaction: discord.Interaction):
        allowed_users = []  # User IDs go here
        return interaction.user.id in allowed_users

    async def execute_rcon_command(self, command):
        response = await self.rcon.run(command)
        return response

    @app_commands.command(name="shutdown", description="Shutdown the server.")
    async def shutdown(self, interaction: discord.Interaction, seconds: int = None, message: str = None):
        command = f"/Shutdown"
        if seconds is not None:
            command += f" {seconds}"
        if message is not None:
            command += f' "{message}"'
        result = await self.execute_rcon_command(command)
        await interaction.response.send_message(result)

    @app_commands.command(name="doexit", description="Force stop the server.")
    async def do_exit(self, interaction: discord.Interaction):
        result = await self.execute_rcon_command("/DoExit")
        await interaction.response.send_message(result)

    @app_commands.command(name="broadcast", description="Send message to all players in the server.")
    async def broadcast(self, interaction: discord.Interaction, message: str):
        result = await self.execute_rcon_command(f"/Broadcast {message}")
        await interaction.response.send_message(result)

    @app_commands.command(name="kickplayer", description="Kick player by SteamID from the server.")
    async def kick_player(self, interaction: discord.Interaction, steam_id: str):
        result = await self.execute_rcon_command(f"/KickPlayer {steam_id}")
        await interaction.response.send_message(result)

    @app_commands.command(name="banplayer", description="Ban player by SteamID from the server.")
    async def ban_player(self, interaction: discord.Interaction, steam_id: str):
        result = await self.execute_rcon_command(f"/BanPlayer {steam_id}")
        await interaction.response.send_message(result)

    @app_commands.command(name="showplayers", description="Show information on all connected players.")
    async def show_players(self, interaction: discord.Interaction):
        result = await self.execute_rcon_command("/ShowPlayers")
        await interaction.response.send_message(result)

    @app_commands.command(name="info", description="Show server information.")
    async def server_info(self, interaction: discord.Interaction):
        result = await self.execute_rcon_command("/Info")
        await interaction.response.send_message(result)

    @app_commands.command(name="save", description="Save the world data.")
    async def save(self, interaction: discord.Interaction):
        result = await self.execute_rcon_command("/Save")
        await interaction.response.send_message(result)

async def setup(client):
    await client.add_cog(PalServer(client))
