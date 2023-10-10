import discord
from discord import Forbidden, app_commands
from discord.ext import commands

class SlashModeration(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print("SlashModeration Enabled")


    @app_commands.command(name= "ping", description= "Ping the bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.client.latency * 1000)}ms")


    @app_commands.command(name="purge", description="Clear chat messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, interaction: discord.Interaction, count: int):
        try:
            await interaction.channel.purge(limit=count)
            await interaction.send_message(f"{count} message(s) have been deleted")

        except Forbidden:
            await interaction.send("Missing permissions")

        except Exception as e:
            await interaction.send(f"Purge failed: {e}")
    print("Purge loaded")

    @app_commands.command(name="kick", description="Kick Member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member=None,):
        if member is None:
            member = interaction.user
        elif member is not None:
            member = member
        
        if member is None:
            await interaction.send_message("Please mention a member to kick.")
        elif member == interaction.author:
            await interaction.send_message("You cannot kick yourself.")
        elif member == interaction.guild.owner:
            await interaction.send_message("You cannot kick the owner.")
        elif member.top_role >= interaction.author.top_role:
            await interaction.send_message("You cannot kick someone with a higher role than you.")
        else:
            await interaction.guild.kick(member)
            await interaction.send_message(f"{member.mention} has been kicked from the server {interaction.author.mention}.")
        await interaction.user.kick(discord.Member)
        await interaction.send_message(f"{interaction.member.mention} has been kicked from the server {interaction.author.mention}.")
        print("Kick loaded")

    # @app_commands.command(name="ban", description="Bans Member")
    # @commands.has_permissions(ban_members=True)
    # async def ban(self, interaction: discord.Interaction, member: discord.member, modreason):
    #     await interaction.guild.ban(member)

    #     conf_embed = discord.Embed(title="Success!", color=discord.Color.blurple())
    #     conf_embed.add_field(name="Banned", value=f"{member.mention} has been Banned from the server {interaction.author.mention}.", inline=False)
    #     conf_embed.add_field(name="Reason", value=modreason, inline=False)

    #     await interaction.send(embed=conf_embed)
    #     print("Ban loaded")

    # @app_commands.command(name="unban")
    # @commands.guild_only()
    # @commands.has_permissions(ban_members=True)
    # async def unban(self, interaction, userId):
    #     user = discord.Object(id=userId)
    #     await interaction.guild.unban(user)

    #     conf_embed = discord.Embed(title="Success!", color=discord.Color.blurple())
    #     conf_embed.add_field(name="Unbanned", value=f"{userId} has been Banned from the server {interaction.author.mention}.", inline=False)

    #     await interaction.send(embed=conf_embed)
    #     print("Unban loaded")

async def setup(client):
    await client.add_cog(SlashModeration(client))