import pygame

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("PygameAssets-main/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 540
        self.velocity = 0.25
        self.float_x = float(self.rect.x)  # Use a float to sum the movement
    def move(self):
        
        # The movement is done only if there is no collision 
        if not self.game.check_collision(self, self.game.all_players):
            self.float_x -= self.velocity  # Sum the movement in float
            self.rect.x = int(self.float_x)  # Update the real movement
