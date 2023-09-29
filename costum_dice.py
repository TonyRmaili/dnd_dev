from random import randint


def custom_dice(die_size):
    max_val = die_size
    roll = randint(1,die_size)
    average = (1+max_val)/2

    return [roll,average,max_val]


print(custom_dice(13)[1])


            
            
