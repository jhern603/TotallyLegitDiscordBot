import discord
from discord.ext import commands
import datetime


class utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Shows the ping/latency of the bot in miliseconds.", short="Shows ping.")
    async def ping(self, ctx):
        if round(self.client.latency * 1000) <= 50:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0x44ff44)
        elif round(self.client.latency * 1000) <= 100:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0xffd000)
        elif round(self.client.latency * 1000) <= 200:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0xff6600)
        else:
            embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(self.client.latency *1000)}** milliseconds!", color=0x990000)
        await ctx.send(embed=embed)
    
    @commands.command(help="Shows information about the server.", short="Shows server info.")
    async def info(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description=f"{ctx.guild.description}",
                              timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at",
                        value=f"{ctx.guild.created_at}")
        embed.add_field(name="Number of Members",
                        value=f"{ctx.guild.member_count}")
        embed.add_field(name="Server Owner",
                        value=f"{ctx.guild.owner}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(
            url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    
    @commands.command(help="Counts the number of users in the server (including bots).", short="Counts users.")
    async def countusers(self, ctx):
        await ctx.send(f"There are {ctx.guild.member_count} members in the server")


def setup(client):
    client.add_cog(utilities(client))
