import pygame
pygame.init()

# Charge our background
background = pygame.image.load('PygameAssets-main/bg.jpg')

# generate the window for our game
pygame.display.set_caption("Comet Fall Game V1")
screen = pygame.display.set_mode((1080,720))

running = True 

# loop for the game
while running:
    
    # apply the background 
    screen.blit(background,(0,-200))
    
    # update our screen
    pygame.display.flip()
    
    # if the player closes this window
    for event in pygame.event.get():
        
        # To verifiy the event is closing the window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")