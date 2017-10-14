import discord
from discord.ext import commands

class Girlsrgross: 
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def girlsrgross(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("MY FINAL FORM IS UNLEASHING")

def setup(bot):
    bot.add_cog(Girlsrgross(bot))