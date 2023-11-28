from settings2 import *
import pygame,sys
from debug import debug

class BattleScreen:
    def __init__(self,game):
        self.game = game
        # link to the main screen
        self.screen = pygame.display.get_surface() 
        # create grps for all the sprites
        self.groups()
                                  
        self.initiative_order()
    
        # tracks current players turn
        self.turn = 0    
        self.acter = self.in_order[self.turn]        
        # camera modes
        self.camera_pos = [self.acter.rect.centerx , self.acter.rect.centery]
        self.menus()

    def menus(self):
        self.action_menu_on = False
        self.bon_action_meno_on = False      
        self.status_on = False

        self.clicked_sprite = None    
        self.target_menu = None
 

    def initiative_order(self):
        # create lists with all combatants
        self.in_order = self.players.sprites() + self.monsters.sprites()

        # initiative
        initiative_list = [] 
        for char in self.in_order:
           initiative_list.append((char.roll_check(1),char))

        initiative_list = sorted(initiative_list, key=lambda x: x[0], reverse=True)
        self.in_order = []

        for i in initiative_list:
            self.in_order.append(i[1])

    def groups(self):
        self.players = players
        self.monsters = monsters
        self.camera_grp = camera_grp
        self.obstacles = obstacles
        self.button_grp = button_grp

    def active_menus(self):
        if self.action_menu_on == True:   
            # menu and submenu method
            self.acter.a_menu.draw(self.screen)
            
            if self.target_menu is not None:
                self.target_menu.draw(self.screen)

        elif self.status_on == True:
            self.clicked_sprite.status_bar((self.clicked_sprite.rect.x -camera_grp.offset.x
                                    ,self.clicked_sprite.rect.y -camera_grp.offset.y),self.screen)      
  
    def targets(self):
        self.target_menu = Menu((self.menu_pos[0]+200,self.menu_pos[1]),'Targets',100,50)

        for sprite in self.in_order:
            if sprite == self.acter:
                pass
            else:
                self.target_menu.add_button(sprite.name)

    def status_bar(self,pos):       
        for sprite in self.in_order:
            if sprite == self.acter:
                pass
            else:
                if sprite.offset_rect.collidepoint(pos):
                    self.status_on = True
                    self.clicked_sprite = sprite

    def collision(self,key):
        for sprite in obstacles.sprites():
            if sprite == self.acter:
                pass
            else:                
                if self.acter.rect.colliderect(sprite.rect):
                    if key == pygame.K_LEFT:
                        self.acter.rect.move_ip(self.acter.size, 0)
                        self.camera_grp.offset.x += self.acter.size
                        self.acter.movement +=1
                    elif key == pygame.K_RIGHT:
                        self.acter.rect.move_ip(-self.acter.size, 0)
                        self.camera_grp.offset.x -= self.acter.size
                        self.acter.movement +=1
                    elif key == pygame.K_UP:
                        self.acter.rect.move_ip(0,self.acter.size)
                        self.camera_grp.offset.y += self.acter.size
                        self.acter.movement +=1
                    elif key == pygame.K_DOWN:
                        self.acter.rect.move_ip(0, -self.acter.size)
                        self.camera_grp.offset.y -= self.acter.size
                        self.acter.movement +=1
                              
    def check_inputs(self,key):
        # handles free roam
        if key == pygame.K_w:
            self.camera_pos[1] -= 200
            self.camera_grp.free_roam(self.camera_pos)            
        elif key == pygame.K_s:            
            self.camera_pos[1] += 200
            self.camera_grp.free_roam(self.camera_pos)
        elif key == pygame.K_d:
           self.camera_pos[0] += 200
           self.camera_grp.free_roam(self.camera_pos) 
        elif key == pygame.K_a:
            self.camera_pos[0] -= 200
            self.camera_grp.free_roam(self.camera_pos)
            

        #acter movement inputs
        if self.acter.movement > 0:
            if key == pygame.K_UP:         
                self.acter.rect.y -= self.acter.size
                self.acter.movement -=1
                self.camera_grp.target_acter(self.acter)
            elif key == pygame.K_DOWN:           
                self.acter.rect.y += self.acter.size
                self.acter.movement -=1
                self.camera_grp.target_acter(self.acter)
            elif key == pygame.K_RIGHT:           
                self.acter.rect.x += self.acter.size
                self.acter.movement -=1
                self.camera_grp.target_acter(self.acter)
            elif key == pygame.K_LEFT:            
                self.acter.rect.x -= self.acter.size
                self.acter.movement -=1
                self.camera_grp.target_acter(self.acter)

        self.acter.action_menu((self.acter.rect.x -camera_grp.offset.x
                                    ,self.acter.rect.y -camera_grp.offset.y))
        
        
 
        # change game mode
        if key == pygame.K_q:
            self.game.switch_mode('bonfire')
            
        # exit with escape
        if key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
  
    def clicks(self,pos):  
        self.status_bar(pos)      
        self.menu_pos = (self.acter.rect.x -camera_grp.offset.x
                                    ,self.acter.rect.y -camera_grp.offset.y)
        
        # the actual acter position
        if self.acter.offset_rect.collidepoint(pos):           
            self.action_menu_on = True     
            # makes the action menu       
            self.acter.action_menu(self.menu_pos)

        # click on attack
        elif self.acter.a_menu.buttons[0].surface.rect.collidepoint(pos):    
            self.targets()    
            roll = self.acter.actions[self.acter.a_menu.buttons[0].text.text]()
            print(roll)
        # click on dash
        elif self.acter.a_menu.buttons[1].surface.rect.collidepoint(pos):
            self.acter.dash()

        else:
            self.action_menu_on = False
            
            

    def end_turn(self):
        self.acter.movement = self.acter.speed
        self.turn = (self.turn+1) % len(self.in_order)
        self.action_menu_on = False  
        self.target_menu = None


    def mouse_down(self,pos):
        if end_turn.rect.collidepoint(pos):
            self.end_turn()
                    
        else:
            self.clicks(pos)
            

    def event_get(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                self.check_inputs(event.key)                
                self.collision(event.key)
            
            if event.type == pygame.MOUSEBUTTONDOWN:               
                self.mouse_down(event.pos)
                                                                      
    def run(self):            
        self.acter= self.in_order[self.turn]    
        
        # checks for pygame.events     
        self.event_get()

        # draws stuff            
        self.camera_grp.custom_draw(self.screen)
        self.button_grp.draw(self.screen)
        
        self.active_menus()
        
        #debug
        debug(f'Turn: {self.turn+1}',(10,10))
        debug(f'Acter : {self.acter}',(10,30))
        debug(f'Movement : {self.acter.movement}',(10,50))
        debug(f'Acter_pos : {self.acter.rect}',(10,70))

