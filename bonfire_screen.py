import pygame,sys
from settings2 import *

class BonFire:  
    def __init__(self,game):
        # link to the main screen
        self.screen = pygame.display.get_surface()
        
        # the sprite members
        self.bonfire_grp = bonfire_grp

        # game mode 
        self.game = game
        
    
    def event_get(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                elif event.key == pygame.K_q:
                    self.game.switch_mode('battle')

    def run(self):
        self.event_get()
        self.bonfire_grp.draw(self.screen)