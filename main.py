import disnake
from disnake.embeds import Embed
from disnake.ext import commands
import os
from disnake.ext.commands.core import command
import jishaku
from filemanage import *

def get_prefix(bot: commands.Bot, message):
    async def get_prefix(bot, message):
        prefix_data = File(f"data/guild/{message.guild.id}/prefix.txt").read()

        if prefix_data is not None:
            return commands.when_mentioned_or(*[prefix_data.lower(), prefix_data.upper(), prefix_data.capitalize()])(bot, message)
        else:
            return commands.when_mentioned_or(*["nb.".lower(), "nb.".upper(), "nb.".capitalize()])(bot, message)
    
    return bot.loop.create_task(get_prefix(bot,message))

bot = commands.Bot(get_prefix, intents=disnake.Intents.all(), help_command=None)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла ошибка!", description=f"```У меня нет такой команды!```"))
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла ошибка!", description=f"```Подожди немного! Задержка команды ещё не кончилась.```"))
    elif isinstance(error, commands.UserNotFound):
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла ошибка!", description=f"```Я не нашёл этого пользователя!```"))
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла ошибка!", description=f"```Я не нашёл этого участника!```"))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла ошибка!", description=f"```Ты забыл указать {error.param.name}!```"))
    elif isinstance(error, commands.BadArgument):
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла ошибка!", description=f"```Мне кажется или ты ввёл что-то не то?```"))
    else:
        await ctx.send(embed=Embed(color=0xff0000, title="Произошла неизвестная ошибка!", description=f"Ошибка в команде `{ctx.command}`: ```{error}```"))

@bot.command()
async def reload(ctx, cog):
    if str(ctx.author.id) not in bot.ownids:
        return
    bot.reload_extension(f"cogs.{cog}")

@bot.command()
async def load(ctx, cog):
    if str(ctx.author.id) not in bot.ownids:
        return
    bot.load_extension(f"cogs.{cog}")

@bot.command()
async def unload(ctx, cog):
    if str(ctx.author.id) not in bot.ownids:
        return
    bot.unload_extension(f"cogs.{cog}")

cogs = [
    "cogs.basic",
    "cogs.junk",
    "cogs.debug"
]

if __name__ == "__main__":
    for cog in cogs:
        bot.load_extension(cog)
    #bot.load_extension('jishaku')
    jishaku.Flags.NO_UNDERSCORE = True
    jishaku.Flags.FORCE_PAGINATOR = True
    jishaku.Flags.NO_DM_TRACEBACK = True

bot.run("")
