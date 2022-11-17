from filemanage import *
import disnake
from disnake.ext import commands
from random import choice, randint as ri
import asyncio
import base64

class Junk(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        if message.author.id == self.bot.user.id: return
        txt = ""
        random = ri(1, 3)
        words = File("junk/words.txt")
        text = words.read()
        wrds = text.split()
        if text != "":
            if message.content != "":
                for word in str(message.content).split():
                    if word not in text:
                        if not word.startswith(":") and not word.endswith(":") and not word.startswith("<") and not word.endswith(">") and not word.startswith("http") and not word.startswith("discord.g") and not word.startswith("@") and not word.startswith("#"):
                            words.write(f"{word.encode('utf-8', 'ignore').decode()} ")
        else:
            if message.content != "":
                for word in str(message.content).split():
                    words.write(f"{word} ")
        #if random == 2:
            #words = File("junk/words.txt").read().split()
            #for i in range(ri(1, 60)):
                #txt+=f"{choice(wrds)} "
            #await message.channel.send(txt)
    
    @commands.command(description="Генерация текста с помощью словаря")
    async def dtext(self, ctx, textrange:int=None):
        text = ""
        if textrange is None:
            words = File("junk/words.txt").read().split()
            for i in range(ri(1, 60)):
                text+=f"{choice(words)} "
            await ctx.send(text)
        else:
            words = File("junk/words.txt").read().split()
            for i in range(textrange):
                text+=f"{choice(words)} "
            await ctx.send(text)

    @commands.command(description="Количество слов в словаре")
    async def dwords(self, ctx):
        count = 0
        for i in File("junk/words.txt").read().split():
            count+=1
        await ctx.send(f"У меня {count} слов")

    @commands.command(description="Перемешать слова в тексте")
    async def distort(self, ctx, *, txt: str):
        text=""
        words=txt.split()
        for word in words:
            mw = len(words)
            rn = ri(0, mw-1)
            text+=f"{words[rn]} "
        await ctx.send(text)
    
    @commands.command(description="Перемешать буквы в тексте")
    async def distort2(self, ctx, *, txt: str):
        text=""
        for word in txt:
            mw = len(txt)
            rn = ri(0, mw-1)
            text+=f"{txt[rn]} "
        await ctx.send(embed=disnake.Embed(title="Текст", description=text))
    
    @commands.command(description="Прогрессбар")
    async def progress(self, ctx, sec: int, *, name: str,):
        progressbar = ["[", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "=", "]"]
        m = await ctx.send(f"{name}: "+"".join(progressbar))
        for i, c in enumerate(progressbar):
            if c != "[" and c != "]":
                progressbar[i] = "#"
                await m.edit(content=f"{name}: "+"".join(progressbar))
                await asyncio.sleep(sec)
    
    @commands.command(description="Это вам не надо")
    async def selfpurge(self, ctx, limit: int):
        if str(ctx.author.id) != self.bot.owner_id:
            return
        def is_me(m):
            return m.author == self.bot.user
        await ctx.channel.purge(limit=limit, check=is_me)

def setup(bot):
    bot.add_cog(Junk(bot))
