from ast import Await
import discord
import os
import random
from discord.ext import commands
from core.core import Cog_Extension


class basic(Cog_Extension):


 @commands.Cog.listener()
 async def on_ready(self):
  print ('basic loaded sucessfully')

  
 @commands.command()
 async def ping_alien(self, ctx,num2:int):
  for x in range(num2):
           await ctx.send('<@876303280198795274>')
    
 @commands.command()
 async def ping_gavin(self, ctx,num2:int):
  for x in range(num2):
           await ctx.send('<@716246469069504593>')
    
 @commands.command()
 async def ping_marcuz(self, ctx,num3:int):
  for x in range(num3):
           await ctx.send('<@905704151269380158>')
    
 @commands.command()
 async def hi(self, ctx): 
    embed=discord.Embed(title="hi", url="discord.com", description="go into the link", color=0xFF5733)
    await ctx.send(embed=embed)

  
 @commands.command()
 async def facts(self, ctx):
  responses = ['```there is a math alien in 1d class who want to do sk class scenario```',
               '```The majority of your brain is fat.```',
               '```"OMG" usage can be traced back to 1917.```',
               '```in Africa, 60 seconds is 1 minute```',
               '```every minute there is a child in africa died of hunger```',
               '```people wont get satisfied of anything, especially asian parents```',
               '👍',
               '```summer holiday? more like summer suffering```',
               '```white cup is really a white cup```',
               '```dnd is better for <@948008013556490341>```',
               '```it is really rare to get 👍 from this command```',
               '```No number from 1 to 999 includes the letter "a" in its word form.```',
               '```there is a adventage of getting covid and die. It is that you dont have to do hw anymore.```',
               '```there is a chance that you might be working until the last moment of your life.```',
               '```Every continent except Antarctica has at least one McDonalds.```',
               '```Baked beans are not baked.```',
               '```maths aliens are evil. they often say they are stupid but they are not.```',
               '```gavin is very smart```',
               '```intergrated science class is hell.```',
               '```Rubber bands last longer when refrigerated.```',
               '```white cup loves subway bread with steak and cheese.```',
               '```a math alien likes intergrated science```',
               '```marcuz likes ukrine very much. In fact, most of the people like ukrine more than russia```',
               '```https://www.youtube.com/watch?v=I9_wK6yLLjE&ab_channel=Superior```']

  await ctx.send (f'{random.choice(responses)}') 




 @commands.command()
 async def map(self, ctx):
   await ctx.send ('https://webstatic-sea.hoyolab.com/ys/app/interactive-map/index.html?bbs_presentation_style=no_header&lang=en-us#/map/2?shown_types=2,3,154,158,190,316,319,338,340&center=828.29,272.62&zoom=-1.50')
 
 @commands.command()
 async def ping(self, ctx):
    await ctx.send (f'the ping of the bot is`{(self.bot.latency*1000)}`ms')


def setup(bot):
  bot.add_cog(basic(bot))
