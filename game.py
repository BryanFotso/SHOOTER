import pygame

from player import Player
from monster import Monster

class Game: 
    
    def __init__(self):
        
        # generating a player
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        
        # generating a list which will stock all the monster
        self.all_monsters = pygame.sprite.Group()
        
        # generating a list inorder to stock all the keys pressed on the keyboard
        self.pressed = {}
        
        self.spawn_monster()
        
    
    def spawn_monster(self):
        
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    def check_collision(self, sprite, group):
        
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)