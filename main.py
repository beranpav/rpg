import pygame
from pygame.locals import *
import numpy as np
import imageio
import random

from monsters import *
from control_functions import *

pygame.init()

"""
########################################################
            !!! variable definitions !!!
########################################################
"""
BLACK = (0,0,0)
WHITE = (255,255,255)

display_width = 1400
display_height = 800

screen = pygame.display.set_mode([display_width,display_height])

pygame.display.set_caption('The Quest')
clock = pygame.time.Clock()

step_range = 4
look_range = 32
monster_range = 16

error_text_font = pygame.font.Font(None, 24)
error_text_color = (0,0,255)
error_box = pygame.Rect(450, 710, 300, 27)

in_text_font = pygame.font.Font(None, 24)
in_text_color = (255,0,0)
in_text = ""
input_box = pygame.Rect(33, 760, 1100, 27)

output_box = pygame.Rect(12, 612, 1100, 135)
out_text_color = (0,255,0)
out_text_font = pygame.font.Font(None, 30)

inventory_img = pygame.image.load('data/inventory.png')
bottom_img = pygame.image.load('data/bottom.png')
player_img = pygame.image.load('data/player.png')
loading_img = pygame.image.load('data/loading.png')

start_img = pygame.image.load('data/start.png')

wife_en_img = pygame.image.load('data/wife_en.png')
cool_truth_img = pygame.image.load('data/cool_truth.png')
uncool_truth_img = pygame.image.load('data/uncool_truth.png')
cool_lie_img = pygame.image.load('data/cool_lie.png')
uncool_lie_img = pygame.image.load('data/uncool_lie.png')
cyclops_end_img = pygame.image.load('data/cyclops_end.png')
elf_end_img = pygame.image.load('data/elf_end.png')
health_end_img = pygame.image.load('data/health_end.png')
rabbit_end_img = pygame.image.load('data/rabbit_end.png')
witch_end_img = pygame.image.load('data/witch_end.png')
simple_end_img = pygame.image.load('data/simple_end.png')
"""
########################################################
            !!! functions i want soon !!!
########################################################
"""
def get_input():
    input_given = ''
    given = False
    while not given:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_given
                    given = True
                elif event.key == pygame.K_BACKSPACE:
                    input_given = input_given[:-1]
                else:
                    input_given += event.unicode

        input_given_text_surface = in_text_font.render(input_given, True, in_text_color)
        pygame.draw.rect(screen, BLACK, input_box)
        screen.blit(input_given_text_surface, (input_box.left + 1, input_box.top + 6))
        pygame.display.update()

def draw_wronginput():
    error_msg = 'wrong input, try again'

    error_text_surface = error_text_font.render(error_msg, True, error_text_color)
    pygame.draw.rect(screen, WHITE, error_box)
    screen.blit(error_text_surface, (error_box.left + 4, error_box.top + 4))
    pygame.display.update()

def draw_spacebartocontinue(event_type):
    if event_type == 'continue':
        error_msg = 'press spacebar to continue'
    elif event_type == 'end':
        error_msg = 'press spacebar to end it'

    error_text_surface = error_text_font.render(error_msg, True, error_text_color)
    pygame.draw.rect(screen, WHITE, error_box)
    screen.blit(error_text_surface, (error_box.left + 4, error_box.top + 4))
    pygame.display.update()

    spaced = False
    while not spaced:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spaced = True
"""
########################################################
            !!! start !!!
########################################################
"""
screen.blit(start_img,(0,0))
screen.blit(bottom_img,(0,600))
screen.blit(inventory_img,(1200,0))
pygame.display.update()

person_name = get_input()

"""
########################################################
            !!! load and remade map to matrix !!!
########################################################
"""
pygame.draw.rect(screen, BLACK, input_box)
screen.blit(loading_img,(0,0))
pygame.display.update()

load_map = imageio.imread('data/map.png')
load_map = np.array(load_map)
c_map = np.transpose(load_map,(1,0,2))
map_size_x = c_map.shape[0]
map_size_y = c_map.shape[1]

grey_shade = 183
display_map = np.ones((map_size_x,map_size_y,3))*grey_shade

tmap = np.dtype([("ground",np.integer),("monster",np.integer),("inventory",np.integer)])
info_map = np.zeros((map_size_x,map_size_y), dtype = tmap)

