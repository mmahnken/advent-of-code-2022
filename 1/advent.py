def process(filename):
	f = open(filename)

	all_elves = []
	current = []
	for line in f:
		if line == '\n':
			all_elves.append(current)
			current = []
		else:
			current.append(int(line))

	all_elves.append(current)
		
	return all_elves


def find_greatest_elf(all_elves):
	all_sums = [sum(l) for l in all_elves]
	return max(all_sums)


def find_sum_of_top_3(all_elves):
	import pdb; pdb.set_trace()
	all_sums = [sum(l) for l in all_elves]
	sums_sorted = sorted(all_sums)
	return sum(sums_sorted[-3:])


if __name__ == "__main__":
	data = process("input.txt")
	# print(find_greatest_elf(data))
	print(find_sum_of_top_3(data))