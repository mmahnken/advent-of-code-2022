def process(filename):

	f = open(filename)
	letters = f.read().strip()

	return letters

def get_start_of_packet_marker(letters):

	current_set = []
	for i, letter in enumerate(letters):
		if len(current_set) == 14:
			if len(set(current_set)) == len(current_set):
				return i
			else:
				current_set.append(letter)
				current_set[0:1] = []


		if len(current_set) != 14:
			current_set.append(letter)




if __name__ == "__main__":
	l = process("input.txt")
	print(get_start_of_packet_marker(l))