import pygame

from player import Player
from monster import Monster
from comet_event import CometFallEvent

class Game: 
    
    def __init__(self):
        
        # define if the game has started or not
        self.is_playing = False
        
        # generating a player
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        
        #generate the event cometfall
        self.comet_event = CometFallEvent(self)
        # generating a list which will stock all the monster
        self.all_monsters = pygame.sprite.Group()
        
        # generating a list inorder to stock all the keys pressed on the keyboard
        self.pressed = {}

    def spawn_monster(self):
        
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    def check_collision(self, sprite, group):
        
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def update(self,screen):
        
        # apply our player
        screen.blit(self.player.image, self.player.rect)
    
        # Update the projectile movement
        for projectile in self.player.all_projectile:
            projectile.move()
    
        # update health bar of the player
        self.player.update_health_bar(screen)
        
        #update the event bar to charge the comet
        self.comet_event.update_bar(screen)
        
        #Update the movement of the comet
        for comet in self.comet_event.all_comets:
            comet.fall()
            
        # update health bar and movement of the monster    
        for monster in self.all_monsters:
            monster.move()
            monster.update_health_bar(screen)
     
        # apply all the images of the projectile
        self.player.all_projectile.draw(screen)

        # apply all the images of the monster
        self.all_monsters.draw(screen)
        
        # apply all the images of the comet
        self.comet_event.all_comets.draw(screen)
        
        # Verify the player movement
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0 : 
            self.player.move_left()
    
    # To restart the game by removing all the monsters and     
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.comet_event.reset_percent()
        self.comet_event.all_comets = pygame.sprite.Group()
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()