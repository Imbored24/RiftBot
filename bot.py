import nextcord
from nextcord.ext import commands
import config
bot = commands.Bot(command_prefix=config.PREFIX)

@bot.event
async def on_ready():
    print("Bot is online!")

    

bot.run(config.TOKEN)