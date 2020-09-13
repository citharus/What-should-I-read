from random import randint
from json import load


class RandomBook:
	def __init__(self, book_list: str):
		self.book_list: str = book_list

	def random(self):
		number = randint(0, len(self.book_list))

		with open(self.book_list) as bl:
			book_list: dict = load(bl)
			book: dict = book_list[str(number)]
			return book
