import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        player = pygame.image.load("images/player.png")
        self.images.append(player)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
