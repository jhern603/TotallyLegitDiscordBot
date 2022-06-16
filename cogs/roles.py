
import discord
import random
from discord.ext import commands


class roles(commands.Cog):

    listylist=["cortadio","espresso","americano","italiano"]

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giverole(self, ctx):
        await ctx.send("giverole ran")

    @commands.command()
    async def removerole(self, ctx):
        await ctx.send("removerole ran")
    @commands.command()
    async def getroles(self, ctx):
        for role in ctx.guild.roles:
            if str(role) != "@everyone":
                await ctx.send(f"Role: {str(role)}")



def setup(client):
    client.add_cog(roles(client))
