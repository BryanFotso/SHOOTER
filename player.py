import pygame

from projectile import Projectile

#sprite are objects that move 
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        
        super().__init__()
        self.game = game
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
        
    # to take into account the damage    
    def damage(self, amount_of_damage):
        self.health -= amount_of_damage
        
        # Verify if the player is death
        if self.health <= 0:
             self.game.game_over()
             
    def move_right(self):
        
        #if the player is not colliding with a monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
        
    def update_health_bar(self, surface):
        
        # define a color for the life 
        bar_color = (111, 210, 46)
        
        # define a color for the backspace of the life 
        back_bar_color = (60,63,60)
        
        #define the position of the background of the life 
        back_bar_position = [self.rect.x + 50 , self.rect.y, self.max_health, 7]
        
        # define the position of its life, its thikness and thinnness
        bar_position = [self.rect.x + 50 , self.rect.y, self.health, 7]

        # Draw our life bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        
        # Draw our life bar
        pygame.draw.rect(surface, bar_color, bar_position)