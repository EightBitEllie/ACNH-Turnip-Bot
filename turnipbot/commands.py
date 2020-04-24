from discord.ext.commands import Bot, Cog, command, Context

class Commands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command()
    async def turnipprice(self, ctx: Context, price: int) -> None:
        pass


def setup(bot: Bot) -> None:
    bot.add_cog(Commands(bot))
