

class BackGrounds:
    def __init__(self,background,char):
        self.char = char
        self.background = background       

    def __str__(self):
        return f'{self.background}'
    
    def soldier(self):         
        self.char.proficiencies.skills.append('Intimidation')
        self.char.proficiencies.skills.append('Athletics')

        self.char.proficiencies.tools.append('Vehicles')
        self.char.proficiencies.tools.append('Chess')
    
    def sage(self):
        self.char.proficiencies.skills.append('Arcana')
        self.char.proficiencies.skills.append('History')
        
    def selection(self):
        if self.background == 'soldier':
            self.soldier()
        elif self.background == 'sage':
            self.sage()