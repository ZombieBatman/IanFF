import discord
from discord.ext import commands

class IanFF: 
	"""My custom cog that does stuff!"""

	def __init__(self, bot):
		self.bot = bot
		self.target = None

	@commands.command()
	async def ianff(self):
		"""This does stuff!"""

		#Your code will go here
		await self.bot.say("MY FINAL FORM IS UNLEASHING")
	
	@commands.command()	
	async def settarget(self, var1: discord.Member = None):
		"""This Does Things!"""
		self.target = var1
		#BotTalking
		await self.bot.say("Target has been sent to "  +  self.target)

def setup(bot):
	bot.add_cog(IanFF(bot))