#function taking matrix with colors and put information about ground into info_map matrix
def redo_map(color_map,empty_matrix):
    for i in range(0,map_size_x - 1):
        for j in range(0,map_size_y - 1):
            if color_map[i,j,1] == 143:
                empty_matrix[i,j]["ground"] = 1 #water
            elif color_map[i,j,1] == 82:
                empty_matrix[i,j]["ground"] = 1 #water
            elif color_map[i,j,1] == 244:
                empty_matrix[i,j]["ground"] = 2 #groud
            elif color_map[i,j,1] == 66:
                empty_matrix[i,j]["ground"] = 2 #groud
            elif color_map[i,j,1] == 47:
                empty_matrix[i,j]["ground"] = 2 #groud
            elif color_map[i,j,1] == 135:
                empty_matrix[i,j]["ground"] = 2 #groud
            elif color_map[i,j,1] == 164:
                empty_matrix[i,j]["ground"] = 2 #groud
            elif color_map[i,j,1] == 188:
                empty_matrix[i,j]["ground"] = 3 #field
            elif color_map[i,j,1] == 159:
                empty_matrix[i,j]["ground"] = 3 #field
            elif color_map[i,j,1] == 100:
                empty_matrix[i,j]["ground"] = 4 #forest
            elif color_map[i,j,1] == 71:
                empty_matrix[i,j]["ground"] = 4 #forest
            elif color_map[i,j,1] == 60:
                empty_matrix[i,j]["ground"] = 4 #forest
            elif color_map[i,j,1] == 95:
                empty_matrix[i,j]["ground"] = 4 #forest
            elif color_map[i,j,1] == 152:
                empty_matrix[i,j]["ground"] = 5 #rock
            elif color_map[i,j,1] == 102:
                empty_matrix[i,j]["ground"] = 5 #rock
            elif color_map[i,j,1] == 25:
                empty_matrix[i,j]["ground"] = 5 #rock
            elif color_map[i,j,1] == 147:
                empty_matrix[i,j]["ground"] = 6 #road
            elif color_map[i,j,1] == 60:
                empty_matrix[i,j]["ground"] = 6 #road
            elif color_map[i,j,1] == 116:
                empty_matrix[i,j]["ground"] = 6 #road
            elif color_map[i,j,1] == 11:
                start_x = i
                start_y = j
            elif color_map[i,j,1] == 114:
                empty_matrix[i,j]["ground"] = 10 #wife
            elif color_map[i,j,1] == 9:
                empty_matrix[i,j]["monster"] = 12 #witch
                print("carodejnice")

    new_map = empty_matrix
    return new_map, start_x, start_y

info_map, person_x, person_y = redo_map(c_map,info_map)

#put monster in map
def put_monstrer(map, clear_range, number_of_monsters, monster_id, forbidden_places):
    for n in range(number_of_monsters):
        put = False
        while put == False:
            unusable = False
            rand_x = random.randint(0,map_size_x - 1)
            rand_y = random.randint(0,map_size_y - 1)
            for f in forbidden_places:
                if map[rand_x,rand_y]["ground"] == f:
                    unusable = True
            if not unusable:
                if map[rand_x,rand_y]["monster"] == 0:
                    monster_around = False
                    for i in range(rand_x - clear_range, rand_x - clear_range + 1):
                        for j in range(rand_y - clear_range, rand_y - clear_range + 1):
                            if i >= 0 and i < map_size_x and j >= 0 and j < map_size_y:
                                if map[i,j]["monster"] > 0:
                                    monster_around = True
                    if monster_around == False:
                        map[rand_x,rand_y]["monster"] = monster_id
                        put = True

