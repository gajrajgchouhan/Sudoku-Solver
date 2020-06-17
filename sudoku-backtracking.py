def printBoard(grid):
    """
    Printing the Sudoku Board
    """
    for i in range(9):
        if i%3 == 0 and i!=0:
            # Adding two horizontal lines, to separate the squres
            print("-----------------------")
        for j in range(9):
            if j%3 == 0 and j!= 0:
            # Adding Vertical lines, to separate the squares
                print(" | ",end='')
            # Printing the numbers
            if j==8:
                print(str(grid[i][j]))
            else:
                print(str(grid[i][j]),end=' ')

def squareGrid(row, col, grid):
    """
    This function identifies which of the 9 smaller grids 
    is a element part of. 
    """
    # position of the square box
    marker1, marker2 = (row//3)*3, (col//3)*3

    square = [grid[i][(marker2):(marker2+3)] for i in range(marker1,marker1+3)]

    # flattening the list
    square = [j for i in square for j in i]

    return square

def isComplete(grid):
    """
    Check if the sudoku board has been completed.
    """
    for row in range(0,9):
        for col in range(0,9):
          if grid[row][col]==0:
            return False
    return True

def solveGrid(grid):
    for row in range(9):
        for col in range(9):    
            # checking the cell
            if grid[row][col] == 0:
                # if zero, try the possible values
                for possible_answer in range(1,10):
                    # make sure possible_answer is not in it's row & it's column
                    if possible_answer not in grid[row]:
                        if possible_answer not in [grid[i][col] for i in range(9)]:
                            # check the possible_answer is not in the squares
                            if not possible_answer in squareGrid(row, col, grid):
                                grid[row][col] = possible_answer
                                if isComplete(grid):
                                    # If the board is solved, print the grid
                                    printBoard(grid)
                                    return True
                                else:
                                    # Solve the other remaining cells
                                    if solveGrid(grid):
                                        return True
                # Backtracking
                grid[row][col] = 0
                return None

grid = []
grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])
printBoard(grid)
print("\nSolving...\n")
solveGrid(grid)
print('\n')