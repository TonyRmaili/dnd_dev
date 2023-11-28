
def backgrounds(char,choice):

    if choice == 'soldier':
        bg_soldier(char)
    if choice == 'sage':
        bg_sage(char)
        
            
def bg_soldier(char):
    
   
    char.proficiencies['Skills'] = ['Intimidation','Athletics']
    char.proficiencies['Tools'] = ['Vehicles','Chess']
    

def bg_sage(char):
    
    char.proficiencies['Skills'] = ['Arcana','History']
    
     
    
