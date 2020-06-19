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
    """
    Function to solve the grid using backtracking.
    """
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

import pygame
import time

# Initialize

pygame.init()

# Using comicsans
myfont = pygame.font.SysFont('comicsans', 50)
WIDTH, HEIGHT = 900, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
color = (0, 0, 0)

# Variables for the grid of GUI
linesinX, linesinY = 9, 9
gridWidth, gridHeight = WIDTH//linesinX, HEIGHT//linesinY

run = True

def drawSquare():
    # Bold lines for smaller 3x3 grid
    x, y = gridWidth*3, 0
    for i in range(2):
        pygame.draw.line(win, (0, 0, 0), (x*(i+1), y), (x*(i+1), HEIGHT), 6)
    x, y = 0, gridHeight*3
    for i in range(2):
        pygame.draw.line(win, (0, 0, 0), (x, y*(i+1)), (WIDTH, y*(i+1)), 6)        

def fillNumbers():
    h, w = len(grid), len(grid[0])
    x, y = 40, 30
    for row in range(h):
        for col in range(w):
            text = str(grid[row][col])
            if text == "0":
                text = ""
            txt = myfont.render(text, 1, color)
            win.blit(txt, (x, y))
            x += gridWidth
        y += gridHeight
        x = 40

def drawGrid():
    posX, posY = 0, 0
    for i in range(linesinY):
        for j in range(linesinX):
            pygame.draw.line(win, (0, 0, 0), (posX, posY), (posX, posY+gridHeight), 2)
            posX += gridWidth
        pygame.draw.line(win, (0,0,0), (0,posY), (WIDTH, posY), 2)
        posY += gridHeight
        posX = 0

def fll():
    win.fill((255, 255, 255))
    drawGrid()
    drawSquare()
    fillNumbers()
    pygame.display.update()

print("STARTING..")

while run:
    pygame.time.delay(100)
    # 100 ms
    for event in pygame.event.get():
        # listen to mouse/kb events.
        if event.type == pygame.QUIT:
            print("ENDING...")
            run = False

    keys = pygame.key.get_pressed()

    fll()
    solveGrid(grid)
    fll()

pygame.quit()