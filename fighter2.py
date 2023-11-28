

class Fighter:
    def __init__(self,lvl,char):
        self.char = char
        self.lvl = lvl

    
    def level1(self):
        # set starting profs
        self.char.proficiencies.weapons.append('simple')
        self.char.proficiencies.weapons.append('martial')

        self.char.proficiencies.armors.append('light')
        self.char.proficiencies.armors.append('medium')
        self.char.proficiencies.armors.append('heavy')

        self.char.proficiencies.skills.append('AnimalHandling')
        self.char.proficiencies.skills.append('Perception')
        
        # increase max lvl
        self.char.max_lvl += 1

        # if starting class is fighter
        if self.char.max_lvl == 1:
            self.max_hp += 10 + self.char.con
            self.proficiencies.stre = True
            self.proficiencies.con = True



    def level2(self):
        self.char.max_lvl += 1

        self.char.max_hp += 6 + self.char.con

    def level3(self):
        self.char.max_lvl += 1

        self.char.max_hp += 6 + self.char.con


    