import dice as d


class Weapon:
    
    def __init__(self,name,damage,subtypes,Property,weight=3,magic=False,attunment=False,cost=15):
        
        self.name = name
        self.weight = weight
        self.damage = d.choose_dice(damage)
        self.subtypes = subtypes
        self.Property = Property
        self.magic = magic
        self.attunment = attunment
        self.cost = cost
        
    def __str__(self):
        
        return f'{self.name}'

Property_dict = {0:'ammunition',1:'finesse',2:'heavy',
           3:'light',4:'loading',5:'reach',
           6:'reload',7:'special',8:'thrown',
           9:'two-handed',10:'versitile'}       
weapon_subtypes = (['simple','martial','exotic'],['range','melee','special'])




longbow = Weapon('Longbow',2, (weapon_subtypes[0][1],weapon_subtypes[1][0]),
            (Property_dict[0],Property_dict[2],Property_dict[9]))


dagger = Weapon('Dagger',0, (weapon_subtypes[0][0],weapon_subtypes[1][1]), (Property_dict[1],Property_dict[3],Property_dict[8]))


longsword = Weapon('Longsword', 2,(weapon_subtypes[0][1],weapon_subtypes[1][1]),Property_dict[10])
