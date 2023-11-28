import item_data as i
import dice as d

class Item:
    
    def __init__(self,name,rarity,cost):
        self.name = name
        self.rarity = i.rarity_dict[rarity]
        self.cost = cost
        
        self.weight = 0
        self.discription = 'Insert text here'
        self.attunment = False
        self.magic = False
        
  
    def __str__(self):
        
        return f'{self.name}'

  
class Weapon(Item):
    
    def __init__(self,name,rarity,cost,damage,subtypes,Property):
        super().__init__(name,rarity,cost)
        self.damage = d.choose_dice(damage)
        self.subtypes = subtypes
        self.Property = Property

class Armor(Item):
    
    def __init__(self,name,rarity,cost,Type,subtype):
        super().__init__(name,rarity,cost)
        self.Type = i.Armors[Type][0]
        self.subtype = i.Armors[Type][1][subtype]
        



hf = Armor('Half-plate', 0, 750, 1, 4)
studded = Armor('Studded-leather', 0, 25, 0, 2)
plate = Armor('Plate', 0, 1500, 2, 3)
hide = Armor('Hide', 0, 0, 1, 0)

ls = Weapon('Longsword', 0, 15, 2, (i.w_subtypes[0][1],i.w_subtypes[1][1]), i.weapon_properties[10])
lb = Weapon('longbow', 0, 2, 2, (i.w_subtypes[0][1],i.w_subtypes[1][0]), i.weapon_properties[0])
gr_axe = Weapon('Greataxe', 0, 0, 4, (i.w_subtypes[0][1],i.w_subtypes[1][1]), i.weapon_properties[9])

armors = [hf,studded,plate]
wpns = [ls,lb]








