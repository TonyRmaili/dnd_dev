import pygame,sys


WIDTH = 800
half_W = WIDTH//2
HEIGHT = 600
half_H = HEIGHT//2
FPS = 30


# 1-These pages needs to be able to display all the info/text passed in -> scolling functionality 
# 3-lastly a save func is needed
# 4-bonus aps - damage calc, large dice, costum dice

class Page:
    def __init__(self):
        '''abstract class'''
        self.text = None
        self.background = None
    
    def generate_page(self):
        pass

class Bottom(Page):
    '''expected to have switching page functionality'''
    def __init__(self):
        super().__init__()
        pass

    def switch_page(self):
        pass

class Stats(Page):
    '''Fixed page; main figures displayed for combat;
        hp,AC,DCs,Movement,death saves/fails,'''
    def __init__(self):
        super().__init__()
        pass

class Resource(Page):
    '''fixed page; displays resoures;
        spellslots/points, class resources, resets at short/long rest etc'''
    def __init__(self):
        super().__init__()
        pass

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

    def lines(self):
        pygame.draw.line(self.screen,color='black',start_pos=(half_W,0),end_pos=(half_W,HEIGHT))
        pygame.draw.line(self.screen,color='black',start_pos=(0,half_H),end_pos=(WIDTH,half_H))
    
    def run(self):
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('white')
            self.lines()

            
                                      
            pygame.display.flip()           
            self.clock.tick(FPS)

   
if __name__ == '__main__':
    game = Game()
    game.run()

    