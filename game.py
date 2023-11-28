import pygame
from battle_screen import BattleScreen
from settings2 import *
from bonfire_screen import BonFire
from debug import debug
from creation3 import CreationScreen


class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        # game modes / screens
        self.game_mode = 'battle'

        self.switch_mode(self.game_mode)

        # self.battle_screen= BattleScreen(self)
        # self.bonfire_screen = BonFire(self)
        # self.creation_screen = CreationScreen(self)
        

    def switch_mode(self, new_mode):
        self.game_mode = new_mode

        #creates new instances. how would carry over data work? tbc 
        # removing this seems to unable players_grp but not camera and obstacle - why 
        if new_mode == 'battle':
            self.battle_screen = BattleScreen(self)
        elif new_mode == 'bonfire':
            self.bonfire_screen = BonFire(self)
        elif new_mode == 'creation':
            self.creation_screen = CreationScreen(self)
     
    def run(self):
        while True:  

            self.screen.fill('white')  

            if self.game_mode == 'battle':
                self.battle_screen.run()

            elif self.game_mode == 'bonfire':
                self.bonfire_screen.run()

            elif self.game_mode == 'creation':
                self.creation_screen.run()
                                      
            pygame.display.flip()           
            self.clock.tick(FPS)

   
if __name__ == '__main__':
    game = Game()
    game.run()

    