import nextcord
from nextcord.ext import commands

class deletewarn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="deletewarn", aliases=["delwarn", "dw"], description="Deletes a warn of a member.")
    @commands.has_permissions(kick_members=True)
    async def deletewarn(self, ctx, member : nextcord.Member, warn : int = None):
        filter_dict = {"user_id": member.id, "guild_id": member.guild.id}
        if warn:
            filter_dict["number"] = warn

        was_deleted = await self.bot.warns.delete_by_custom(filter_dict)
        if was_deleted and was_deleted.acknowledged:
            if warn:
                return await ctx.send(
                    f"I deleted warn number `{warn}` for `{member.display_name}`"
                )

            return await ctx.send(
                f"I deleted `{was_deleted.deleted_count}` warns for `{member.display_name}`"
            )

        await ctx.send(
            f"I could not find any warns for `{member.display_name}` to delete matching your input"
        )

def setup(bot):
    bot.add_cog(deletewarn(bot))