from ast import Await
from datetime import time
from distutils.log import error
from typing_extensions import Self
import discord
import asyncio
import os
import datetime
from discord.ext import commands
from core.core import Cog_Extension


class mod(Cog_Extension):
 @commands.Cog.listener()
 async def on_ready(self):
       print ('mod load successfully.')

   

   
 @commands.command()
 async def clear(self, ctx, message_count: int, *, silent: str = "not silent"):
    silent = silent.lower() in ("silent", "true", "1", "yes", "y")
    await ctx.channel.purge(limit = message_count + 1)
    if not silent:
        await ctx.send(f"{message_count} {'message was' if message_count == 1  else 'messages were'} just cleared by {ctx.author.mention}.",
            allowed_mentions = discord.AllowedMentions(users = []), delete_after=5)

 @commands.command()
 async def say(self, ctx,*, args): 
      await ctx.message.delete()
      await ctx.send(args)


 @commands.command()
 @commands.has_permissions(manage_roles=True)
 async def mute(self, ctx, member: discord.Member, time : int, reason=None):
    role = discord.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"{member.mention} is muted for {time} {'second' if time == 1 else 'seconds'}, the reason is {reason}")
    await asyncio.sleep(time)
    await member.remove_roles(role)
    await ctx.send(f"hey {member.mention} you can talk again now :D")


 @commands.command()
 async def dm(self, ctx, user:discord.Member,*, content):
  await ctx.message.delete() 
  embed=discord.Embed(title=f"New message from {ctx.author}", description=f"{content}", color=0x00f5cc)
  await user.send(embed=embed)
  await ctx.send (f'Message sent to {user.mention}')

   
def setup(bot): 
  bot.add_cog(mod(bot))
