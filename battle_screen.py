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
        
        
        self.targets = self.monsters.sprites()

    def targets_menu(self):
        functions= {}
        for target in self.targets:
            functions[target.name] = self.acter.roll_attack


        self.t_menu = Menu2((550,HEIGHT-175),'Targets',functions,self.menu_grp)   
        

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
        self.menu_grp = menu_grp
   
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


        # change game mode
        if key == pygame.K_q:
            self.game.switch_mode('bonfire')
            
        # exit with escape
        if key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    
    def end_turn(self):
        self.acter.movement = self.acter.speed
        self.turn = (self.turn+1) % len(self.in_order)
        

    def mouse_down(self,pos):
        
        if end_turn.rect.collidepoint(pos):
            self.acter.action_menu.close()
            self.end_turn()
            
          
        # elif self.acter.offset_rect.collidepoint(pos):
        #     self.acter.action_menu.open_menu()
            
        elif self.acter.action_menu.title.on:
            self.acter.action_menu.click_button(pos)
        
        elif self.t_menu.title.on:
            self.t_menu.click_button(pos)

        # else:
        #     self.acter.action_menu.close_menu()
            

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
        if self.acter in self.monsters:
            self.end_turn() 
        self.acter.action_menu.open()  
        
        # checks for pygame.events     
        self.event_get()

        # draws stuff            
        self.camera_grp.custom_draw(self.screen)
        self.button_grp.draw(self.screen)
        self.menu_grp.custom_draw(self.screen)
        
        
        #debug
        debug(f'Turn: {self.turn+1}',(10,10))
        debug(f'Acter : {self.acter}',(10,30))
        debug(f'Movement : {self.acter.movement}',(10,50))
        debug(f'Acter_pos : {self.acter.rect}',(10,70))
        debug(f'menu_pos : {self.acter.action_menu.pos}',(10,90))
        debug(f'menus : {len(self.menu_grp)}',(10,110))
        