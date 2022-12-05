
def decode(letter):
	codes = {
			 'A': 'rock',
	         'X': 'rock',
	         'B': 'paper', 
	         'Y': 'paper', 
	         'C': 'scissors',
	         'Z': 'scissors'
	}

	return codes[letter]

def get_winner(elf, me):
	if elf == me:
		return 'draw'
	elif elf == 'rock':
		if me == 'paper':
			return 'me'
		if me == 'scissors':
			return 'elf'

	elif elf == 'paper':
		if me == 'rock':
			return 'elf'
		if me == 'scissors':
			return 'me'

	elif elf == 'scissors':
		if me == 'rock':
			return 'me'
		if me == 'paper':
			return 'elf'

def score(result, move):
	result_points = {'W': 6, 'D': 3, 'L': 0}
	move_points = {'rock': 1, 'paper': 2, 'scissors': 3}
	return result_points[result] + move_points[move]

def decode_desired_result(elf, result):

	if result == 'W':
		if elf == 'rock':
			return 'paper'
		elif elf == 'paper':
			return 'scissors'
		elif elf == 'scissors':
			return 'rock'
	elif result == 'D':
		return elf
	elif result == 'L':
		if elf == 'rock':
			return 'scissors'
		elif elf == 'paper':
			return 'rock'
		elif elf == 'scissors':
			return 'paper'

def process(filename):

	total_elf = 0
	total_me = 0

	results = {'X':'L', 'Y':'D', 'Z': 'W'}

	for line in open(filename):
		elf, me = line.strip().split()
		elf = decode(elf)
		
		# Part 1
		# me = decode(me)


		# Part 2
		result = results[me]
		me = decode_desired_result(elf, result)
		
		winner = get_winner(elf, me)


		if winner == 'draw':
			my_score = score('D', me)
			elf_score = score('D', elf)
		elif winner == 'me':
			my_score = score('W', me)
			elf_score = score('L', elf)
		else:
			my_score = score('L', me)
			elf_score = score('W', elf)
		print('my score', my_score)
		total_elf += elf_score
		total_me += my_score

	print(total_me)



if __name__ == "__main__":
	# test should be 15

	process('input.txt')
