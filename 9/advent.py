from copy import copy
class Grid:
	def __init__(self):
		self.head = Head()
		self.tail = Tail(self.head)
		self.head.set_tail(self.tail)
		self.head.grid = self
		self.tail.grid = self

	def __repr__(self):
		max_x = max([abs(self.head.x), abs(self.tail.x)])
		max_y = max([abs(self.tail.y), abs(self.tail.y)])
		row = ['.' for n in range(max_x+3)]
		empty = [copy(row) for n in range(max_y+3)]
		empty[-1][0] = 's'

		empty[(-self.head.y)-1][self.head.x] = 'H'
		empty[(-self.tail.y)-1][self.tail.x] = 'T'

		out = ""
		for row in empty:
			out += "".join([str(x) for x in row])
			out += '\n'
		return out


class Knot:
	def __init__(self, x=0, y=0):
		self.x = 0
		self.y = 0

	def __repr__(self):
		return f"({self.x, self.y})"


class Tail(Knot):
	def __init__(self, head):
		super().__init__()
		self.head = head
		self.visited = set()
		self.visited.add((0,0))

	def handle_move(self):
		print('need to move tail now')
		if self.y == self.head.y:
			if self.head.x > self.x:
				self.x += 1
			else:
				self.x -= 1
		elif self.x == self.head.x:
			if self.head.y > self.y:
				self.y += 1
			else:
				self.y -= 1
		else:
			if self.head.x > self.x:
				self.x += 1
			else:
				self.x -= 1

			if self.head.y > self.y:
				self.y += 1
			else:
				self.y -= 1

		self.visited.add((self.x, self.y))

	def react(self):
		print(f'reacting to new head position {self.head.x}, {self.head.y}')

		# if same, do nothing
		if self.x == self.head.x and self.y == self.head.y:
			return
		# if in same col and only one row away do nothing
		elif self.x == self.head.x and (abs(self.y - self.head.y) == 1):
			return


		# if in same row and only one away do nothing
		elif self.y == self.head.y and (abs(self.x - self.head.x) == 1):
			return


		elif abs(self.x - self.head.x) == 1 and abs(self.y - self.head.y) == 1:
			return

		else:
			self.handle_move()



class Head(Knot):
	def __init(self, tail=None):
		super().__init__()
		self.tail = tail

	def set_tail(self, tail):
		self.tail = tail

	def move_once(self, direction):
		if direction == "R":
			self.x += 1
		if direction == "L":
			self.x -= 1
		if direction == "U":
			self.y += 1
		if direction == "D":
			self.y -= 1

		self.tail.react()
		# print(self.grid)

	def process(self, line):
		print('LINE', line)
		direction, num = line.strip().split()
		num = int(num)

		for i in range(num):
			self.move_once(direction)
			print(f"head {self} tail {self.tail}")


		# import pdb; pdb.set_trace()


if __name__ == "__main__":
	g = Grid()

	f = open("input.txt")
	for line in f:
		g.head.process(line)

	print(len(g.tail.visited))


