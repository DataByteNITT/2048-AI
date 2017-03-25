from random import randint
import math


# from eval import *


def new_game(n):
	matrix = []
	for i in range(n):
		matrix.append([0] * n)
	return matrix


def add_two(mat):
	a = randint(0, len(mat) - 1)
	b = randint(0, len(mat) - 1)
	while mat[a][b] != 0:
		a = randint(0, len(mat) - 1)
		b = randint(0, len(mat) - 1)
	mat[a][b] = 2
	return mat


def game_state(mat):
	over = False
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == 2048:
				over = True
				return 'win', over
	for i in range(len(mat) - 1):  # intentionally reduced to check the row on the right and below
		for j in range(len(mat[0]) - 1):  # more elegant to use exceptions but most likely this will be their solution
			if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
				return 'not over', over
	for i in range(len(mat)):  # check for any zero entries
		for j in range(len(mat[0])):
			if mat[i][j] == 0:
				return 'not over', over
	for k in range(len(mat) - 1):  # to check the left/right entries on the last row
		if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
			return 'not over', over
	for j in range(len(mat) - 1):  # check up/down entries on last column
		if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
			return 'not over', over
	over = True
	return 'lose', over


def reverse(mat):
	new = []
	for i in range(len(mat)):
		new.append([])
		for j in range(len(mat[0])):
			new[i].append(mat[i][len(mat[0]) - j - 1])
	return new


def transpose(mat):
	new = []
	for i in range(len(mat[0])):
		new.append([])
		for j in range(len(mat)):
			new[i].append(mat[j][i])
	return new


def cover_up(mat):
	new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	done = False
	for i in range(4):
		count = 0
		for j in range(4):
			if mat[i][j] != 0:
				new[i][count] = mat[i][j]
				if j != count:
					done = True
				count += 1
	return new, done


def merge(mat):
	score = 0
	done = False
	for i in range(4):
		for j in range(3):
			if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
				mat[i][j] *= 2
				mat[i][j + 1] = 0
				score += mat[i][j]
				done = True
	return mat, done, score


def up(game):
	# print("up")
	# return matrix after shifting up
	game = transpose(game)
	game, done = cover_up(game)
	temp = merge(game)
	game = temp[0]
	done = done or temp[1]
	game = cover_up(game)[0]
	game = transpose(game)
	return game, done, temp[2]


def down(game):
	# print("down")
	game = reverse(transpose(game))
	game, done = cover_up(game)
	temp = merge(game)
	game = temp[0]
	done = done or temp[1]
	game = cover_up(game)[0]
	game = transpose(reverse(game))
	return game, done, temp[2]


def left(game):
	# print("left")
	# return matrix after shifting left
	game, done = cover_up(game)
	temp = merge(game)
	game = temp[0]
	done = done or temp[1]
	game = cover_up(game)[0]
	return game, done, temp[2]


def right(game):
	# print("right")
	# return matrix after shifting right
	game = reverse(game)
	game, done = cover_up(game)
	temp = merge(game)
	game = temp[0]
	done = done or temp[1]
	game = cover_up(game)[0]
	game = reverse(game)
	return game, done, temp[2]


def gen():
	return randint(0, 3)


def generate_next(mat):
	rand_x = randint(0, 3)
	rand_y = randint(0, 3)
	index = (rand_x, rand_y)
	while mat[index[0]][index[1]] != 0:
		index = (gen(), gen())
	rand_val = randint(0,100)
	if(rand_val<80):
		mat[index[0]][index[1]] = 2
	else:
		mat[index[0]][index[1]] = 4
	return mat


def init_matrix():
	mat = new_game(4)

	mat = add_two(mat)
	mat = add_two(mat)
	return mat


moves = {'l': left, 'r': right, 'u': up, 'd': down}


def print_game(game_matrix):
	for i in game_matrix:
		print(i)


def get_game_matrix(mat):
	grid = []
	for i in mat:
		grid += i
	# print([tuple(grid)])
	return grid


def main_loop():
	game_matrix = init_matrix()
	while True:
		# print(score)
		print_game(game_matrix)
		move = input('Enter your move : ')
		if moves.get(move):
			game_matrix, done, score = moves[str(move)](game_matrix)
			# game_matrix = generate_next(game_matrix)
		get_game_matrix(game_matrix)


# main_loop()
# 0 up
# 1 right
# 2 down
# 3 left
bincodes = {'00': 0, '01': 1, '10': 2, '11': 3}
move_array = ['u', 'r', 'd', 'l']


def normalize(mat,flag,prev_move):
	g = get_game_matrix(mat)
	max_ele = math.log2(max(g))
	# print("max_ele {}".format(max_ele))
	k = []
	for i in g:
		if i != 0:
			k.append(1+(math.log2(i) / max_ele))
		else:
			k.append(i)
	if(flag==0):
		k.append(0)
	else:
		k.append(1+prev_move[0]+prev_move[1])
	return k


def make_move(game_matrix, move_tuple):
	illegal_move = False
	move = build_move(move_tuple)
	# print('selected move {}'.format(move))
	if moves.get(move):
		new_game_matrix, done, score = moves.get(move)(game_matrix)
		if new_game_matrix == game_matrix:
			# ILLEGAL MOVES HAVE BEEN MADE
			illegal_move = True
		else:
			game_matrix = generate_next(new_game_matrix)
	return game_matrix, score, illegal_move


def build_move(move_tuple):
	x, y = -1, -1
	if move_tuple[0] < 0.5:
		x = 0
	else:
		x = 1
	if move_tuple[1] < 0.5:
		y = 0
	else:
		y = 1
	move = move_array[bincodes.get(str(x) + str(y))]
	return move
