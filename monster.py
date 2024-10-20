import pygame
import random

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.15
        self.image = pygame.image.load("PygameAssets-main/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 100)
        self.rect.y = 540 
        self.velocity = 0.25 + random.uniform(0, 0.5)
        self.float_x = float(self.rect.x)  # Use a float to sum the movement
        
    def move(self):
        
        # The movement is done only if there is no collision 
        if not self.game.check_collision(self, self.game.all_players):
            self.float_x -= self.velocity  # Sum the movement in float
            self.rect.x = int(self.float_x)  # Update the real movement
        
        # damage the player when there is collision
        else : 
            self.game.player.damage(self.attack)
            
    def update_health_bar(self, surface):
        
        # define a color for the life 
        bar_color = (111, 210, 46)
        
        # define a color for the backspace of the life 
        back_bar_color = (60,63,60)
        
        #define the position of the background of the life 
        back_bar_position = [self.rect.x + 10 , self.rect.y - 15 , self.max_health, 5]
        
        # define the position of its life, its thikness and thinnness
        bar_position = [self.rect.x + 10 , self.rect.y - 15 , self.health, 5]

        # Draw our life bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        
        # Draw our life bar
        pygame.draw.rect(surface, bar_color, bar_position)
    
    # to take into account the damage    
    def damage(self, amount_of_damage):
        self.health -= amount_of_damage
        
        # Verify if the monster is still alive
        if self.health <= 0:
            self.rect.x = 900 + random.randint(0, 100)
            self.float_x = float(self.rect.x)
            self.health = self.max_health
            self.velocity = 0.25 + random.uniform(0, 0.5)
            
        
