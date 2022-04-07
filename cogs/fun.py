from ast import Await
from datetime import time
from distutils.log import error
from typing_extensions import Self
import discord
import asyncio
import os
import random
import datetime
from discord.ext import commands
from core.core import Cog_Extension

class fun(Cog_Extension):
 @commands.Cog.listener()
 async def on_ready(self):
       print ('fun load successfully.')

 @commands.command(pass_context = True)
 async def exam(self, ctx, user :discord.Member):
     embed= discord.Embed (title = f'the mark {user} will get in the next exam', description = (random.randint(1,100)))
     await ctx.send (embed=embed)
     #1

 


def setup(bot):
  bot.add_cog(fun(bot))