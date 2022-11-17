import disnake
from disnake.ext import commands
from disnake.ext.commands.context import Context

class XCog(commands.Cog):
    def __init__(self, bot: disnake.Client) -> None:
        self.bot = bot

def setup(bot):
    bot.add_cog(XCog(bot))
