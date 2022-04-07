import asyncio
from curses.panel import bottom_panel
import discord
import datetime
import aiohttp
import random
import os
from discord.ext import commands

  

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle , activity=discord.Activity(type=discord.ActivityType.listening, name="white cup's code"))   
  print ("yayyyyy it works")


@bot.command()
async def afk(ctx, mins):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} has gone afk for {mins} minutes.")
    await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(10)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break
            

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send ('ok u broke the cmd, happy now? try doing it with a argument you failure')

@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send ('u r not a admin. cant u check ur role before using the cmd?')


@bot.command()
async def load(ctx, extension):

    bot.load_extension(F'cogs.{extension}')
    await ctx.send(F'i have loaded {extension}. Use unload to disable it.')

@bot.command()
async def unload(ctx, extension):

    bot.unload_extension(F'cogs.{extension}')
    await ctx.send(f'i have unload {extension}. Use load to enable it.')
    
@bot.listen()
async def on_message(message):
    if message.content.startswith('help'):
       await message.channel.send ('<@876303280198795274> help')
  

@bot.listen() 
async def on_message_delete(ctx):
    await ctx.send ('why did you delete that')







@bot.command()
async def reload(ctx, extension):

        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(F'I have reloaded {extension}.')
    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(F'cogs.{filename[:-3]}')     
if __name__ == "__main__": 

 bot.run('Your token here ') 

bot.run('Your token here') 
 
