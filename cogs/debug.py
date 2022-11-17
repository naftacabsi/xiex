from os import environ, system

import jishaku
from discord.ext import commands
from jishaku.cog import Jishaku
import logging


logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class DevModule(Jishaku):
    pass


def setup(bot: commands.Bot):
    jishaku.Flags.NO_UNDERSCORE = True
    jishaku.Flags.FORCE_PAGINATOR = True
    jishaku.Flags.NO_DM_TRACEBACK = True
    environ['JISHAKU_EMBEDDED_JSK'] = 'true'
    bot.add_cog(DevModule(bot=bot))
