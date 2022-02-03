import nextcord
from nextcord.ext import commands
import config
# This is a test cog so i can test functionality for things before adding it to the main stream bot.
class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        if ctx.message.author.id == config.OWNER_ID or config.MANAGER_ID:
            await ctx.send("test")
        else:
            await ctx.send(f'Sorry this command is under testing. So only people with the ids: `{config.OWNER_ID}`, `{config.MANAGER_ID}` can run this command!')

    @commands.command()
    async def rules(self, ctx):
        if ctx.message.author.id == config.OWNER_ID or config.MANAGER_ID:
            embed = nextcord.Embed(title="Rules", description="These are the rules for the RiftBot support server.")
            embed.add_field(name="1. No swearing", value="This is a family freindly server and swearing will not be tolerated towards anyone.", inline=False)
            embed.add_field(name="2. No NSFW Content", value="NSFW Content is a definate no go. This seen anywhere will be an instant ban.", inline=False)
            embed.add_field(name="3. No Advertising", value="Advertising in the discord server will result in a mute.", inline=False)
            embed.add_field(name="4. No DM Advertising", value="Advertising in any members dms will result in an immediate kick.", inline=False)
            embed.add_field(name="5. No Spamming", value=f"Spamming in any sort will result in a mute. As we would like to keep our chats clean from random gibberish", inline=False)
            embed.add_field(name="6. Treat others how you want to be treated.", value=f"Don't treat other people bad. Treat them how you would want to be treated.", inline=False)
            embed.add_field(name="7. No CyberBullying", value="Cyberbullying is a serious thing and we will not tolorate it here. Any sign of this in a members dms or this server will result in an immediate ban", inline=False)
            embed.add_field(name="8. Follow Discord TOS", value="Follow the discord TOS. (our bible) https://discord.com/tos", inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(test(bot))