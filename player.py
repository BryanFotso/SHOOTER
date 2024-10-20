import pygame

from projectile import Projectile

#sprite are objects that move 
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100 
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 500
        self.all_projectile = pygame.sprite.Group()
        
    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))
        
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity