def process(filename):
	f = open(filename)

	box_rows = []

	for line in f:
		if '[' in line:
			box_rows.append(line)
		else:
			indices = [int(n) for n in line.split()]
			break

	stacks = [ [] for i in indices]
	for row in box_rows[::-1]:
		letter_index = 1
		for i in indices:
			if row[letter_index] != ' ':
				stacks[i-1].append(row[letter_index])
			letter_index += 4

	print(stacks)

	directions = []
	for direction in f:
		if not direction.strip():
			continue
		print(direction)
		tokens = direction.split()
		directions.append({
			'quantity': int(tokens[1]),
			'from': int(tokens[3]),
			'to': int(tokens[5])
		})

	return stacks, directions


def execute_directions(stacks, directions):
	for d in directions:
		from_stack = stacks[d['from']-1]
		to_stack = stacks[d['to']-1]
		for rep in range(d['quantity']):
			item = from_stack.pop()
			to_stack.append(item)

	for s in stacks:
		print(s[-1], end="")
	print()

def execute_directions_part2(stacks, directions):
	for d in directions:
		print(d)
		from_stack = stacks[d['from']-1]
		to_stack = stacks[d['to']-1]
		
		N = d['quantity']
		to_move = from_stack[-(N):]
		from_stack[-(N):] = []
		
		to_stack.extend(to_move)

	for s in stacks:
		print(s[-1], end="")
	print()


if __name__ == "__main__":
	s, d = process("input.txt")
	# execute_directions(s, d)
	execute_directions_part2(s, d)
