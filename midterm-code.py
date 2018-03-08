# midterm-code.py 2018-03-08

class Cell(object):
	def __init__(self, state=0):
		self.state = state

	def get_state(self):
		return self.state

	def next_life(self, grid, row, col):
		"""Return the next state of a cell object as zero or one.
		This method does not modify the state attribute.
		Parameters are the grid and location of the cell object within grid.
		"""
		alive_nbrs = 0
		nbrs = [(row-1, col+1), (row+1, col+1), (row+1, col-1), (row-1, col-1)]
		for x, y in nbrs: 
			try:
				alive_nbrs += grid[x][y].get_state()
			except IndexError:
				pass # nbr on boundary - ignore and continue iteration
		
		if self.state > 0:
			if alive_nbrs < 1 or alive_nbrs > 2:
				return 0
		elif alive_nbrs == 2: 
			return 1
		
		return self.state

class PrisonCell(Cell):
	def next_life(self, grid, row, col):
		alive_nbrs = 0
		nbrs = [(row-1, col), (row+1, col)]
		for x, y in nbrs: 
			try:
				alive_nbrs += grid[x][y].get_state()
			except IndexError:
				pass # nbr on boundary - ignore and continue iteration
		
		if self.state > 0:
			if alive_nbrs == 0 or alive_nbrs > 1:
				return 0
		elif alive_nbrs == 2: 
			return 1
		
		return self.state				


class Grid(object):
	
	def __init__(self, d=5, initial=[]):
		""" 
		d is the width and height of the grid
		initial is a list of tuples of the form: [(row, col), (row, col), ...]
		"""
		limit = range(d)
		self.size = d
		self.data = [[Cell() for j in limit] for i in limit]

		for i, j in initial:
			self.data[i][j].state = 1

	def __str__(self):
		return self.display_on_terminal()

	def display_on_terminal(self):
		s = ''
		for i in gol.data: 
			s += ' '.join([str(j.get_state()) for j in i])
			s += '\n'
		return s

if __name__ == '__main__':
	# Hi midterm examinees, you might want to start with a grid object!
	pass

			   


