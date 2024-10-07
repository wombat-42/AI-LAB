class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state  
        self.goal_state = goal_state

    def is_goal(self, state):
       
        return state == self.goal_state

    def get_possible_moves(self, state):
      
        moves = []
        row, col = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
        
        if row > 0: 
            moves.append(self.swap(state, row, col, row-1, col))
        if row < 2: 
            moves.append(self.swap(state, row, col, row+1, col))
        if col > 0: 
            moves.append(self.swap(state, row, col, row, col-1))
        if col < 2: 
            moves.append(self.swap(state, row, col, row, col+1))
        
        return moves

    def swap(self, state, row1, col1, row2, col2):
        
        new_state = [list(row) for row in state]  
        new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]  # Swap
        return new_state

    def dls(self, state, depth, path, visited):
  
        if self.is_goal(state):
            return path
        
        if depth == 0:
            return None
        
        visited.add(tuple(map(tuple, state)))  
        
      
        for move in self.get_possible_moves(state):
            if tuple(map(tuple, move)) not in visited:
                result = self.dls(move, depth-1, path + [move], visited)
                if result:
                    return result
        
        visited.remove(tuple(map(tuple, state)))  
        return None

    def ids(self, max_depth):
        
        for depth in range(max_depth):
            visited = set()
            result = self.dls(self.initial_state, depth, [self.initial_state], visited)
            if result:
                return result
        return None


initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]] 
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]    

puzzle = Puzzle(initial_state, goal_state)
max_depth = 20 
solution = puzzle.ids(max_depth)


if solution:
    print("Solution found:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")





# Solution found:
# [1, 2, 3]
# [4, 0, 5]
# [6, 7, 8]

# [1, 2, 3]
# [4, 5, 0]
# [6, 7, 8]

# [1, 2, 3]
# [4, 5, 8]
# [6, 7, 0]

# [1, 2, 3]
# [4, 5, 8]
# [6, 0, 7]

# [1, 2, 3]
# [4, 5, 8]
# [0, 6, 7]

# [1, 2, 3]
# [0, 5, 8]
# [4, 6, 7]

# [1, 2, 3]
# [5, 0, 8]
# [4, 6, 7]

# [1, 2, 3]
# [5, 6, 8]
# [4, 0, 7]

# [1, 2, 3]
# [5, 6, 8]
# [4, 7, 0]

# [1, 2, 3]
# [5, 6, 0]
# [4, 7, 8]

# [1, 2, 3]
# [5, 0, 6]
# [4, 7, 8]

# [1, 2, 3]
# [0, 5, 6]
# [4, 7, 8]

# [1, 2, 3]
# [4, 5, 6]
# [0, 7, 8]

# [1, 2, 3]
# [4, 5, 6]
# [7, 0, 8]

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 0]
