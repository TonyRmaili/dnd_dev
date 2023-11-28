import pygame

class Image(pygame.sprite.Sprite):
    ''' Customizable for sprite groups, anchor point and draw boarder method
        Loads an image'''
    def __init__(self,image,w,h,pos,anchor='topleft',groups=None):
        if groups is not None:
            super().__init__(groups) 
       
        self.w = w
        self.h = h
        self.image = pygame.image.load(image)
        self.image= pygame.transform.scale(self.image,(self.w,self.h))
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, pos)

    def draw_border(self):
        pygame.draw.rect(self.image, 'black', self.image.get_rect(), 2)
       

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Surface(pygame.sprite.Sprite):
    def __init__(self,w,h,pos,anchor='topleft',groups=None):
        if groups is not None:
            super().__init__(groups)
        
        self.w = w
        self.h = h
        self.image = pygame.Surface((self.w,self.h),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        setattr(self.rect, anchor, pos)
    
    def draw_border(self,color,thickness):
        pygame.draw.rect(self.image, color, self.image.get_rect(), thickness)

    def fill_color(self,color):
        self.image.fill(color)
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Text(pygame.sprite.Sprite):
    def __init__(self, text, font_size,pos,anchor='topleft',groups=None):
        if groups is not None:
            super().__init__(groups)

        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.pos = pos
        self.text = text
        self.font_color = 'black'   
        self.rect_anchor = anchor
        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        setattr(self.rect, self.rect_anchor, self.pos)


    def draw(self,screen):
        screen.blit(self.image,self.rect)
         
    def new_text(self,text):
        self.text = text        
        self.image = self.font.render(self.text, True, self.font_color)
    
    def draw_border(self,color,thickness):
        pygame.draw.rect(self.image, color, self.image.get_rect(), thickness)

class Button(pygame.sprite.Sprite):
    def __init__(self, text, surf_w, surf_h,font_size,pos):    
                     
        self.surface = Surface(surf_w,surf_h,pos)
        self.text = Text(text,font_size,pos)
        

    def draw(self,screen):
        self.surface.draw(screen)
        self.text.draw(screen)
   
class Menu:
    def __init__(self,pos,title,w,h):
           
        self.num = 0
        self.buttons = []
        self.w = w
        self.h = h
        self.pos = pos
        self.title = Button(title,w,h,40,pos)
        self.title.text.draw_border('black',2)  
        self.active = False

    def add_button(self,text):       
        button = Button(text,self.w,self.h,40,(self.pos[0],self.pos[1]+50*(self.num+1)))
        self.buttons.append(button)   
        self.num += 1

    def kill_button(self,index):
        self.buttons.pop(index)
        self.num -= 1

    def draw(self,screen):
    
        self.title.draw(screen)
        for button in self.buttons:
            button.draw(screen)
    

# imporved
class TextBtn2:
    def __init__(self,pos,text,font_size):
        pygame.font.init()
        self.text = text     
        self.font_size = font_size
        self.font_color = 'black'
        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        
        # rect
        self.pos = pos 
        self.width = self.image.get_width
        self.height = self.image.get_height
        self.rect = self.image.get_rect(center=self.pos)

        #boarder 
        color = 'black'
        thickness = 2
        pygame.draw.rect(self.image, color, self.image.get_rect(), thickness)
        
        # experiments      
        self.on = True


    def draw(self,screen):
        if self.on:
            color = 'black'
            thickness = 2
            pygame.draw.rect(self.image, color, self.image.get_rect(), thickness)

            screen.blit(self.image,self.rect)

    def new_text(self,new_text):
        self.text = new_text     
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        
    

class Menu2(pygame.sprite.Sprite):
    def __init__(self,pos,title,functions,group):
        super().__init__(group)
        self.pos = pos
        self.title = TextBtn2(pos,title,40)
        self.num = 1
        self.buttons = []
        
        self.functions = functions
        
        for text in self.functions.keys():
            self.add_button(text)
              
        # original menu
        self.og_menu = self


    def add_button(self,text):
        self.pos_adj = (self.pos[0], self.pos[1] + self.title.height()*self.num)
        button = TextBtn2(self.pos_adj,text,40)
        self.buttons.append(button)
        self.num += 1

    def draw(self,screen):      
        self.title.draw(screen)
        for button in self.buttons:           
            button.draw(screen)

    def close(self):
        self.title.on = False
        for button in self.buttons:
            button.on = False

    def open(self):
        self.title.on = True
        for button in self.buttons:
            button.on = True

    def new_menu(self,pos,title,functions):
        self.pos = pos
        self.title = TextBtn2(pos,title,40)
        self.num = 1
        self.buttons = []
        
        self.functions = functions
        
        for text in self.functions.keys():
            self.add_button(text)
        
        menu_grp.add(self)

    def click_button(self,pos,):
        for button in self.buttons: 
            if button.rect.collidepoint(pos) and button.on and self.functions[button.text] is not None:
                
                self.functions[button.text]()
                     




class MenuGrp(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def custom_draw(self,screen):   
         for menu in self.sprites():           
            menu.draw(screen)

    def clicked(self,pos):
        for menu in self.sprites():   
            menu.click_button(pos)

menu_grp = MenuGrp()


