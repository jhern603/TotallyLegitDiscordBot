# docs: https://discordpy.readthedocs.io/en/stable/
import configparser
import discord
import os
import logging
from discord.ext import commands

logging.basicConfig(level=logging.INFO)
config = configparser.ConfigParser()
config.read('.conf')


activity = discord.Game("Life")
client = commands.Bot(command_prefix='$', activity=activity,
                      description="This is the unofficial official bot for the Oracle interns server!")
bot_log_channel_ID = 873247206617006160

class OraBot(discord.Client):
    channel = client.get_channel(bot_log_channel_ID)
    logging.info("Starting...")
    
    def __init__(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.load_extension(f'cogs.{file[:-3]}')
                logging.info(f'Loaded cog: {file[:-3]}')
        client.run(config['ORABOT']['TOKEN'])

    @client.command()
    async def load(self, extension):
        client.load_extension(f'cogs.{extension}')

    @client.command()
    async def unload(self, extension):
        client.unload_extension(f'cogs.{extension}')

    @client.command()
    async def reload(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.reload_extension(f'cogs.{file[:-3]}')
                logging.info(f'Reloaded cog: {file[:-3]}')
        await self.channel.send("Cogs reloaded!")

    @client.command()
    async def listcogs(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.channel.send(f"cog: {file[:-3]}")

    @client.event
    async def on_ready():
        logging.info(f'Connected to bot: {client.user.name}')
        logging.info(f'Bot ID: {client.user.id}')
        for guild in client.guilds:
            logging.info(f'Connected to guild: {guild.name}')
        logging.info('Orabot connected!')
        logging.info(
            f"Bot log hooked to {client.get_channel(bot_log_channel_ID)}")

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


if __name__ == '__main__':
    instance = OraBot()
