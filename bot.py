from discord.ext import commands, tasks
from discord import Embed, Colour, Game
from book import RandomBook
from pathlib import Path
from random import choice


def read_token():
	with open('TOKEN.txt', 'r') as token:
		return token.readlines()[0].strip()


TOKEN: str = read_token()
CLIENT = commands.Bot(command_prefix='&')
CLIENT.remove_command('help')

STATUS: list = [
	'Made by me.',
	'Made by citharus c:',
	'I like your taste. uwu',
	'Running low on books...',
	'Made by citharus#6618',
	'Gotta keep you reading.',
	'&help for help ;)',
	'Help: &help',
	'Can\'t find a book? &help!'
]


@CLIENT.event
async def on_ready():
	change_status.start()


@tasks.loop(minutes=1)
async def change_status():
	await CLIENT.change_presence(activity=Game(name=choice(STATUS)))


@CLIENT.command(name='help')
async def _help(ctx):
	embed = Embed(title="Help", colour=Colour(0xf3b816), description="Here is all you need to know for using this Bot.")

	embed.add_field(name="Commands", value="`&book <book list>` - Gives you a random book.\n`&help` \
					- Displays this help.")
	embed.add_field(name="Book lists", value="`times` - The Top-100-Book list from the Times Magazine.\n`gurdian` \
					- The Top-100-Book list from the Gurdian.")

	await ctx.send(content="You asked for help? Here you go. uwu", embed=embed)


@CLIENT.command(name='book')
async def _book(ctx, book_list: str):
	if not book_list:
		raise commands.errors.MissingRequiredArgument('Missing book list argument.')
	if not Path(f'list/{book_list}.json').exists():
		raise commands.errors.ArgumentParsingError('Missing book list location.')

	random_book = RandomBook(f'list/{book_list}.json').random()
	book_name = random_book[0]['name']
	book_author = random_book[0]['author']
	book_year = random_book[0]['year']
	book_link = random_book[0]['link']

	embed = Embed(title="A random book for you! uwu", colour=Colour(0xf3b816), url=f"{book_link}")
	embed.add_field(name=f"{book_name}", value=f"The book '[{book_name}]({book_link})' was written in {book_year} by\
					{book_author}")

	await ctx.send(content="Here you have it!", embed=embed)


@_book.error
async def missing_argument_error(ctx, error):
	if isinstance(error, commands.errors.MissingRequiredArgument):
		embed = Embed(title="Missing book list argument.", colour=Colour(0xf3b816))
		embed.add_field(name='Book list', value='You need to give me a book list.\n Try `&help` for more info.')
		await ctx.send(content='I didn\'t understand that. Please retry.', embed=embed)

	if isinstance(error, commands.errors.ArgumentParsingError):
		embed = Embed(title="Missing book list location.", colour=Colour(0xf3b816))
		embed.add_field(name='Book list', value='You need to give me a *proper* book list.\n\
						Try `&help` for more info.')
		await ctx.send(content='I didn\'t find the book list. Please retry.', embed=embed)


if __name__ == '__main__':
	CLIENT.run(TOKEN)
