

class Races:
    def __init__(self,race,char):
        self.char = char
        self.race = race       

    def __str__(self):
        return self.race
    
    def human(self):
        self.char.speed = 6
        self.char.size = 50

        self.char.stre += 1
        self.char.dex += 1
        self.char.con += 1
        self.char.inte += 1
        self.char.wis += 1
        self.char.cha += 1       


    def dwarf(self):
        self.char.speed = 5
        self.char.size = 50
               
        self.char.con += 2
        
    def elf(self):
        self.char.speed = 6
        self.char.size = 50

        self.char.dex += 2
        
    def selection(self):
        if self.race == 'human':
            self.human()
        elif self.race == 'dwarf':
            self.dwarf()
        elif self.race == 'elf':
            self.elf

