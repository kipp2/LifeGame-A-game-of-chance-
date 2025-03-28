import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (50, 50, 50)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

# Create Grid
grid = np.zeros((ROWS, COLS), dtype=int)

def draw_grid():
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row, col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def update_grid():
    global grid
    new_grid = grid.copy()
    for row in range(ROWS):
        for col in range(COLS):
            alive_neighbors = np.sum(grid[max(row-1, 0):min(row+2, ROWS), max(col-1, 0):min(col+2, COLS)]) - grid[row, col]
            if grid[row, col] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[row, col] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[row, col] = 1
    grid = new_grid

running = True
simulating = False
while running:
    screen.fill(BLACK)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulating = not simulating
            elif event.key == pygame.K_r:
                grid = np.zeros((ROWS, COLS), dtype=int)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid[y // CELL_SIZE, x // CELL_SIZE] ^= 1
    
    if simulating:
        update_grid()
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

