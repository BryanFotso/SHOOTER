import pygame
import random

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('PygameAssets-main/comet.png')   
        self.rect = self.image.get_rect()
        self.velocity = 0.25 + random.uniform(0.1 , 0.9)
        self.float_rect_y = float(self.rect.y)
        self.rect.x = self.rect.x + random.randint(0, 900)
        self.rect.y = - random.randint(0, 300)
        self.comet_event = comet_event
        
    def fall(self):
        self.float_rect_y += self.velocity
        self.rect.y = int(self.float_rect_y)
        
        if self.rect.y >= 500:
            print("sol")
            self.remove()
            
            if len(self.comet_event.all_comets) == 0:
                print("The event is finish")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
                
        if self.comet_event.game.check_collision(self,
                                                 self.comet_event.game.all_players):
            print("Joueur touché")
            self.remove()
            # hit the player 20 points
            self.comet_event.game.player.damage(20)
    
    def remove(self):
        self.comet_event.all_comets.remove(self)
        
        # verify if the number of comet is null
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

        