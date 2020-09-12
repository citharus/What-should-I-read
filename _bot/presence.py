from discord.ext import commands, tasks
from pypresence import Presence
from random import choice


def read_token():
	with open('../TOKEN.txt', 'r') as token:
		return token.readlines()[1].strip()


class RichPresence(commands.Cog):
	RPC = Presence(read_token())
	RPC.connect()

	def presence(self, RPC=RPC):
		presence_text = [
			'Made by me c:',
			'Made by citharus',
			'Runing low on books :c',
			'`&help` for help ;)',
			'Gotta keep you reading.',
			'Made by citharus#6618'
		]

		RPC.update(state=choice(presence_text), large_image='book', large_text='Made by me.')

	@tasks.loop(minutes=1)
	async def update(self):
		self.presence()
