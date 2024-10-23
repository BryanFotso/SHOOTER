import pygame
from comet import Comet
# create a class that will manage the rain of comet
class CometFallEvent():
    
    # during the charge create a counter
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 15
        self.game = game
        self.fall_mode = False
        
        # define a group of sprite to stock all the comets
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
    
    def meteor_fall(self):
        for i in range(1, 10):
            self.all_comets.add(Comet(self))
    
    #this function will attempt to launch the comet fall if the bar is fully loaded
    def attempt_fall(self):
        
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Comet rain")
            self.meteor_fall()
            self.fall_mode = True

    
    def update_bar(self, surface):
        
        self.add_percent()
        
         # define a color to charge the event 
        bar_color = (187, 11, 11)
        
        # define a color for the backspace of the life 
        back_bar_color = (0,0,0)
        
        #define the position of the background of the life 
        back_bar_position = [0, 
                             surface.get_height() - 20 ,
                             surface.get_width(),
                             10 # this is the thickness of the bar
                             ]
        
        # define the position of its life, its thikness and thinnness
        bar_position = [0, 
                        surface.get_height() - 20 ,
                        (surface.get_width()/100) * self.percent,
                        10 # this is the thickness of the bar
                        ]
        # Draw our back_bar 
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        
        # Draw our life bar on our back_bar
        pygame.draw.rect(surface, bar_color, bar_position)