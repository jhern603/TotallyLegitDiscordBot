# docs: https://discordpy.readthedocs.io/en/stable/
import configparser
import discord
import os
import logging
from discord.ext import commands

#Load configurations
logging.basicConfig(level=logging.INFO)
config = configparser.ConfigParser()
config.read('.conf')

#Bot settings
prefix = "$"
activity = discord.Game("Life")
bot_log_channel_ID = 873247206617006160

#Initialize bot
client = commands.Bot(command_prefix=prefix, 
                      activity=activity,
                      description="This is the unofficial official bot for the Oracle interns server!", 
                      help_command=None)
client.remove_command('help')

class OraBot(discord.Client):
    channel = client.get_channel(bot_log_channel_ID)
    logging.info("Starting...")

    def __init__(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.load_extension(f'cogs.{file[:-3]}')
                logging.info(f'Loaded cog: {file[:-3]}')
        client.run(config['ORABOT']['TOKEN'])

    @client.command(help="Load a new cog.", short="Load cog.")
    async def load(self, extension):
        client.load_extension(f'cogs.{extension}')

    @client.command(help="Unload a cog.", short="Unload cog.")
    async def unload(self, extension):
        client.unload_extension(f'cogs.{extension}')

    @client.command(help="Reload all cogs.", short="Reload cog.")
    async def reload(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.reload_extension(f'cogs.{file[:-3]}')
                logging.info(f'Reloaded cog: {file[:-3]}')
        await self.channel.send("Cogs reloaded!")

    @client.command(help="Lists all cogs.", short="List cogs.")
    async def listcogs(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.channel.send(f"cog: {file[:-3]}")

    @client.command()
    async def help(ctx, args=None):
        help_embed = discord.Embed(title="Help!")
        command_names_list = [x.name for x in client.commands]

        # If there are no arguments, just list the commands:
        if not args:
            help_embed.add_field(
                name="List of supported commands:",
                value="\n".join([str(i+1)+". "+x.name for i,
                                x in enumerate(client.commands)]),
                inline=False
            )
            help_embed.add_field(
                name="Details",
                value=f"Type `{prefix}help <command name>` for more details about each command.",
                inline=False
            )
        elif args in command_names_list:
            help_embed.add_field(
                name=args,
                value=client.get_command(args).help
            )
        else:
            help_embed.add_field(
                name="Nope.",
                value="Don't think I got that command, boss!"
            )
        await ctx.send(embed=help_embed)

    # Error Handling
    @load.error
    async def load_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Improper usage of $load.\nPlease use $listcogs first, then use $load as follows:\n\t$load <cog name>")
            logging.error(
                f"Improper usage of $load found by user {ctx.author}")

    @unload.error
    async def unload_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Improper usage of $unload.\nPlease use $listcogs first, then use $unload as follows:\n\t$unload <cog name>")
            logging.error(
                f"Improper usage of $unload found by user {ctx.author}")

    @client.event
    async def on_ready():
        logging.info(f'Connected to bot: {client.user.name}')
        logging.info(f'Bot ID: {client.user.id}')
        for guild in client.guilds:
            logging.info(f'Connected to guild: {guild.name}')
        logging.info('Orabot connected!')
        logging.info(
            f"Bot log hooked to {client.get_channel(bot_log_channel_ID)}")


if __name__ == '__main__':
    instance = OraBot()
