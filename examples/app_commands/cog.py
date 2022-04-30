import discord
from discord import app_commands
from discord.ext import commands

MY_GUILD = discord.Object(id=0)  # replace with your guild id


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        pass

    async def cog_unload(self):
        pass


async def setup(bot):
    await bot.add_cog(MyCog(bot))
