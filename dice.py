import random as rn


def roll_d20():   
    d20 = rn.randint(1, 20)   
    return d20

def roll_d12():    
    d12 = rn.randint(1, 12)   
    return d12

def roll_d10():   
    d10 = rn.randint(1, 10)  
    return d10

def roll_d8():  
    d8 = rn.randint(1, 8)   
    return d8

def roll_d6():  
    d6 = rn.randint(1, 6)  
    return d6

def roll_d4():  
    d4 = rn.randint(1, 4)   
    return d4

def roll_d100(): 
    d100 = rn.randint(1, 100) 
    return d100

def choose_dice(die):
    '''Take in number 0-6 to list of dice'''

    dice = [roll_d4(),roll_d6(),roll_d8(),roll_d10(),roll_d12() ,roll_d20() ,roll_d100()]    
    return dice[die]
    
     


def roll_adv(any_dice1,any_dice2):      
    return max(any_dice1, any_dice2)  


def roll_disadv(any_dice1,any_dice2):      
    return min(any_dice1, any_dice2)  


def roll_ability_score():   
    ability = []
    array = []  
    for j in range(6):
    
        for i in range(4):
            x = roll_d6()
            ability.append(x)
            
        ability.remove(min(ability))
        
        y = sum(ability)
        array.append(y)
        ability = []
    
    return array
    
        
    

    








