#docs: https://discordpy.readthedocs.io/en/stable
import configparser
import discord
import os
import logging
from discord.ext import commands

logging.basicConfig(level=logging.INFO)
config = configparser.ConfigParser()
config.read('.conf')


activity = discord.Activity(
    type=discord.ActivityType.listening, name="your commands")
client = commands.Bot(command_prefix='$', activity=activity,
                      description="This is the unofficial official bot for the Oracle interns server!")

class OraBot(discord.Client):
    logging.info("Starting...")
    def __init__(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.load_extension(f'cogs.{file[:-3]}')
                logging.info(f'Loaded cog: {file[:-3]}')
        client.run(config['MYBOT']['TOKEN'])

    @client.command()
    async def load(self, ctx, extension):
        client.load_extension(f'cogs.{extension}')

    @client.command()
    async def unload(self, ctx, extension):
        client.unload_extension(f'cogs.{extension}')

    @client.command()
    async def reload(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.reload_extension(f'cogs.{file[:-3]}')
                logging.info(f'Reloaded cog: {file[:-3]}')
        channel = client.get_channel(873247206617006160)
        await channel.send("Cogs reloaded!")

    @client.event
    async def on_ready():
        logging.info(f'\nConnected to bot: {client.user.name}')
        logging.info(f'Bot ID: {client.user.id}')
        for guild in client.guilds:
            logging.info(f'Connected to guild: {guild.name}')
        logging.info('Orabot connected!')

    # @client.event
    # async def on_message(message):
    #     if message.channel.name == 'jose-channel':
    #         await client.process_commands(message)


if __name__ == '__main__':
    instance = OraBot()