#puts monsters randomly on map
def random_encounters(map):
    num_of_rabbits = 80
    num_of_spiders = 80
    num_of_wolfs = 40
    num_of_goblins = 30
    num_of_deers = 60
    num_of_golems = 20
    num_of_cyclopses = 7
    num_of_elfs = 2
    num_of_salmons = 60
    num_of_zombierabbits = 15
    num_of_magicrabbits = 2

    forbidden_rabbits = [0,1,5,6,10]
    forbidden_spiders = [0,1,2,6,10]
    forbidden_wolfs = [0,1,6,10]
    forbidden_goblins = [0,1,10]
    forbidden_deers = [0,1,2,5,6,10]
    forbidden_golems = [0,1,2,3,4,6,10]
    forbidden_cyclopses = [0,1,2,3,4,5,10]
    forbidden_elfs = [0,1,10]
    forbidden_salmons = [0,2,3,4,5,6,10]
    forbidden_zombierabbits = [0,1,5,6,10]
    forbidden_magicrabbits = [0,1,5,6,10]

    #changed order so that it is slightly less likely for the rare monsters to be next to each other
    #last number = 12
    put_monstrer(map, monster_range, num_of_magicrabbits, 11, forbidden_magicrabbits)
    put_monstrer(map, monster_range, num_of_elfs, 8, forbidden_elfs)
    put_monstrer(map, monster_range * 3, num_of_cyclopses, 7, forbidden_cyclopses)
    put_monstrer(map, monster_range, num_of_zombierabbits, 10, forbidden_zombierabbits)
    put_monstrer(map, monster_range, num_of_golems, 6, forbidden_golems)
    put_monstrer(map, monster_range, num_of_goblins, 4, forbidden_goblins)
    put_monstrer(map, monster_range, num_of_wolfs, 3, forbidden_wolfs)
    put_monstrer(map, monster_range, num_of_deers, 5, forbidden_deers)
    put_monstrer(map, monster_range, num_of_rabbits, 1, forbidden_rabbits)
    put_monstrer(map, monster_range, num_of_spiders, 2, forbidden_spiders)
    #12 is witch, she is on specific place

    put_monstrer(map, monster_range, num_of_salmons, 9, forbidden_salmons)

#put item on map
def put_loot(map,number_of_loots,loot_id, forbidden_places):
    for n in range(number_of_loots):
        put = False
        while put == False:
            unusable = False
            rand_x = random.randint(0,map_size_x - 1)
            rand_y = random.randint(0,map_size_y - 1)
            for f in forbidden_places:
                if map[rand_x,rand_y]["ground"] == f:
                    unusable = True
            if not unusable:
                if map[rand_x,rand_y]["inventory"] == 0:
                    map[rand_x,rand_y]["inventory"] = loot_id
                    put = True   
    
#puts loot randomly on the map
def random_loot(map):
    num_of_daggers = 100
    num_of_swords = 50
    num_of_spears = 20
    num_of_flowers = 300
    num_of_rings = 20
    num_of_diamonds = 10

    forbidden_daggers = [0,1,6]
    forbidden_swords = [0,1,2,6]
    forbidden_spears = [0,1,2,3,6]
    forbidden_flowers = [0,1,2,5,6]
    forbidden_rings = [0]
    forbidden_diamonds = [0,2,3,4,6]

    put_loot(map,num_of_daggers, 1, forbidden_daggers)
    put_loot(map,num_of_swords, 2, forbidden_swords)
    put_loot(map,num_of_spears, 3, forbidden_spears)
    put_loot(map,num_of_flowers, 4, forbidden_flowers)
    put_loot(map,num_of_rings, 5, forbidden_rings)
    put_loot(map,num_of_diamonds, 6, forbidden_diamonds)

print('encounters:')
random_encounters(info_map)
print('loot:')
random_loot(info_map)

"""
########################################################
            !!! control functions - not part of the final game !!!
########################################################
"""
#check_for_mosters(info_map,display_map)
#check_for_loot(info_map,display_map)
"""
########################################################
            !!! class definitions !!!
########################################################
"""
class player():
    def __init__(self,name,player_x,player_y):
        self.x = player_x
        self.y = player_y
        self.name = name
        self.health = 100
        self.number_of_scars = 0 
        self.atrocities = 0
        self.acts_of_cowardness = 0
        self.acts_of_bravery = 0

        self.spider_kills = 0
        self.wolf_kills = 0
        self.goblin_kills = 0
        self.golem_kills = 0
        self.cyclops_kills = 0
        self.salmon_kills = 0
        self.zombierabbit_kills = 0
        self.witch_kills = 0

        self.end_cause = ""

class inventory():
    def __init__(self):
        self.dagger = 1
        self.sword = 0
        self.spear = 0

        self.rabbit = 0
        self.spider = 0
        self.wolf = 0
        self.deer = 0

        self.flower = 0
        self.ring = 1
        self.diamond = 0
        self.pelt = 0
        self.ancient_knowledge = 0

