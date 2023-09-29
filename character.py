


class Character:
    def __init__(self,name,race,background):
        self.name= name
        self.race = race
        self.background = background
        self.classes = []
        self.max_hp = 0
        self.ac = 10
        self.movement = 30
        self.jump_distance = 0

    def change_max_hp(self,new_hp):
        self.max_hp = new_hp
        return new_hp

    def alter_spell_slot(self):
        pass

    def short_rest(self):
        pass

    def long_rest(self):
        pass

    def spell_slots(self):
        pass



def display_character(character):
    print(character.name)
    print(character.background)
    print(character.race)
