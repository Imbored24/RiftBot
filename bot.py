import nextcord
from nextcord.ext import commands
import config
import os
import motor.motor_asyncio
from utils.mongo import Document
bot = commands.Bot(command_prefix=config.PREFIX)

@bot.event
async def on_ready():
    print(f"Bot is online! \nId: {config.BOT_ID}\nUsername: {config.BOT_NAME}")
    await bot.change_presence(
        activity=nextcord.Game(name=f"Hi, my names {bot.user.name}.Use {config.PREFIX} to interact with me!")
    )
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(config.MONGODB))
    bot.db = bot.mongo["myFirstDatabase"]
    bot.config = Document(bot.db, "configs")
    print("Database has been loaded!")
    for document in await bot.config.get_all():
        print(document)

@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id == config.OWNER_ID or config.MANAGER_ID:
        bot.load_extension(f'cogs.{extension}')    
        await ctx.send(f'I have loaded the cog `{extension}`!')
        print(f'Cog loaded with in discord\n{extension}')
    else:
        await ctx.send(f'Only users with the ids: `{config.OWNER_ID}`, `{config.MANAGER_ID}`. Can run this command!')


@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id == config.OWNER_ID or config.MANAGER_ID:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"I have unloaded the cog `{extension}`!")
        print(f'Cog unloaded with in discord\n{extension}')
    else:
        await ctx.send(f'Only users with the ids: `{config.OWNER_ID}, `{config.MANAGER_ID}`. Can use this command!')

@bot.command()
async def reload(ctx, extension):
    if ctx.message.author.id == config.OWNER_ID or config.MANAGER_ID:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f"I have reloaded the cog `{extension}`!")
        print(f'Cog reload with in discord\n{extension}')
    else:
        await ctx.send(f'Only users with the ids: `{config.OWNER_ID}`, {config.MANAGER_ID}. Can use this command!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded cog:\n{filename[:-3]}")
    else:
        print(f"Error loading cog:\n{filename[:-3]}")
bot.run(config.TOKEN)