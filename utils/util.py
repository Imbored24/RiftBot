import asyncio

import nextcord
from nextcord.ext.menus import Paginator

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except nextcord.HTTPException:
            pass



async def GetMessage(bot, ctx, contentOne="Default Message", contentTwo="\uFEFF", timeout=100):
    embed = nextcord.Embed(title=f"{contentOne}", description=f"{contentTwo}",)
    sent = await ctx.send(embed = embed)
    try:
        msg = await bot.wait_for("message", timeout=timeout, check=lambda message: message.author == ctx.author and message.channel == ctx.channel,)
        if msg:
            return msg.content
    except asyncio.TimeoutError:
        return False

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content