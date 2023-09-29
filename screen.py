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
    

    def render_text(self,pos,text,color = 'black',font_size=40,anchor='topleft'):
        self.font = pygame.font.Font(None, font_size)
        self.pos = pos
        self.text = text
        self.font_color = color
        self.rect_anchor = anchor
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        setattr(self.rect, self.rect_anchor, self.pos)

        return [self.image,self.rect]


    def render_many_text(self,rows):
        texts_list = []
        height = 0
        for row in range(rows):                   
            texts_list.append(self.render_text((0,height),'many rows'))
            height += 22
        return texts_list
        
    def blit_many_text(self,rows):
        for row in self.render_many_text(rows):
            self.screen.blit(row[0],row[1])


   
    def lines(self):
        pygame.draw.line(self.screen,color='black',start_pos=(half_W,0),end_pos=(half_W,HEIGHT))
        pygame.draw.line(self.screen,color='black',start_pos=(0,half_H),end_pos=(WIDTH,half_H))
    
    def run(self):
        while True:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # keydown
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            
            self.screen.fill('white')
            
            self.blit_many_text(10)

            self.lines()

                                
            pygame.display.flip()           
            self.clock.tick(FPS)

class Text(pygame.sprite.Sprite):
    def __init__(self, text, font_size,pos,anchor='topleft',groups=None):
        if groups is not None:
            super().__init__(groups)

        pygame.font.init()
        self.font = pygame.font.Font(font_size)
        self.pos = pos
        self.text = text
        self.font_color = 'black'   
        self.rect_anchor = anchor
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        setattr(self.rect, self.rect_anchor, self.pos)

if __name__ == '__main__':
    game = Game()
    game.run()

    