import pygame

# Initialisation
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jeu de Plateau")
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Variables
grid_size = 8
cell_size = 600 // grid_size

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner le plateau
    screen.fill(WHITE)
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK if (row + col) % 2 == 0 else WHITE, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()