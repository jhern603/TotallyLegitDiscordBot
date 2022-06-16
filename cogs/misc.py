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

  @commands.command()
  async def coffee(self, ctx):
    await ctx.send(f"Here's a cup of {self.listylist[random.randint(0,3)]} ☕")
    
  
  @commands.command()
  async def curseatme(self,ctx):
    await ctx.send(f"{data[random.randint(0,len(data))]}")


def setup(client):
  client.add_cog(misc(client))
