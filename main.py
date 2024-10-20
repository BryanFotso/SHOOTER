import pygame
import math

from game import Game

pygame.init()

# charge our game
game = Game()

# generate the window for our game
pygame.display.set_caption("Comet Fall Game V1")
screen = pygame.display.set_mode((1080,720))

# Charge our background
background = pygame.image.load('PygameAssets-main/bg.jpg')

#charge our background image
banner = pygame.image.load("PygameAssets-main/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charge the play button
play_button = pygame.image.load("PygameAssets-main/button.png")
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2.0)


running = True 

# loop for the game
while running:
    
    # apply the background                     
    screen.blit(background,(0,-200))
    
    # verify if the game has started or not
    if game.is_playing:
        game.update(screen)
    else :
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

        
    # update our screen
    pygame.display.flip()
    
    # if the player closes this window
    for event in pygame.event.get():
        
        # To verifiy the event is closing the window 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
        # To detect movement from keyboard   
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
            
            # To detect if the player wants to attack
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
             
            