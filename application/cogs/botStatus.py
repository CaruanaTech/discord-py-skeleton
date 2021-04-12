from discord.ext import commands
from colorama import Fore as color
import logging


class botStatus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.warning(color.GREEN + "Bot is online" + color.RESET)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(botStatus(bot))
