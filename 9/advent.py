from copy import copy
class Grid:
	def __init__(self, length=10):
		
		self.head = Node(0)
		self.nodes = [self.head]
		previous = self.head
		for i in range(length-1):
			node = Node(parent=previous, data=i+1)
			previous.child = node
			previous = node
			self.nodes.append(node)
		self.tail = self.nodes[-1]

	def process(self, line):
		print('LINE', line)
		direction, num = line.strip().split()
		num = int(num)

		for i in range(num):
			self.head.move_once(direction)
		
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


class Node:
	def __init__(self, data, parent=None, child=None, x=0, y=0):
		self.x = x
		self.y = y
		self.parent = parent
		self.child = child
		self.data = data
		self.visited = set()
		self.visited.add((0,0))


	def __repr__(self):
		return f"({self.x, self.y})"
		
	def handle_move(self):
		print('moving', self.data)
		if self.y == self.parent.y:
			if self.parent.x > self.x:
				self.x += 1
			else:
				self.x -= 1
		elif self.x == self.parent.x:
			if self.parent.y > self.y:
				self.y += 1
			else:
				self.y -= 1
		else:
			if self.parent.x > self.x:
				self.x += 1
			else:
				self.x -= 1

			if self.parent.y > self.y:
				self.y += 1
			else:
				self.y -= 1

		self.visited.add((self.x, self.y))

		if self.child:
			self.child.react()


	def react(self):
		print("child", self.data, "reaction")
		# if same, do nothing
		if self.x == self.parent.x and self.y == self.parent.y:
			return
		# if in same col and only one row away do nothing
		elif self.x == self.parent.x and (abs(self.y - self.parent.y) == 1):
			return
		# if in same row and only one away do nothing
		elif self.y == self.parent.y and (abs(self.x - self.parent.x) == 1):
			return
		elif abs(self.x - self.parent.x) == 1 and abs(self.y - self.parent.y) == 1:
			return
		else:
			self.handle_move()

	def move_once(self, direction):
		if direction == "R":
			self.x += 1
		if direction == "L":
			self.x -= 1
		if direction == "U":
			self.y += 1
		if direction == "D":
			self.y -= 1
		if self.child:
			self.child.react()


if __name__ == "__main__":
	g = Grid()

	f = open("input.txt")
	for line in f:
		g.process(line)

	print(len(g.tail.visited))


