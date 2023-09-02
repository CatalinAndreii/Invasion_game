import pygame
from player import Player
pygame.init()

# Useful data
fps = 60
X = 800
Y = 700
dt = 0.7
running = True
player = Player()
player.rect.x = 380
player.rect.y = 570
player_list = pygame.sprite.Group()
player_list.add(player)

# load images
ICON = pygame.image.load("images/icon.png")
BACKGROUND = pygame.image.load("images/background.jpg")

# set the resolution, title, icon, background
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pygame.display.set_caption("Revolution")
pygame.display.set_icon(ICON)
background = screen.get_rect()


# running display
while running:
    # close the window when you click X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.rect.y -= 10 * dt
    if keys[pygame.K_s]:
        player.rect.y += 10 * dt
    if keys[pygame.K_a]:
        player.rect.x -= 10 * dt
    if keys[pygame.K_d]:
        player.rect.x += 10 * dt

    # update screen
    screen.blit(BACKGROUND, background)
    player_list.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps) / 1000

pygame.quit()
