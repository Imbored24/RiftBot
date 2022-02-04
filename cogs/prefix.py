from ast import alias
import nextcord
from nextcord.ext import commands

class prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prefix", aliases=["changeprefix", "setprefix"], description="Change your guilds prefix!", usage="[prefix]")
    @commands.has_guild_permissions(manage_guild=True)
    async def prefix(self, ctx, *, prefix=None):
        if prefix == None:
            await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": "!"})
            await ctx.send("Because you did not set a prefix when running this command. The prefix has been changed back to the default prefix `!`.")
        else:
            await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": prefix})
            await ctx.send(f"The guild prefix has been set to `{prefix}`. Use `{prefix}prefix [prefix]` to change it again!")

def setup(bot):
    bot.add_cog(prefix(bot))