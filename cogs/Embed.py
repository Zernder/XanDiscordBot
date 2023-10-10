import discord
from discord.ext import commands


class MyEmbed(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Embeds are ready")

    @commands.command()
    async def embed(self,ctx):
        embed_message = discord.Embed(title="Title of embed", description="Description of embed", color=discord.Color.dark_purple())

        embed_message.set_author(name=f"requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field name", value="Field value", inline=False)
        embed_message.set_footer(text="This is the footer", icon_url=ctx.author.avatar)

        await ctx.send(embed = embed_message)


async def setup(client):
    await client.add_cog(MyEmbed(client))