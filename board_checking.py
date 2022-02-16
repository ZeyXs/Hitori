from copy import deepcopy
import colorama
from termcolor import colored as c

colorama.init()

"""
-1 = Blank
0 = Checked
1 = Safe
"""

class CheckingBoard:
	def __init__(self, board):
		self.board = deepcopy(board)
		self.submitted_board = deepcopy(self.board)

		self.total_case = len(self.board)*len(self.board) #On admet que la board est carré...
		self.checked_case = len([case for line in self.board for case in line if case[1] == 0])

	def start(self):
		# Check if we can spread everywhere (no case separated from the group)
		if self.recursive_spread((0,0)) != self.total_case-self.checked_case:
			return self.is_invalid("Unable to spread everywhere")
		else:
			self.reset_board()
			
			# Check if there's no two checked case neighbor
			if not self.recursive_check_neighbors((0,0)):
				return self.is_invalid("At least 2 checked case are neighbors...")
			else:
				self.reset_board()
				
				# Check if there's no not-checked doublon in same line
				if not self.recursive_check_for_doublon_on_line():
					return self.is_invalid("There's a doublon in a line somewhere")
				else:
					self.reset_board()
					
					# Check if there's no not-checked doublon in same column
					if not self.recursive_check_for_doublon_on_column():
						return self.is_invalid("There's a doublon in a column somewhere")
					else:
						return self.is_valid()

	def reset_board(self):
		self.board = deepcopy(self.submitted_board)

	def show(self):
		"""
			Display the board in terminal, with color
		"""
		for line in self.board:
			for col in line:
				if col[1] == -1:
					print(c(col[0], "white"), end=" ")
				elif col[1] == 0:
					print(c(col[0], "red"), end=" ")
				elif col[1] == 1:
					print(c(col[0], "green"), end=" ")
			print()
		print()

	def is_invalid(self, err_msg):
		return False, err_msg

	def is_valid(self):
		return True, None


	def has_neighbors(self, x,y, state=0, notstate=False):
		"""
			This function return the neighbors of (x,y) with a state of -2
				#left   ->  0, -1
				#top    -> -1,  0
				#right  ->  0, +1
				#bottom -> +1,  0
		"""
		neighbors = []
		posx,posy = [0,-1,0,1], [-1,0,1,0]
		for i in range(4):
			px,py = posx[i], posy[i]

			if not (x + px >= 0) or not (y + py >= 0): #Prevent it to be negative, and thus linking to the board opposite side
				continue

			try: neighbor = self.board[x+px][y+py]
			except IndexError: continue #IndexError triggered when the (x,y) case is on board borders 

			if (type(notstate) == bool and neighbor[1] == state) or (neighbor[1] != notstate):
				# .append / .insert / += to neighboar list object were bugged
				# it was done 3 times, with no reaons.
				# Had to hack it
				neighbor = (neighbor[0], neighbor[1], (x+px, y+py))
				neighbor = list(neighbor)
				neighbors.append(neighbor)

		return neighbors if neighbors else False

	def recursive_spread(self, pos: tuple):
		px,py = pos
		value,state = self.board[px][py]
		total = 0

		if state == 0 and px == 0 and py == 0:
			return total + self.recursive_spread((px,py+1)) 
		
		elif state == 69:
			return total
		else:
			self.board[px][py][1] = 69
			total += 1


		neighborhood = self.has_neighbors(px,py, state=False, notstate=0)
		if neighborhood:
			for neighbor in neighborhood:
				if neighbor[1] != 69: # Already spread there
					#self.board[neighbor[2][0]][neighbor[2][1]][1] = 69 
					total += self.recursive_spread(neighbor[2])

		return total

	def recursive_check_neighbors(self, pos: tuple):
		px,py = pos
		try:
			value,state = self.board[px][py]
		except:
			try:
				return self.recursive_check_neighbors((px+1, py-1)) 
			except:
				return True

		if state == 0:
			neighborhood = self.has_neighbors(px,py, state=0)
			if not neighborhood:
				return self.recursive_check_neighbors((px,py+1))
			
			for neighbor in neighborhood:
				if neighbor[1] == 0:
					return False

			return self.recursive_check_neighbors((px,py+1))

		else:
			return self.recursive_check_neighbors((px,py+1))

	def recursive_check_for_doublon_on_line(self, line_idx: int=0):
		line = [x[0] for x in self.board[line_idx] if x[1] != 0]
		dic = {e:line.count(e) for e in line}

		for el in dic:
			if dic[el] > 1:
				return False

		if line_idx+1 >= len(self.board[0]):
			return True
		return self.recursive_check_for_doublon_on_line(line_idx+1)

	def recursive_check_for_doublon_on_column(self, column_idx: int=0):
		line = []
		for lidx,l in enumerate(self.board):
			el = self.board[lidx][column_idx]
			if el[1] == 0:
				continue
			line.append(el[0])

		dic = {e:line.count(e) for e in line}

		for el in dic:
			if dic[el] > 1:
				return False

		if column_idx+1 >= len(self.board[0]):
			return True
		return self.recursive_check_for_doublon_on_column(column_idx+1)
