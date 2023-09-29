from random import randint

class Dice:

    def __init__(self):
        pass
    
    def roll_d4(self):
        max_val = 4
        average = (1+max_val)/2
        d4 = randint(1, 4)   

        return [d4,max_val,average]
    
    def roll_d6(self):  
        d6 = randint(1, 6)  
        return d6

    def roll_d8(self):  
        d8 = randint(1, 8)   
        return d8

    
    def roll_d10(self):   
        d10 = randint(1, 10)  
        return d10


    def roll_d12(self):    
        d12 = randint(1, 12)   
        return d12

    def roll_d20(self):   
        max_val = 20
        d20 = randint(1, 20)   
        return d20,max_val
    
    def roll_d100(self): 
        d100 = randint(1, 100) 
        return d100

    def choose_dice(self, die):
        '''Take in number 0-6 to list of dice'''

        dice = [self.roll_d4(),self.roll_d6(),self.roll_d8(),self.roll_d10(),self.roll_d12() ,self.roll_d20() ,self.roll_d100()]    
        return dice[die]
        

    def roll_adv(self,any_dice1,any_dice2):      
        return max(any_dice1, any_dice2)  

    def roll_disadv(self,any_dice1,any_dice2):      
        return min(any_dice1, any_dice2)  


    def roll_many_dice(self,amount,modifier,dice_roll):
        '''Pass in dice_roll function '''

        all_rolls = []
        for _ in range(amount):
            roll = dice_roll() + modifier
            all_rolls.append(roll)
        total_roll = sum(all_rolls)
        return total_roll
    
    def many_attack_rolls(self,amount,modifier,target_number=15):

        hit_count = 0
        miss_count = 0
        crit_hit = 0
        crit_miss = 0
        for i in range(amount):
            roll = dice_roll()
            max_roll = roll[1]
            rolled = roll[0]

            if rolled == max_roll:
                crit_hit +=1
                print('critical hit!')
            
            elif rolled == 1:
                crit_miss += 1
                print('critical miss')

            elif rolled + modifier >= target_number:
                print('hit')
                hit_count += 1
            else:
                miss_count += 1
                print('miss')

        return hit_count,crit_hit,miss_count,crit_miss         
    
    def big_damage_calc(self,d4_set=(0,0),d6_set=(0,0),
                        d8_set=(0,0),d10_set=(0,0),
                        d12_set=(0,0),d20_set=(0,0)):
        rolls =[]
        dice_sets = [(d4_set,roll_d4),(d6_set,roll_d6),(d8_set,roll_d8),(d10_set,roll_d10),(d12_set,roll_d12),(d20_set,roll_d20)]
        for set in dice_sets:
            if set[0][0] == 0:
                pass
                
            else:
                
                set_roll = self.roll_many_dice(set[0][0],set[0][1],set[1])
                rolls.append(set_roll)

        rolls = sum(rolls)
        return rolls


   

d1 = Dice()

print(d1.roll_d4())







