
import discord
from discord.ext import commands
from discord.utils import get
import logging


class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True, name="removerole", aliases=['takeroles', 'removeroles'], help="Takes away a role from a user", short="Take role from user")
    async def removerole(self, ctx, user: discord.User, *roles):
        mod_role = ctx.author.guild_permissions.administrator
        if mod_role:
            user_roles = user.roles
            if len(roles) == 0:
                await ctx.send(f"You have called $removerole but didn't pass what roles to remove!")
                return
            if len(str(user)) == 0:
                await ctx.send(f"You have called $removerole but didn't pass what user to remove roles from!")
                return
            if len(user_roles) <= 1:
                await ctx.send(f"{str(user)} doesn't have any roles!")
                return
            for role in user_roles:
                if str(role) != "@everyone":
                    if(str(role) in roles):
                        await ctx.send(f"Removed the following roles from {str(user)}:")
                        await ctx.send(f"\t{role}")
                        await user.remove_roles(role)
                        logging.info(f"Removed{role} from {str(user)}")
        else:
            await ctx.send("You must be a moderator to run this command!")

    @commands.command(hidden=True, name="giverole", aliases=['addrole'], help="Adds a new role to a user", short="Add role to user")
    async def giverole(self, ctx, user: discord.User, *roles):
        mod_role = ctx.author.guild_permissions.administrator
        if mod_role:
            if len(roles) == 0:
                await ctx.send(f"You have called $addrole but didn't pass what roles to add!")
                return
            if len(str(user)) == 0:
                await ctx.send(f"You have called $addrole but didn't pass what user to add roles to!")
                return
            for role in roles:
                role_object = get(user.guild.roles, name=role)
                if str(role) != "@everyone":
                    await ctx.send(f"Gave {role} to {user}")
                    await user.add_roles(role_object)
                    logging.info(f"Added {role} to {str(user)}")
                else:
                    await ctx.send(f"{str(user)} already has the {role} role!")
                    logging.info(f"{str(user)} already has the {role} role!")
        else:
            await ctx.send("You must be a moderator to run this command!")

    @commands.command(hidden=True, help="List all roles in the server", short="List roles")
    async def getroles(self, ctx):
        for role in ctx.guild.roles:
            if str(role) != "@everyone":
                await ctx.send(f"Role: {str(role)}")
    
    #Errors
    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Improper usage of $removerole.\nThe proper usage of this command is as follows:\n$removerole <user> <role>\nMultiple roles may be passed and are separated by a space.")
            logging.error(
                f"Improper usage of $removerole. found by user {ctx.author}")
    @giverole.error
    async def giverole_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Improper usage of $giverole.\nThe proper usage of this command is as follows:\n$giverole <user> <role>\nMultiple roles may be passed and are separated by a space.")
            logging.error(
                f"Improper usage of $giverole found by user {ctx.author}")

def setup(client):
    client.add_cog(roles(client))
