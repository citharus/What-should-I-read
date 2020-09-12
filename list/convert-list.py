from collections import defaultdict
from json import dump

READ_LIST = 'list/<list.txt>'
WRITE_LIST = 'list/<list.json>'
DATA = defaultdict(list)

with open(READ_LIST, 'r') as read_list:
	books: list = read_list.readlines()

for i in range(len(books)):
	info = books[i].split(';')
	new_book = {
		"name": info[0],
		"author": info[1],
		"year": info[2],
		"link": info[3].strip('\n')
	}
	DATA[i].append(new_book)

with open(WRITE_LIST, 'w') as write_list:
	dump(DATA, write_list, indent=4)
