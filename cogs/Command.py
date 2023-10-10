import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Enabled")
    
    @commands.command(name="Purge", description="Clear chat messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f"{count} message(s) have been deleted")
        print("Purge loaded")

    @commands.command(name="Kick", description="Kick Member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.member, modreason):
        await ctx.guild.kick(member)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.blurple())
        conf_embed.add_field(name="Kicked", value=f"{member.mention} has been kicked from the server {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)
        print("Kick loaded")

    @commands.command(name="ban", description="Bans Member")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.member, modreason):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.blurple())
        conf_embed.add_field(name="Banned", value=f"{member.mention} has been Banned from the server {ctx.author.mention}.", inline=False)
        conf_embed.add_field(name="Reason", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)
        print("Ban loaded")

    @commands.command(name="Unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.blurple())
        conf_embed.add_field(name="Unbanned", value=f"{userId} has been Banned from the server {ctx.author.mention}.", inline=False)

        await ctx.send(embed=conf_embed)
        print("Unban loaded")


async def setup(client):
    await client.add_cog(Moderation(client))
    