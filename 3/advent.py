def process(filename):
	f = open(filename)

	rucksacks = []
	for line in f:
		line = line.strip()
		L = int(len(line)/2)
		compartment1 = line[:L]
		compartment2 = line[L:]
		rucksacks.append((compartment1, compartment2))
	return rucksacks

def process_part_2(filename):
	f = open(filename)

	rucksacks = []
	current_group = []
	for line in f:
		if not len(current_group) == 3:
			current_group.append(set(line.strip()))
		else:
			rucksacks.append(current_group)
			current_group = [set(line.strip())]

	rucksacks.append(current_group)
	return rucksacks

def find_common_items(rucksacks):
	items = []

	for r in rucksacks:
		r1 = set(r[0])
		r2 = set(r[1])

		items.append((r1 & r2).pop())
	
	return items

def find_id_item(groups):
	items = []
	
	for g in groups:
		item = (g[0] & g[1] & g[2]).pop()
		items.append(item)

	return items


def calculate_priority_sum(items):
	P = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	total = 0

	for item in items:
		total += P.index(item) + 1
	return total


if __name__ == "__main__":
	# Part 1
	rucksacks = process("test.txt")
	items = find_common_items(rucksacks)
	calculate_priority_sum(items)


	# Part 2
	rucksacks = process_part_2("input.txt")
	items = find_id_item(rucksacks)
	print(calculate_priority_sum(items))



