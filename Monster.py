
import Items as Items
import character as c3
import random as rn

class Monster(c3.Character):
    
    def __init__(self,name,max_hp,armor,wpn,stre,dex,con,inte,wis,cha,speed,color):
        super().__init__()
        self.name = name
        self.monster_type = ''
        self.CR = 0
        self.max_hp = max_hp
        self.equiped['Body'] = armor
        self.equiped['Hands'] = wpn
        del self.race
        del self.background
        self.stre = stre
        self.dex = dex
        self.con = con
        self.inte = inte
        self.wis = wis
        self.cha = cha
        self.speed = speed
        self.color= color
        
    def blit_me(self):
        self.x = rn.randint(0, 14)*50
        self.y = rn.randint(0, 14)*50
        self.square = 50
       
        
        
        