"""
########################################################
            !!! Game Function definitions !!!
########################################################
"""
#draw text in several lines
def draw_multiline(surface,text,color,rect,font):
    rect = Rect(rect)
    y = rect.top + 3
    lineSpacing = 2
    fontHeight = font.size('Tg')[1]
    breaker = "ç"
    while text:
        b_exist = False
        for i in range(len(text)):
            if text[i] == breaker:
                b = i
                b_exist = True
                break
        if b_exist == True:
            line_surface = font.render(text[:b], True,color)
            surface.blit(line_surface,(rect.left + 3,y))
            y += fontHeight + lineSpacing
            text = text[b+1:]
        else:
            line_surface = font.render(text, True,color)
            surface.blit(line_surface,(rect.left + 3,y))
            text = ""  

#draw output text and wait for SPACE
def draw_outputandwait(output_text):
    pygame.draw.rect(screen, WHITE, output_box)
    draw_multiline(screen,output_text,out_text_color,output_box,out_text_font)
    draw_spacebartocontinue('continue')

#reveal map around player position
def reveal_map(grey_map,colored_map,player):
    x_max = player.x + look_range + 1 
    x_min = player.x - look_range
    y_max = player.y + look_range + 1
    y_min = player.y - look_range

    for i in range(x_min,x_max):
        for j in range(y_min,y_max):
            if i >= 0 and i < map_size_x and j >= 0 and j < map_size_y:
                distance = ((i-player.x)**2 + (j-player.y)**2)**(1/2)
                if distance <= look_range:
                    if grey_map[i,j,2] != colored_map[i,j,2]:
                        if grey_map[i,j,1] == grey_shade:
                            grey_map[i,j,:] = colored_map[i,j,:]

def remove_redcross(monster_x, monster_y, dis_map, original_map):
    if dis_map[monster_x,monster_y,0] != original_map[monster_x,monster_y,0]:
        for i in range(monster_x-3,monster_x+4):
                    for j in range(monster_y-3,monster_y+4):
                        if i >= 0 and i < map_size_x and j >=0 and j < map_size_y:
                            if (monster_x-i)**2 == (monster_y-j)**2:
                                dis_map[i,j,:] = original_map[i,j,:]        

#check for inventory items while stepping on them
def check_for_stuff(player,inv,map,search_range):
    x_max = player.x + search_range + 1 
    x_min = player.x - search_range
    y_max = player.y + search_range + 1
    y_min = player.y - search_range

    found = False
    wife_in_range = False
    for i in range(x_min,x_max):
        for j in range(y_min,y_max):
            if i >= 0 and i < map_size_x and j >= 0 and j < map_size_y:
                distance = ((i-player.x)**2 + (j-player.y)**2)**(1/2)
                if distance <= search_range:
                    if map[i,j]["ground"] == 10:
                        wife_in_range = True
                    if map[i,j]["inventory"] == 1:
                        if inv.dagger < 3:
                            inv.dagger += 1
                            map[i,j]["inventory"] = 0
                            found = True
                    elif map[i,j]["inventory"] == 2:
                        if inv.sword < 2:
                            inv.sword += 1
                            map[i,j]["inventory"] = 0
                            found = True
                    elif map[i,j]["inventory"] == 3:
                        if inv.spear < 1:
                            inv.spear += 1
                            map[i,j]["inventory"] = 0
                            found = True
                    elif map[i,j]["inventory"] == 4:
                        inv.flower += 1
                        map[i,j]["inventory"] = 0
                        found = True
                    elif map[i,j]["inventory"] == 5:
                        inv.ring += 1
                        map[i,j]["inventory"] = 0
                        found = True
                    elif map[i,j]["inventory"] == 6:
                        inv.diamond += 1
                        map[i,j]["inventory"] = 0
                        found = True
    return wife_in_range, found

