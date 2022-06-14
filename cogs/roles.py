
import discord
from discord.ext import commands


class roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giverole(self, ctx):
        await ctx.send("giverole ran")

    @commands.command()
    async def removerole(self, ctx):
        await ctx.send("removerole ran")


def setup(client):
    client.add_cog(roles(client))
