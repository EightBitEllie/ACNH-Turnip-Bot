
import peewee
import peeweedbevolve # pylint: disable=unused-import

from discord.ext.commands import Bot, Cog
from playhouse import db_url
from shared import configuration

POOL = db_url.connect(configuration.get('db'))

class BaseModel(peewee.Model):
    class Meta:
        database = POOL



POOL.evolve(interactive=False, ignore_tables=['basemodel'])

class Database(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.pool = POOL
        if bot is not None:
            bot.pool = self.pool

def setup(bot: Bot) -> None:
    bot.add_cog(Database(bot))
