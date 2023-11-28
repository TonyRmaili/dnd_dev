import pygame,sys, os
from settings2 import *

from char3 import Character, view_char
from races import races
from backgrounds import backgrounds
from classes import fighter, wizard
from debug import debug

class CreationScreen:  
    def __init__(self,game):
        # general setup       
        self.game = game
        self.screen = pygame.display.get_surface()
        # layers and groups
        self.party_grp = party_grp
        self.selection_grp = selection_grp
        self.ability_grp = ability_grp
        self.race_grp = race_grp
        self.background_grp = background_grp
        self.class_grp = class_grp
        self.token_grp = token_grp
        # background 
        self.cr_background = Image(pic_path+'char_creation_bg.jpg',WIDTH,HEIGHT,(0,0),
                                   anchor='topleft')
        self.caption = Text('Character Creation',50,(WIDTH//2,50),
                            anchor='center')
           
        # stage values
        self.stage = 'party_size'
        self.name_text = ''
        self.party_size_num = 1
        self.que = 0
        self.selection = None

        # final character values
        self.race = None
        self.background = None
        self.cls = None
        self.token = None

        self.stre = 8
        self.dex = 8
        self.con = 8
        self.inte = 8
        self.wis = 8
        self.cha = 8

        

    def test_blit(self,pos,txt,screen,anchor='topleft'):
        font = pygame.font.Font(None,50)
        position = pos
        text = txt
        font_color = 'black'
        rect_anchor = anchor
        image = font.render(text,True,font_color)
        rect = image.get_rect()
        setattr(rect,rect_anchor,position)

        screen.blit(image,rect)


    def create_char(self):
        char = Character(self.name_text,
                         self.race,
                         self.background, 
                         self.stre, self.dex, self.con, self.inte, self.wis, self.cha,                       
                         [camera_grp,players,obstacles]
                         )
        
        races(char,self.race)
        backgrounds(char,self.background)
        if self.cls == 'fighter':
            fighter(char)
        elif self.cls == 'wizard':
            wizard(char)

        char.load_image(self.token,(400+(self.que*50),400+(self.que*50)))
        #view_char(char)
        

    def party_selection(self,pos):
        if plus_box.rect.collidepoint(pos):
            self.party_size_num += 1
            
        elif minus_box.rect.collidepoint(pos):
            self.party_size_num -= 1
            if self.party_size_num <= 0:
                self.party_size_num = 1
        party_num_box.new_text(str(self.party_size_num))
        party_num_box.draw_border('black',2)

    def selection_panel(self,pos):
        if ability_box.rect.collidepoint(pos):
            self.selection = 'ability'
        
        elif race_box.rect.collidepoint(pos):
            self.selection = 'race'

        elif background_box.rect.collidepoint(pos):
            self.selection = 'background'
        
        elif class_box.rect.collidepoint(pos):
            self.selection = 'class'
        
        elif token_box.rect.collidepoint(pos):
            self.selection = 'token'
 
    def ability_scores_click(self,pos):      
        for i, plus in enumerate(plus_list):
            if plus.rect.collidepoint(pos):             
                abs_score[i] += 1
                ability_list[i].new_text2(str(abs_score[i]))                  
                break
        for i, minus in enumerate(minus_list):
            if minus.rect.collidepoint(pos):
                abs_score[i] -= 1
                ability_list[i].new_text(str(abs_score[i]))                  
                break
        self.stre, self.dex, self.con, self.inte, self.wis, self.cha = abs_score
      
    def race_selection(self,pos):
        if human_box.rect.collidepoint(pos):
            self.race = 'human'
            
        elif dwarf_box.rect.collidepoint(pos):
            self.race = 'dwarf'
            
        elif elf_box.rect.collidepoint(pos):
            self.race = 'elf'
            
    def bg_selection(self,pos):
        if soldier_box.rect.collidepoint(pos):
            self.background = 'soldier'
        elif sage_box.rect.collidepoint(pos):
            self.background = 'sage'

    def class_selection(self,pos):
        if fighter_box.rect.collidepoint(pos):
            self.cls = 'fighter'
        elif wizard_box.rect.collidepoint(pos):
            self.cls = 'wizard'

    def token_selection(self,pos):
        for image in images:
            if image[1].rect.collidepoint(pos):
                self.token = image[0]
                break

    def name_entry(self,key):    
        if key == pygame.K_BACKSPACE:
            self.name_text = self.name_text[:-1]          
        else:         
            self.name_text += pygame.key.name(key)
        name_box.new_text(self.name_text)

    def event_listner(self):
        for event in pygame.event.get():
            # handles quits 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if self.stage == 'party_size':
                    if event.key == pygame.K_RETURN:
                        self.stage = 'main_stage'   
                     
                else:
                    if event.key == pygame.K_RETURN:
                        self.create_char()
                        self.que += 1

                        if self.que == self.party_size_num:
                            self.game.switch_mode('bonfire')

                    self.name_entry(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.stage == 'party_size':               
                    self.party_selection(event.pos)
                else:
                    self.selection_panel(event.pos)

                    if self.selection == 'ability':
                        self.ability_scores_click(event.pos)
                    elif self.selection == 'race':
                        self.race_selection(event.pos)
                    elif self.selection == 'background':
                        self.bg_selection(event.pos)
                    elif self.selection == 'class':
                        self.class_selection(event.pos)
                    elif self.selection == 'token':
                        self.token_selection(event.pos)
                
    def run(self):
        self.event_listner()
        # draw constants
        
        self.screen.blit(self.cr_background.image,self.cr_background.rect)
        self.screen.blit(self.caption.image,self.caption.rect)

        # draw layers       
        if self.stage == 'party_size':    
            self.party_grp.draw(self.screen)
            
        else:          
            self.selection_grp.draw(self.screen)

            if self.selection == 'ability':
                self.ability_grp.draw(self.screen)
            elif self.selection == 'race':
                self.race_grp.draw(self.screen)
            elif self.selection == 'background':
                self.background_grp.draw(self.screen)
            elif self.selection == 'class':
                self.class_grp.draw(self.screen)
            elif self.selection == 'token':
                self.token_grp.draw(self.screen)
            
       
        debug(f'{self.stre}',(10,10))
        debug(f'{self.dex}',(10,20))
        debug(f'{self.con}',(10,30))
        debug(f'{self.inte}',(10,40))
        debug(f'{self.wis}',(10,50))
        debug(f'{self.cha}',(10,60))
        debug(f'{self.token}',(10,70))  

