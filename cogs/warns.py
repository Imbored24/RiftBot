import nextcord
from nextcord.ext import commands
from utils.util import Pag

class warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="warns", aliases=["checkwarns"], description="Checks to see how many warns a member has.", usage="[warns]")
    async def warns(self, ctx, member: nextcord.Member = None):
        if member == None:
            await ctx.send("[prefix]warns @member")
        else:
            warn_filter = {"user_id": member.id, "guild_id": member.guild.id}
            warns = await self.bot.warns.find_many_by_custom(warn_filter)
        
            if not bool(warns):
                return await ctx.send(f"Couldn't find any warns for: `{member.display_name}`")
        
            warns = sorted(warns, key=lambda x: x["number"])
        
            pages = []
            for warn in warns:
                description = f"""
                Warn Number: `{warn['number']}`
                Warn Reason: `{warn['reason']}`
                Warned By: <@{warn['warned_by']}>
                Warn Date: {warn['timestamp'].strftime("%I:%M %p %B %d, %Y")}
                """
                pages.append(description)
        
            await Pag(
                title=f"Warns for `{member.display_name}`",
                colour=0xCE2029,
                entries=pages,
                length=1
            ).start(ctx)

def setup(bot):
    bot.add_cog(warns(bot))