#interaction between player and monster on land
def monster_meeting_land(moster_type,player,inv,map,displayed_map,original_map,monster_x,monster_y):
    if moster_type == 1:
        encounter_monster = rabbit(monster_x,monster_y)
    elif moster_type == 2:
        encounter_monster = spider(monster_x,monster_y)
    elif moster_type == 3:
        encounter_monster = wolf(monster_x,monster_y)
    elif moster_type == 4:
        encounter_monster = goblin(monster_x,monster_y)
    elif moster_type == 5:
        encounter_monster = deer(monster_x,monster_y)
    elif moster_type == 6:
        encounter_monster = golem(monster_x,monster_y)
    elif moster_type == 7:
        encounter_monster = cyclops(monster_x,monster_y)
    elif moster_type == 8:
        encounter_monster = elf(monster_x,monster_y)
    elif moster_type == 10:
        encounter_monster = zombie_rabbit(monster_x,monster_y)
    elif moster_type == 11:
        encounter_monster = magic_rabbit(monster_x,monster_y)
    elif moster_type == 12:
        encounter_monster = witch(monster_x,monster_y)
    
    encounter_start_text = "you have encountered %s. what will u do:\
    çA)ttack çI)nteract çR)un" % (encounter_monster.name)

    pygame.draw.rect(screen, WHITE, output_box)
    draw_multiline(screen,encounter_start_text,out_text_color,output_box,out_text_font)
    pygame.display.update()

    chosen = False
    while not chosen:
        en_choise = get_input() 
        en_choise = en_choise.upper()
        if en_choise == 'A' or en_choise == 'ATTACK':
            en_result = encounter_monster.attack(player,inv,map)
            remove_redcross(monster_x, monster_y, displayed_map, original_map)
            chosen = True
        elif en_choise == 'I' or en_choise == 'INTERACT':
            en_result = encounter_monster.interact(player,inv,map)
            remove_redcross(monster_x, monster_y, displayed_map, original_map)
            chosen = True
        elif en_choise == 'R' or en_choise == 'RUN':
            en_result = encounter_monster.run(player,map,displayed_map)
            chosen = True
        else:
            draw_wronginput()
    return en_result

#interaction between player and monster in water
def monster_meeting_water(moster_type,player,inv,map,displayed_map,original_map,monster_x,monster_y):
    if moster_type == 3:
        encounter_monster = wolf(monster_x,monster_y)
    elif moster_type == 4:
        encounter_monster = goblin(monster_x,monster_y)
    elif moster_type == 5:
        encounter_monster = deer(monster_x,monster_y)
    elif moster_type == 8:
        encounter_monster = elf(monster_x,monster_y)
    elif moster_type == 9:
        encounter_monster = vicious_salmon(monster_x,monster_y)
    
    encounter_start_text = "you have encountered %s. what will u do:\
    çA)ttack çI)nteract çR)un" % (encounter_monster.name)

    pygame.draw.rect(screen, WHITE, output_box)
    draw_multiline(screen,encounter_start_text,out_text_color,output_box,out_text_font)
    pygame.display.update()

    chosen = False
    while not chosen:
        en_choise = get_input() 
        en_choise = en_choise.upper()
        if en_choise == 'A' or en_choise == 'ATTACK':
            en_result = encounter_monster.attack(player,inv,map)
            remove_redcross(monster_x, monster_y, displayed_map, original_map)
            chosen = True
        elif en_choise == 'I' or en_choise == 'INTERACT':
            en_result = encounter_monster.interact(player,inv,map)
            remove_redcross(monster_x, monster_y, displayed_map, original_map)
            chosen = True
        elif en_choise == 'R' or en_choise == 'RUN':
            en_result = encounter_monster.run(player,map,displayed_map)
            chosen = True
        else:
            draw_wronginput()
    return en_result

#checks for monsters in range of player and starts interaction
def monster_time(player,inv,map,displayed_map,original_map):
    x_max = player.x + monster_range + 1
    x_min = player.x - monster_range
    y_max = player.y + monster_range + 1
    y_min = player.y - monster_range

    for i in range(x_min,x_max):
        for j in range(y_min,y_max):
            if i >= 0 and i < map_size_x and j >= 0 and j < map_size_y:
                distance = ((i-player.x)**2 + (j-player.y)**2)**(1/2)
                if distance <= monster_range:
                    if map[player.x,player.y]["ground"] == 1:
                        if map[i,j]["monster"] == 3 or map[i,j]["monster"] == 4 or map[i,j]["monster"] == 5\
                        or map[i,j]["monster"] == 8 or map[i,j]["monster"] == 9:
                            monster_meeting_result = monster_meeting_water(map[i,j]["monster"],player,inv,map,displayed_map,original_map,i,j)
                            draw_outputandwait(monster_meeting_result) 
                    else:
                        if map[i,j]["monster"] > 0 and map[i,j]["monster"] != 9:
                            monster_meeting_result = monster_meeting_land(map[i,j]["monster"],player,inv,map,displayed_map,original_map,i,j)
                            draw_outputandwait(monster_meeting_result) 

