import dice as d
from Items import *
import races as r
import fighter as f
import wizard as w
import backgrounds as b
import Skills as sk
import pygame
from tile2 import *

class Character(pygame.sprite.Sprite):          
    def __init__(self,name,race,background,stre,dex,con,inte,wis,cha,groups):
        super().__init__(groups)
        self.name = name
        self.stre= stre
        self.dex= dex
        self.con= con
        self.inte= inte
        self.wis= wis
        self.cha= cha        
        self.race = race
        self.speed = 0
        self.movement = self.speed
        self.size = 0
        self.background = background
           
        self.class_lvls = [0,0]     
        self.max_hp = 0
        self.wound = 0
        self.proficiencies = {'Saves':[0,0,0,0,0,0],'Skills':[],'Weapon':[],'Armor':[]}    
        self.inventory = []
        self.equiped = {'Head':None,'Neck':None,'Body':None,'Hands':None,
                        'Feet':None,'Finger':None,'Back':None}       
        self.powers = {'Fighter':[],'Wizard':[]}
    
        self.actions = {'Attack':self.roll_attack,'Dash':None, 'Dodge':None}
        self.bonus_actions = {}
        self.grp = groups   # access groups
        self.offset_pos = (0,0)
        self.offset_rect = pygame.rect.Rect(self.offset_pos[0],
                                    self.offset_pos[1],
                                    self.size,self.size)

        self.a_menu_on = False
        self.b_menu_on = False
        


    def action_menu(self,pos):
        self.a_menu = Menu((pos[0]+75,pos[1]),'Actions',75,40)      
        for key in self.actions.keys():
            self.a_menu.add_button(key)
    


    def status_bar(self,pos,screen):       
        status = Menu((pos[0]+75,pos[1]),'Status',50,25)
        status.add_button(self.name)
        status.add_button(str(self.max_hp))
        ac = self.AC()
        status.add_button(str(ac))
       
        status.draw(screen) 
       
    def dash(self):
        self.movement += self.speed

    def draw_menu(self,screen):
        self.a_menu.draw(screen)

    def load_image(self,image,pos):
        self.image= pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect= self.image.get_rect(topleft=pos)

           
    def __str__(self):
        return f'{self.name}'
        
    def lvl(self):
        return sum(self.class_lvls)
    
    # outdated
    def lvlup(self):
        class_options = {0: f.fighter, 1:w.wizard}
        class_names = {0: 'fighter', 1:'wizard'}
        print('Choose a class:')
        for x, c in class_names.items():
            print(f'{x}: {c}')
        choice = int(input())
        if choice in class_options:
            class_options[choice](self)
        else:
            print('Invalid choice')

    def ability_score(self):
        return [self.stre,self.dex,self.con,self.inte,self.wis,self.cha]
    
    def saving_throws(self):
      
        for x in range(len(self.proficiencies['Saves'])):
            if self.proficiencies['Saves'][x] != 0:                
                self.proficiencies['Saves'][x] = self.PB()
        return [sum(q) for q in zip(self.ability_mod(),self.proficiencies['Saves'])]  
              
    def PB(self):                         
        if self.lvl() <= 4:
            return 2  
        if self.lvl() >= 5 and self.lvl() <= 8:
            return 3       
        if self.lvl() >= 9 and self.lvl() <= 12:
            return 4      
        if self.lvl() >= 13 and self.lvl() <= 16:
            return 5         
        if self.lvl() >= 17 and self.lvl() <= 20:
            return 6
          
    def AC(self):
        if self.equiped['Body'] == None:          
            return 10 + self.ability_mod()[1]
        else:
            if self.equiped['Body'].Type == 'light':
                return self.equiped['Body'].subtype[1] + self.ability_mod()[1]           
            elif self.equiped['Body'].Type == 'medium':
                if self.ability_mod()[1] > 2:               
                    return self.equiped['Body'].subtype[1] + 2
                else:
                    return self.equiped['Body'].subtype[1] + self.ability_mod()[1]                  
            elif self.equiped['Body'].Type == 'heavy':
               return self.equiped['Body'].subtype[1]
     
    def ability_mod(self):
        ab_mod = []
        for stat in self.ability_score():
            if stat >= 10:
                stat = int((stat-10)/2)
                ab_mod.append(stat)            
            elif stat < 10:
                stat = int((stat-10)/2 -0.5)
                ab_mod.append(stat)         
        return ab_mod

    def roll_check(self,ability):
        return d.roll_d20() + self.ability_mod()[ability]
        
    def roll_save(self,ability):       
        return d.roll_d20() + self.saving_throws()[ability]
                   
    def roll_skill(self,ability,skill):
        
        if sk.Skills[ability][skill] in self.proficiencies['Skills']:
            return d.roll_d20() + self.ability_mod()[ability] + self.PB()
        else:
            return d.roll_d20() + self.ability_mod()[ability] 
    
    def roll_attack(self):
        x = d.roll_d20()
        if self.equiped['Hands'] == None:
            return x + self.ability_mod()[0] + self.PB()
        
        elif self.equiped['Hands'].subtypes[0] in self.proficiencies['Weapon']:
            if self.equiped['Hands'].subtypes[1] == 'melee':
                return x + self.ability_mod()[0] + self.PB()
            elif self.equiped['Hands'].subtypes[1] == 'ranged':
                return x + self.ability_mod()[1] + self.PB()
        else:
            if self.equiped['Hands'].subtypes[1] == 'melee':
                return x + self.ability_mod()[0] 
            elif self.equiped['Hands'].subtypes[1] == 'ranged':
                return x + self.ability_mod()[1] 
            
    def roll_damage(self):
        if self.equiped['Hands'] == None:
            return self.ability_mod()[0]
        else:
            if self.equiped['Hands'].subtypes[1] == 'melee':
                return self.equiped['Hands'].damage + self.ability_mod()[0]
            elif self.equiped['Hands'].subtypes[1] == 'ranged':
                return self.equiped['Hands'].damage + self.ability_mod()[1]


def view_char(char):   
    print('Name-------',char.name)
    print('Race-------',char.race)
    print('Background-',char.background)
    print('Class lvls--------',char.class_lvls)
    print('Total lvls--------',char.lvl())
    print('Proficiency bonus-',char.PB())
    print('Max Hp:-----------',char.max_hp)
    print('Armor Class-------',char.AC())
    print('Ability Scores    ',char.ability_score())
    
    print('Ability modifiers ',char.ability_mod())   
    print('Saving Throws     ',char.saving_throws())   
    
    print('Proficiencies:     ',char.proficiencies)



