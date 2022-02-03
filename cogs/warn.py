import nextcord
from nextcord.ext import commands

from utils.util import Pag

class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: nextcord.Member=None, *, reason=None):
        if reason == None or member == None:
            await ctx.send("Please put a reason or mention a member! e.g !warn @member reason")
        
        if member.id in [ctx.author.id, self.bot.user.id]:
            return await ctx.send("You cannot warn yourself or the bot!")

        current_warn_count = len(
            await self.bot.warns.find_many_by_custom(
                {
                    "user_id": member.id,
                    "guild_id": member.guild.id
                }
            )
        ) + 1

        warn_filter = {"user_id": member.id, "guild_id": member.guild.id, "number": current_warn_count}
        warn_data = {"reason": reason, "timestamp": ctx.message.created_at, "warned_by": ctx.author.id}

        await self.bot.warns.upsert.custom(warn_filter, warn_data)

        embed = nextcord.Embed(tile="You are being warned:", description=f"__**Reason**__:\n{reason}",colour=nextcord.Colour.red(), timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Warn: {current_warn_count}")
        try:
            await member.send(embed=embed)
            await ctx.send("Warned that user in dm's for you.")
        except nextcord.HTTPException:
            await ctx.send(member.mention, embed = embed)

def setup(bot):
    bot.add_cog(warn(bot))