#draw inventory:
def draw_inventory(player,inv):
    inventory_box = pygame.Rect(1214, 12, 180, 520)
    inventory_color = (243,2,7)
    inventory_font = pygame.font.Font(None, 18)

    inventory_text = "%s" % (player.name)
    inventory_text += "ç" + "Health: %i" % (player.health)
    
    if player.number_of_scars > 0:
        inventory_text += "ç" + "Number of scars: %i" % (player.number_of_scars)
    if player.atrocities > 0:
        inventory_text += "ç" + "Atrocities commited: %i" % (player.atrocities)
    if player.acts_of_cowardness > 0:
        inventory_text += "ç" + "Being coward: %i" % (player.acts_of_cowardness)
    if player.acts_of_bravery > 0:
        inventory_text += "ç" + "Acts of bravery: %i" % (player.acts_of_bravery)
    if inv.ancient_knowledge > 0:
        inventory_text += "ç" + "Ancient knowledge gained: %i" % (inv.ancient_knowledge)
    if inv.dagger > 0:
        inventory_text += "ç" + "Daggers: %i / 3" % (inv.dagger)
    if inv.sword > 0:
        inventory_text += "ç" + "Swords: %i / 2" % (inv.sword)
    if inv.spear > 0:
        inventory_text += "ç" + "Spears: %i / 1" % (inv.spear)
    if inv.flower > 0:
        inventory_text += "ç" + "Flowers picked: %i" % (inv.flower)
    if inv.ring > 0:
        inventory_text += "ç" + "Rings: %i" % (inv.ring)
    if inv.diamond > 0:
        inventory_text += "ç" + "Diamons: %i" % (inv.diamond)
    if inv.pelt > 0:
        inventory_text += "ç" + "Pelts: %i" % (inv.pelt)
    if inv.rabbit > 0:
        inventory_text += "ç" + "Rabbits caught: %i" % (inv.rabbit)
    if inv.spider > 0:
        inventory_text += "ç" + "Spiders taken: %i" % (inv.spider)
    

    pygame.draw.rect(screen, WHITE, inventory_box)
    draw_multiline(screen,inventory_text,inventory_color,inventory_box,inventory_font)
    pygame.display.update()

#move object on map
def move(obj, movement_axis, movement_direction):
    if info_map[obj.x,obj.y]["ground"] == 1:
        movement_speed = 1
    elif info_map[obj.x,obj.y]["ground"] == 5:
        movement_speed = 2
    elif info_map[obj.x,obj.y]["ground"] == 6:
        movement_speed = 10
    else:
        movement_speed = 4

    if movement_axis == 'x':
        if movement_direction == 'plus':
            if obj.x + movement_speed < map_size_x - 6:
                obj.x += movement_speed
            else:
                obj.x = map_size_x - 7
        elif movement_direction == 'minus':
            if obj.x - movement_speed >= 6:
                obj.x -= movement_speed
            else:
                obj.x = 7
    elif movement_axis == 'y':
        if movement_direction == 'plus':
            if obj.y + movement_speed < map_size_y - 11:
                obj.y += movement_speed
            else:
                obj.y = map_size_y - 12
        elif movement_direction == 'minus':
            if obj.y - movement_speed >= 11:
                obj.y -= movement_speed
            else:
                obj.y = 11

"""
########################################################
            !!! start of the game loop !!!
########################################################
"""
person = player(person_name,person_x,person_y) 
person_inv = inventory()

done = False

