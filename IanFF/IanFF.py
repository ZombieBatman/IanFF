import discord
from discord.ext import commands

class IanFF: 
	"""My custom cog that does stuff!"""

	def __init__(self, bot):
		self.bot = bot
		self.target = Nun

	@commands.command()
	async def IanFF(self):
		"""This does stuff!"""

		#Your code will go here
		await self.bot.say("MY FINAL FORM IS UNLEASHING @ian#9201")
	
	@commands.command()	
	async def SetTarget(self, var1):
			"""This Does Things!"""
		self.target = var1
			#BotTalking
			await self.bot.say("Target has been send" + self.target)

def setup(bot):
	bot.add_cog(IanFF(bot))