def races(char,choice):       
    if choice == 'human':
        rc_human(char)
    if choice == 'elf':
        rc_elf(char)
    if choice == 'dwarf':
        rc_dwarf(char)

     

def rc_human(char):    
    char.speed = 6
    char.movement = char.speed
    char.size = 50
    
    char.stre += 1
    char.dex += 1
    char.con += 1
    char.inte += 1
    char.wis += 1
    char.cha += 1
    
def rc_elf(char):  
    char.speed = 6
    char.movement = char.speed
    char.size = 50

    char.dex += 2
   
def rc_dwarf(char):    
    char.speed = 5
    char.movement = char.speed
    char.size = 50
    
    char.con += 2