while not done:
    read_input = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                move(person, 'x', 'minus')
            elif event.key == K_RIGHT:
                move(person, 'x', 'plus')
            elif event.key == K_UP:
                move(person, 'y', 'minus')
            elif event.key == K_DOWN:
                move(person, 'y', 'plus')
            elif event.key == pygame.K_RETURN:
                read_input = in_text.upper()
                in_text = ''
            elif event.key == pygame.K_BACKSPACE:
                in_text = in_text[:-1]
            else:
                in_text += event.unicode
    
    #reveal surrounding
    reveal_map(display_map,c_map,person)

    #draw map and clear output
    mapbox = pygame.surfarray.make_surface(display_map)
    screen.blit(mapbox,(0,0))
    pygame.draw.rect(screen, WHITE, output_box)

    #draw player and his inventory
    screen.blit(player_img,(person.x - 5,person.y - 10))
    draw_inventory(person,person_inv)

    #check actual position for loot
    wife_stepped_on, step_on = check_for_stuff(person,person_inv,info_map,step_range)
    if wife_stepped_on:
        wife_stepped_on_text = 'you have aproached your potential wife'
        person.end_cause = 'wife'
        draw_outputandwait(wife_stepped_on_text)
        done = True
        break
    if step_on:
        step_on_text = "you stepped on something"
        draw_outputandwait(step_on_text) 
        draw_inventory(person,person_inv)

    #moster move, look in square around position, check if the position is in range
    monster_time(person,person_inv,info_map,display_map,c_map)
    draw_inventory(person,person_inv)

    #check for players health
    if person.health <= 0:
        if person.end_cause == "":
           person.end_cause = "health"
        done = True
        break

    #lookaround rutine
    if read_input == "LOOK":
        read_input = ""
        wife_seen, looked_for = check_for_stuff(person,person_inv,info_map,look_range)
        if wife_seen:
            wife_seen_text = "you can see your goal"
            draw_outputandwait(wife_seen_text) 
        if looked_for:
            looked_for_text = "you succesfully found something"
        else:
            looked_for_text = "you found nothing"
        draw_outputandwait(looked_for_text)
        draw_inventory(person,person_inv)


    #draw input text
    in_text_surface = in_text_font.render(in_text, True, in_text_color)
    pygame.draw.rect(screen, BLACK, input_box)
    screen.blit(in_text_surface, (input_box.left + 1, input_box.top + 6))


    pygame.display.update()

"""
########################################################
            !!! End Function definitions !!!
########################################################
"""
#calculates cool factor for wife meeting                    
def cal_coolfactor(pl,inv):
    coolfactor = 5 * inv.rabbit - 2 * inv.spider + 3 * inv.flower + 5 * inv.pelt + 10* inv.ring \
    + 5 * pl.acts_of_bravery + 10 * inv.wolf + 15 * inv.deer + 50 * inv.ancient_knowledge \
    + 4 * pl.number_of_scars - 10 * pl.atrocities - 1 * pl.acts_of_cowardness \
    + 1 * pl.spider_kills + 3 * pl.goblin_kills + 3 * pl.wolf_kills + 9 * pl.golem_kills + 15 * pl.cyclops_kills\
    + 4 * pl.salmon_kills + 10 * pl.zombierabbit_kills + 20 * pl.witch_kills
    return coolfactor

def draw_imageandwait(screen_img):
    screen.blit(screen_img,(0,0))
    pygame.draw.rect(screen, WHITE, output_box)
    draw_spacebartocontinue('end')

def wife_encounter(player,inv):
    screen.blit(wife_en_img,(0,0))
    pygame.draw.rect(screen, WHITE, output_box)
    pygame.display.update()
    lvl_of_cool = cal_coolfactor(player,inv)
    lvl_of_cool_needed = 50

    wife_an_chosen = False
    while not wife_an_chosen:
        wife_en_choise = get_input() 
        wife_en_choise = wife_en_choise.upper()
        if wife_en_choise == 'TRUTH' or wife_en_choise == 'T':
            if lvl_of_cool >= lvl_of_cool_needed:
                draw_imageandwait(cool_truth_img)
            else:
                draw_imageandwait(uncool_truth_img)
            wife_an_chosen = True
        elif wife_en_choise == 'LIE' or wife_en_choise == 'L':
            if lvl_of_cool >= lvl_of_cool_needed:
                draw_imageandwait(cool_lie_img)
            else:
                draw_imageandwait(uncool_lie_img)
            wife_an_chosen = True
        else:
            draw_wronginput() 

"""
########################################################
            !!! End !!!
########################################################
"""
if person.end_cause == 'wife':
    wife_encounter(person,person_inv)
elif person.end_cause == 'cyclops':
    draw_imageandwait(cyclops_end_img)
elif person.end_cause == 'elf':
    draw_imageandwait(elf_end_img)
elif person.end_cause == 'rabbit':
    draw_imageandwait(rabbit_end_img)
elif person.end_cause == 'witch':
    draw_imageandwait(witch_end_img)
elif person.end_cause == 'health':
    draw_imageandwait(health_end_img)
else:
    draw_imageandwait(simple_end_img)


pygame.quit()