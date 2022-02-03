import nextcord
from nextcord.ext import commands
import config
# This is a test cog so i can test functionality for things before adding it to the main stream bot.
class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        if ctx.message.author.id == config.OWNER_ID or ctx.message.author.id == config.MANAGER_ID:
            await ctx.send("test")
        else:
            await ctx.send(f'Sorry this command is under testing. So only people with the ids: `{config.OWNER_ID}`, `{config.MANAGER_ID}` can run this command!')

def setup(bot):
    bot.add_cog(test(bot))