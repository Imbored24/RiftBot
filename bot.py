import nextcord
from nextcord.ext import commands
import config
import os
bot = commands.Bot(command_prefix=config.PREFIX)

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.command()
async def load(ctx, extension):
    bot.load_extesnion(f'cogs.{extension}')    
    await ctx.send(f'I have loaded the cog `{extension}`!')
    print(f'Cog loaded with in discord\n{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded cog:\n{filename[:-3]}")
    else:
        print(f"Error loading cog:\n{filename[:-3]}")
bot.run(config.TOKEN)