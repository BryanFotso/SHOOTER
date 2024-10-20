import pygame

from game import Game

pygame.init()

# Charge our background
background = pygame.image.load('PygameAssets-main/bg.jpg')

# charge our game
game = Game()

# generate the window for our game
pygame.display.set_caption("Comet Fall Game V1")
screen = pygame.display.set_mode((980,720))
 
running = True 

# loop for the game
while running:
    
    # apply the background                     
    screen.blit(background,(0,-200))
    
    # apply our player
    screen.blit(game.player.image, game.player.rect)
    
    # apply all the projectiles
    for projectile in game.player.all_projectile:
        projectile.move()
        
    for monster in game.all_monsters:
        monster.move()
     
    # apply all the images of the projectile
    game.player.all_projectile.draw(screen)
    
    # apply all the images of the monster
    game.all_monsters.draw(screen)
    
    #Verify the player movement
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0 : 
        game.player.move_left()
    
    print(game.player.rect.x)
    
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
             
            