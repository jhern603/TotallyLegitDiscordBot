
import discord
from discord.ext import commands
import logging

class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giverole(self, ctx):
        await ctx.send("giverole ran")

    # Need to implement check to see if user has the role(s)
    @commands.command()
    async def removerole(self, ctx, user: discord.User, *roles):
        user_roles = user.roles
        await ctx.send(f"Removed the following roles from {str(user)}:")
        for role in user_roles:
            if str(role) != "@everyone":
                if user_roles:
                    ctx.send(f"{str(user)} does not have the {role} role!")
                else:
                    await user.remove_roles(role)
                    logging.info(f"Removed{role} from {str(user)}")
                    await ctx.send(f"\t{role}")
                    
    @commands.command()
    async def getroles(self, ctx):
        for role in ctx.guild.roles:
            if str(role) != "@everyone":
                await ctx.send(f"Role: {str(role)}")



def setup(client):
    client.add_cog(roles(client))
