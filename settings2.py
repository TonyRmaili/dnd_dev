import pygame, os
from tile2 import *
from camera_group import CameraGroup
from char3 import Character


WIDTH = 1200
HEIGHT = 900
FPS = 30
BLOCK_SIZE = 50

pic_path = './Pygame/D4/pics/'

# battle groups
players = pygame.sprite.Group()
monsters = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
camera_grp = CameraGroup()
button_grp = pygame.sprite.Group()


# bonfire groups
bonfire_grp = pygame.sprite.Group()

# creation groups
party_grp = pygame.sprite.Group()
selection_grp = pygame.sprite.Group()
ability_grp = pygame.sprite.Group()
race_grp = pygame.sprite.Group()
background_grp = pygame.sprite.Group()
class_grp = pygame.sprite.Group()
token_grp = pygame.sprite.Group()

# Party Size Settings
party_box = Text('Select Party Size',50,(WIDTH//2,150),groups=party_grp,anchor='center')
party_num_box = Text('1',75,(WIDTH//2,200),groups=party_grp,anchor='center')  
party_num_box.draw_border('black',2)     
plus_box = Image(pic_path+'plus.jpg',40,40,(WIDTH//2+75,200),groups=party_grp,anchor='center')
minus_box = Image(pic_path+'minus.jpg',40,40,(WIDTH//2-75,200),groups=party_grp,anchor='center')

# Selection Panel 

ability_box = Text('Ability Score',40,(75,100),groups=selection_grp)
race_box = Text('Race',40,(300,100),groups=selection_grp)
background_box = Text('Background',40,(450,100),groups=selection_grp)
class_box = Text('Class',40,(700,100),groups=selection_grp)
token_box = Text('Token',40,(900,100),groups=selection_grp)
name_box = Text('Enter Name',40,(WIDTH//2,150),groups=selection_grp,anchor='center')


# Ability scores 
stre_box = Text('Strength',40,(WIDTH//2,250),anchor='center',groups=ability_grp)
dex_box = Text('Dexterity',40,(WIDTH//2,300),anchor='center',groups=ability_grp)
con_box = Text('Constitution',40,(WIDTH//2,350),anchor='center',groups=ability_grp)
inte_box = Text('Inteligence',40,(WIDTH//2,400),anchor='center',groups=ability_grp)
wis_box = Text('Wisdom',40,(WIDTH//2,450),anchor='center',groups=ability_grp)
cha_box = Text('Charisma',40,(WIDTH//2,500),anchor='center',groups=ability_grp)

    # plus signs
plus_list =[]
for i in range(6):
    
    plus = Image(pic_path+'plus.jpg',30,30,(WIDTH//2+110,250+(i*50)),groups=ability_grp,anchor='center')
    plus_list.append(plus)

    # minus signs
minus_list =[]
for i in range(6):
    
    minus = Image(pic_path+'minus.jpg',30,30,(WIDTH//2-110,250+(i*50)),groups=ability_grp,anchor='center')
    minus_list.append(minus)

    # ability numbers
ability_list =[]
abs_score = []
for i in range(6):
    score = 8
    ability = Text(str(score),40,(WIDTH//2+175,250+(i*50)),anchor='center',groups=ability_grp)
    ability_list.append(ability)
    abs_score.append(score)


# Races

human_box = Text('Human',40,(WIDTH//2,250),groups=race_grp)
dwarf_box = Text('Dwarf',40,(WIDTH//2,350),groups=race_grp)
elf_box = Text('Elf',40,(WIDTH//2,450),groups=race_grp)


# Backgrounds 

soldier_box = Text('Soldier',40,(WIDTH//2,250),groups=background_grp)
sage_box = Text('Sage',40,(WIDTH//2,350),groups=background_grp)

# Classes

fighter_box = Text('Fighter',40,(WIDTH//2,250),groups=class_grp)
wizard_box = Text('Wizard',40,(WIDTH//2,350),groups=class_grp)



# Tokens

image_folder = './Pygame/D4/player_tokens/'
images = []
token_count = 0
for file_name in os.listdir(image_folder):
    # if file_name.endswith(".jpg"):               
    image_path = os.path.join(image_folder, file_name)
    image= Image(image_path,50,50,(WIDTH//2,250+token_count),anchor='center',groups=token_grp)
    token_count += 60
    images.append((image_path,image))


# temp. dungeon
forest_tile = Image(pic_path+'forest.jpg',WIDTH,HEIGHT,(0,0),groups=camera_grp)

rock = Image(pic_path+'rock.png',50,50,(300,300),groups=[obstacles,camera_grp])

wall1 = Surface(20,HEIGHT,(20,0),groups=[obstacles,camera_grp])
wall1.fill_color('black')

wall2 = Surface(WIDTH,20,(20,HEIGHT),groups=[obstacles,camera_grp])
wall2.fill_color('black')

wall3 = Surface(20 ,HEIGHT, (WIDTH, 0 ),groups=[obstacles,camera_grp])
wall3.fill_color('black')

info_panel = Surface(WIDTH,200,(0,  HEIGHT -200),groups=[button_grp])
info_panel.fill_color('grey')

end_turn = Text('End Turn',30,(WIDTH-200,HEIGHT-100),groups=button_grp)
end_turn.draw_border('black',2)


# characters
amenu_pos = (400,HEIGHT-175)
test_pc = Character('garry','human','soldier',
                    10,10,10,10,10,10,
                    [camera_grp,obstacles,players])
test_pc.size = 50
test_pc.speed = 100
test_pc.movement = test_pc.speed
test_pc.load_image(pic_path+'garry.jpg',(500,500),amenu_pos)




test_pc2 = Character('theo','human','soldier',
                    10,10,10,10,10,10,
                    [camera_grp,obstacles,players])
test_pc2.size = 50
test_pc2.speed = 100
test_pc2.movement = test_pc.speed
test_pc2.load_image(pic_path+'theo.jpg',(700,500),amenu_pos)



test_pc3 = Character('arnold','human','soldier',
                    10,10,10,10,10,10,
                    [camera_grp,obstacles,players])
test_pc3.size = 50
test_pc3.speed = 100
test_pc3.movement = test_pc.speed
test_pc3.actions['Cast Spell'] = None
test_pc3.load_image(pic_path+'arnold.jpg',(800,500),amenu_pos)

orc = Character('orc','human','soldier',
                    10,10,10,10,10,10,
                    [camera_grp,obstacles,monsters])
orc.size = 50
orc.speed = 100
orc.movement = test_pc.speed
orc.load_image(pic_path+'orc.jpg',(900,500),amenu_pos)

