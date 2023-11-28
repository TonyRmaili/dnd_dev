def wizard1(char):
               
    char.class_lvls[1] += 1
    
  
    if char.lvl() == 1:
        char.max_hp += 6 + char.ability_mod()[2]
        char.proficiencies['Saves'] = [0,0,0,char.PB(),char.PB(),0]
     
    else:
        char.max_hp += 4 + char.ability_mod()[2]
        
    char.proficiencies['Skills'].append('Religion')
    char.proficiencies['Skills'].append('Insight')

def wizard2(char):
    char.class_lvls[1] += 1
    char.max_hp += 4 + char.ability_mod()[2]
    

def wizard3(char):
    
    char.class_lvls[1] += 1
    char.max_hp += 4 + char.ability_mod()[2]
    

def wizard(char):
    
    if char.class_lvls[1] == 0:
        wizard1(char)
        
    elif char.class_lvls[1] == 1:
        wizard2(char)
        
    elif char.class_lvls[1] == 2:
        wizard3(char)
        
