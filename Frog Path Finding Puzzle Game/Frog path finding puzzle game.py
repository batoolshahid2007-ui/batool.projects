import pygame

pygame.init()
W = 500
ROWS = 10
SIZE = W // ROWS

screen = pygame.display.set_mode((W, W))
pygame.display.set_caption("Play A* Maze Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

grid = [[0]*ROWS for _ in range(ROWS)]

obstacles = [
    (1,1),(1,2),(1,3),(2,3),(3,3),
    (4,3),(5,3),(6,3),(6,4),(6,5),
    (7,5),(8,5),(8,6),(7,7),(6,7),
    (5,7),(4,7),(3,7),(2,7),(1,7)
]
for x, y in obstacles:
    grid[x][y] = 1
  
player_x, player_y = 9, 0  
goal_x, goal_y = 0, 9      

run = True
clock = pygame.time.Clock()

while run:
    screen.fill(WHITE)
    
    for i in range(ROWS):
        for j in range(ROWS):
            color = BLUE
            if grid[i][j] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, (j*SIZE, i*SIZE, SIZE, SIZE))
            pygame.draw.rect(screen, WHITE, (j*SIZE, i*SIZE, SIZE, SIZE), 1)
            
    pygame.draw.circle(screen, YELLOW, (goal_y*SIZE+SIZE//2, goal_x*SIZE+SIZE//2), 15)
    pygame.draw.circle(screen, RED, (player_y*SIZE+SIZE//2, player_x*SIZE+SIZE//2), 15)
    pygame.display.update()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            new_x, new_y = player_x, player_y
            
            if e.key == pygame.K_UP:
                new_x -= 1
            elif e.key == pygame.K_DOWN:
                new_x += 1
            elif e.key == pygame.K_LEFT:
                new_y -= 1
            elif e.key == pygame.K_RIGHT:
                new_y += 1
                
            if 0 <= new_x < ROWS and 0 <= new_y < ROWS:
                if grid[new_x][new_y] != 1:
                    player_x, player_y = new_x, new_y

    if player_x == goal_x and player_y == goal_y:
        print("congratulations you have won the game! 🎉")
        run = False
        
    clock.tick(30)

pygame.quit()
