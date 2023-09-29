from random import randint

class Dice:
    def __init__(self):

        # bad 
        self.d4 = self.roll_d4
        self.d6 = 6
        self.d8 = 8
        self.d10 = 10
        self.d12 = 12
        self.d20 = 20
        self.d100 = 100

        self.dice_types = [self.d4,self.d6,self.d8,
                           self.d10,self.d12,self.d20,self.d100]
        
  
    def roll_d4(self,adv = False, dis_adv= False):
        max_val = 4
        average = (1+max_val)/2

        if adv == False and dis_adv == False:
            roll = randint(1, max_val)
        
        elif adv is not False:           
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
         
        elif dis_adv is not False:
            
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)

        return [roll,max_val,average]
    
    def roll_d6(self,adv = False, dis_adv= False):  
        max_val = 6
        average = (1+max_val)/2
        if adv == False and dis_adv == False:
            roll = randint(1, max_val)

        elif adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
        
        elif dis_adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)
        
        return [roll,max_val,average]

    def roll_d8(self,adv = False, dis_adv= False):  
        max_val = 8
        average = (1+max_val)/2

        if adv == False and dis_adv == False:
            roll = randint(1, max_val)

        if adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
        
        elif dis_adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)
        
        return [roll,max_val,average]  

    def roll_d10(self,adv = False, dis_adv= False):   
        max_val = 10
        average = (1+max_val)/2
        if adv == False and dis_adv == False:
            roll = randint(1, max_val)

        if adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
        
        elif dis_adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)
        
        return [roll,max_val,average]
    
    def roll_d12(self,adv = False, dis_adv= False):    
        max_val = 12
        average = (1+max_val)/2

        if adv == False and dis_adv == False:
            roll = randint(1, max_val)
        if adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
        
        elif dis_adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)
        
        return [roll,max_val,average]

    def roll_d20(self,adv = False, dis_adv= False):   
        max_val = 20
        average = (1+max_val)/2
        if adv == False and dis_adv == False:
            roll = randint(1, max_val)

        if adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
        
        elif dis_adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)
        
        return [roll,max_val,average]
    
    def roll_d100(self,adv = False, dis_adv= False): 
        max_val = 100
        average = (1+max_val)/2
        if adv == False and dis_adv == False:
            roll = randint(1, max_val)

        if adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= max(roll1,roll2)
        
        elif dis_adv is not False:
            roll1 = randint(1, max_val)
            roll2 = randint(1, max_val)
            roll= min(roll1,roll2)
        
        return [roll,max_val,average]


d1 = Dice()


