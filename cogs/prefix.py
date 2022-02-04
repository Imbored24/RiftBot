import nextcord
from nextcord.ext import commands

class prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
def setup(bot):
    bot.add_cog(prefix(bot))