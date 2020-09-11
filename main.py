from random import randint
from json import load


class RandomBook:
	def __init__(self, book_list: str, number: int = None):
		self.book_list: str = book_list
		self.number: int = number

	def random(self):
		if not self.number:
			self.number = randint(0, 100)

		with open(self.book_list) as bl:
			book_list: dict = load(bl)
			book: dict = book_list[str(self.number)]
			return book
