import dice as d

def fighter1(char):
               
    char.class_lvls[0] += 1
    
    char.proficiencies['Weapon']= ['simple','martial']
    char.proficiencies['Armor']= ['light','medium','heavy']
    char.proficiencies['Skills'].append('AnimalHandling')
    char.proficiencies['Skills'].append('Perception')
    
       
    if char.lvl() == 1:
        char.max_hp += 10 + char.ability_mod()[2]
        char.proficiencies['Saves']= [char.PB(),0,char.PB(),0,0,0]
        
    else:
        char.max_hp += 6 + char.ability_mod()[2] 
    

def fighter2(char):
    char.class_lvls[0] += 1
    char.max_hp += 6 + char.ability_mod()[2]
    

def fighter3(char):
    
    char.class_lvls[0] += 1
    char.max_hp += 6 + char.ability_mod()[2]
    

def fighter(char):
    
    if char.class_lvls[0] == 0:
        fighter1(char)
        
    elif char.class_lvls[0] == 1:
        fighter2(char)
        
    elif char.class_lvls[0] == 2:
        fighter3(char)
        
