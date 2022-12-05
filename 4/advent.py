def process(filename):
	f = open(filename)

	pairs = []
	for line in f:
		a1, a2 = line.strip().split(',')

		i, j = a1.split('-')
		x, y = a2.split('-')

		pairs.append([(int(i), int(j)), (int(x), int(y))])
	return pairs


def find_containing_pairs(pairs):

	count = 0

	for p in pairs:

		p1, p2 = p

		x1, y1 = p1
		x2, y2 = p2

		# Part 1 - this block only
		if x1 >= x2 and y1 <= y2:
			count += 1
		elif x2 >= x1 and y2 <= y1:
			count += 1
		
		# Part 2 - additional acceptance criteria
		# left hanging off
		elif x2 <= y1 and x1 <= x2:
			count += 1

		elif x1 <= y2 and y1 > y2:
			count += 1

		

	print(count)


# x1       y1
#      x2        y2 




# 		   x1       y1
#      x2        y2        



if __name__ == "__main__":
	p = process("input.txt")
	find_containing_pairs(p)