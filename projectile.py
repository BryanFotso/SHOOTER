import pygame 

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0
        
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        # To verify if our projectile is in collision with a monster
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            
            # delete the projectile
            self.remove()
        
        # To verify if our projectile is out of the screen
        if self.rect.x > 1080:
            
            # delete the projectile
            self.remove()
            
    def remove(self):
         self.player.all_projectile.remove(self)
    
    # To rotate the projectile     
    def rotate(self):
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center = self.rect.center)