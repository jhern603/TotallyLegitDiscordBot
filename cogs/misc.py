import discord
import json
import random
from discord.ext import commands

f = open('profanity.json')
data = json.load(f)

class misc(commands.Cog):
  listylist = ["cortadio", 4, "americano", "italiano"]
  
  def __init__(self, client):
    self.client = client  
  
  @commands.command(help="Hurl slurs at the user.", short="The antichrist.")
  async def curseatme(self,ctx):
    await ctx.send(f"{data[random.randint(0,len(data))]}")


def setup(client):
  client.add_cog(misc(client))
