import random

def cal_atp(inv):
    attackpower = 2 * inv.dagger + 5 * inv.sword + 8 * inv.spear + 15 * inv.wolf
    return attackpower

def decrease_life(player, life_taken):
    if player.health - life_taken >= 0:
        player.health -= life_taken
    else:
        player.health = 0

def run_away(player,monster_x, monster_y, min_distance, max_distance, dis_map):
    runned = False
    map_size_x = dis_map.shape[0]
    map_size_y = dis_map.shape[1]
    while runned == False:
        new_x = player.x + (player.x-monster_x)*random.randint(min_distance,max_distance)
        new_y = player.y + (player.y-monster_y)*random.randint(min_distance,max_distance)
        if new_x >= 0 and new_x <= map_size_x and new_y >= 0 and new_y <= map_size_y and (new_x != player.x or new_y != player.y):
            player.x = new_x
            player.y = new_y
            runned = True
            #change map to show that
            for i in range(monster_x-3,monster_x+4):
                    for j in range(monster_y-3,monster_y+4):
                        if i >= 0 and i < map_size_x and j >=0 and j < map_size_y:
                            if (monster_x-i)**2 == (monster_y-j)**2:
                                dis_map[i,j,0] = 255
                                dis_map[i,j,1] = 0
                                dis_map[i,j,2] = 0

class rabbit():
    def __init__(self,x,y):
        self.defence = 0
        self.name = "rabbit"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        player.atrocities += 1
        if (atp - self.defence) > 0:
            out_text = "your hands are covered in blood of innocent rabbit.\
            çyou feel sick for what you have done and your consciousness will never be clean again."
            inv.pelt += 1
        else:
            out_text = "how. did. you. fail?"
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 8:
            out_text = "rabbit run away"
        else:
            out_text = "you caught the rabbit"
            inv.rabbit += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "you run away from little rabbit. you coward!"
        player.acts_of_cowardness += 1
        run_away(player,self.x, self.y, 0, 3, displayed_map)

        return out_text

class spider():
    def __init__(self,x,y):
        self.defence = 1
        self.name = "spider"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        if (atp - self.defence) > 0:
            player.spider_kills += 1
            out_text = "you killed the spider. i guess, he had it comming"
        else:
            out_text = "you failed to defeat this 'mighty' spider. you weakling!"
        return out_text

    def interact(self,player,inv,map):
        dice = random.randint(1,10)
        map[self.x,self.y]["monster"] = 0
        if dice <= 3:
            out_text = "spider bit you"
            player.number_of_scars += 1
            decrease_life(player, 5)
        else:
            out_text = "you caught the spider"
            inv.spider += 1
        return out_text
 
    def run(self,player,map,displayed_map):
        out_text = "you run away from the spider. really?"
        player.acts_of_cowardness += 1
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text

class wolf():
    def __init__(self,x,y):
        self.defence = 3
        self.name = "wolf"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        atp = cal_atp(inv)
        map[self.x,self.y]["monster"] = 0
        if (atp - self.defence) > 0:
            dice = random.randint(1,10)
            if dice <= 3:
                out_text = "you defeated the wolf, but not without the cost"
                player.number_of_scars += 1
                decrease_life(player, 5)
                player.wolf_kills += 1
                inv.pelt += 1
            else:
                out_text = "clean kill"
                player.wolf_kills += 1
                inv.pelt += 1
        else:
            out_text = "you are defeated. wolf is standing victorious on the top of your chest. \
            çbut he is satistified with the blood in his mouth and scars he left you with and leaves"
            player.number_of_scars += 3
            decrease_life(player, 20)
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 5:
            out_text = "you tried to pet the wolf, but he bit you"
            player.number_of_scars += 1
            decrease_life(player, 5)
        elif dice <=9:
            out_text = "you pet the wolf and he nods towards you in act of mutual understanding"
            player.acts_of_bravery += 1
        else:
            out_text = "you kneel in front of the wolf and he kneels in front of you. \
            çyou feel the instant connection. you have become friends for life"
            inv.wolf += 1
            player.acts_of_bravery += 1
        return out_text  

    def run(self,player,map,displayed_map):
        dice = random.randint(1,10)
        if dice <= 3:
            out_text = "did u really think u can outrun a wolf? he bit you while you were trying.\
            fontunatelly for you, it was enough for him."
            decrease_life(player, 10)
            player.number_of_scars += 1
        else:
            out_text = "i guess better safe than sorry"
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text


class goblin():
    def __init__(self,x,y):
        self.defence = 4
        self.name = "goblin"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        if (atp - self.defence) > 0:
            dice = random.randint(1,10)
            if dice <= 3:
                out_text = "the goblin lies dead next to you. you heart is beating after long fight.\
                çyou feel the mixture of yours and his blood on your scared body. and you lost your weapon"
                player.number_of_scars += 2
                decrease_life(player, 10)
                player.goblin_kills += 1
                if inv.dagger > 0:
                    inv.dagger -= 1
                else:
                    if inv.sword > 0:
                        inv.sword -= 1
                    elif inv.spear > 0:
                        inv.spear -= 1
                    else:
                        pass
            elif dice <= 8:
                out_text = "after short fight u killed the goblin"
                decrease_life(player, 5)
                player.goblin_kills += 1
            else:
                out_text = "in one clean sweap u chopped his head. and stole his dagger. and the wedding ring."
                player.goblin_kills += 1
                if inv.dagger < 3:
                    inv.dagger += 1
                inv.ring += 1
        else:
            out_text = "the goblin defeated you. he stands next your bloodied body lying on the ground and laughts. \
            çnand laughts. and laughts...Ha ha HAhahaHAha ha"
            player.number_of_scars += 3
            decrease_life(player, 20)
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 3:
            out_text = "u wanted to speak with the goblin, but second after you opened you mouth he smacked you and left"
            player.number_of_scars += 1
        elif dice <= 8:
            out_text = "you stared to the eyes of the goblin, thinking about what he is thinking. \
            çand after a while you shaked your hands. giving respect one to the another"
            player.acts_of_bravery += 1
        else:
            out_text = "you high-fived the goblin and he gave you small trinket of frienship"
            player.acts_of_bravery += 1
            inv.ring += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "well, he looked scary..."
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text

class deer():
    def __init__(self,x,y):
        self.defence = 6
        self.name = "deer"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        player.atrocities += 1
        if (atp - self.defence) > 0:
            out_text = "you killed a deer. a peaceful, harmless creature. and u cut his throat and let him bleed to death...\
            çand took his skin..."
            inv.pelt += 1
        else:
            out_text = "u tried to slay the magnificent beast, but he dodged, used his antlers to get you to the ground.\
            çand kicked u. kicked u hard!"
            decrease_life(player, 10)
            player.number_of_scars += 1
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 3:
            out_text = "u wanted to pet the deer, yet he run away"
        elif dice <= 9:
            out_text = "you friendly approached the deer. he carefully observed u and let u touch him. \
            çhe let you quietly pet him and you shared quiet, beautiful moment. and he gave u flower in the end."
            inv.flower += 1
        else:
            out_text = "you bowed to the deer and he kneeled in front of you. letting you drive him."
            inv.deer += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "u are running from peaceful deer while he is silently staring at you. \
        çrelentlesly. continuously. silently. staring. at. you"
        player.acts_of_cowardness += 1
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text

class golem():
    def __init__(self,x,y):
        self.defence = 9
        self.name = "golem"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        player.acts_of_bravery += 1
        if (atp - self.defence) > 0:
            dice = random.randint(1,10)
            if dice <=5:
                out_text = "you managed to defeat the golem. barely. and u damaged your weapon doing so."
                decrease_life(player, 10)
                player.number_of_scars += 1
                if inv.dagger > 0:
                    inv.dagger -= 1
                elif inv.sword > 0:
                    inv.sword -= 1
                elif inv.spear > 0:
                    inv.spear -= 1
                else:
                    pass
            else:
                out_text = "you smashed the golem into the pile of rocks. so you took some."
                inv.diamond += random.randint(1,4)
        else:
            out_text = "you got beaten to the ground by the golem."
            decrease_life(player, 25)
            player.number_of_scars += 2
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        player.acts_of_bravery += 1
        if dice <= 5:
            out_text = "you tried to speak to golem. but golems do not speak...\
            çthey use their hands."
            player.number_of_scars += 1
            decrease_life(player, 10)
        else:
            out_text = "you sat on the group waiting for golem to react.\
            çhe sat as well, shared a quiet moment with you. and left small rock behind him after he left."
            inv.diamond += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "wise. he was big... and hard."
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text

class cyclops():
    def __init__(self,x,y):
        self.defence = 15
        self.name = "cyclops"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        player.acts_of_bravery += 1
        if (atp - self.defence) > 0:
            out_text = "you did it! you slained the cyclops. you can call yourself mighty warrior from now on."
            player.cyclops_kills += 1
            player.number_of_scars += 2 
            inv.spear += 1
        else:
            dice = random.randint(1,10)
            if dice <= 5:
                out_text = "you are dead. he killed you."
                player.health = 0
                player.end_cause = "cyclops"
            else:
                out_text = "you tried to attack huge cyclops. and u got your ass kicked\
                çplus he took all your weapons."
                decrease_life(player, 55)
                player.number_of_scars += 5
                inv.dagger = 0
                inv.sword = 0
                inv.spear = 0
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        player.acts_of_bravery += 1
        dice = random.randint(1,20)
        if dice <= 5:
            out_text = "well. he just smacked you. and while you were uncounscious he took one of your weapons."
            decrease_life(player, 15)
            player.number_of_scars += 1
            if inv.dagger > 0:
                inv.dagger -= 1
            elif inv.sword > 0:
                inv.sword -= 1
            elif inv.spear > 0:
                inv.spear -= 1
            else:
                pass                    
                    
        elif dice <= 10:
            out_text = "you offered the cyclops the hand to shake. and he did it. viciously."
            decrease_life(player, 5)
        elif dice <= 19:
            out_text = "you waved you hand at cyclops, attending to greet him. he did the same...\
            çand than threw the spear at u. so you picked it up."
            if inv.spear < 1:
                inv.spear += 1
        else:
            out_text = "you waited a while staring into his eyes. he waited and after a while poited towards his fire.\
            çyou sat together next to the fire. you feel like you learned a lot."
            inv.ancient_knowledge += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "reasonable. very reasonable."
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text

class elf():
    def __init__(self,x,y):
        self.defence = 20
        self.name = "elf"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        player.atrocities += 1
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        if (atp - self.defence) > 0:
            out_text = "you did it. you actually did it.\
            çyou attack and killed one of the last members of this wise race. world suffered a huge lost.\
            çand you looted his corpse... so at least you gained something. you monster."
            inv.ring += 2
            if inv.sword < 2:
                inv.sword += 1
            if inv.spear < 1:
                inv.spear += 1
        else:
            dice = random.randint(1,10)
            if dice <= 5:
                out_text = "why, why did you have to attack this old and battle-harden elf. now you lay slain on the ground."
                player.health = 0
                player.end_cause = "elf"
            else:
                out_text = "while he could easily kill you, he satisfied himself with severely beating you and taking all of your weapons"
                if player.health > 20:
                    player.health = 15
                else: 
                    player.health = 1
                inv.dagger = 0
                inv.sword = 0
                inv.spear = 0
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        if inv.dagger + inv.sword + inv.spear == 0:
            out_text = "seeing that you have no weapon this wise and charitable elf gave you his sword."
            inv.sword += 1
        else:
            dice = random.randint(1,10)
            if dice <= 3:
                out_text = "u tried to speak with the elf. but you forgot all the elven you know except 'the soup'.\
                çthe conversation did not go very well... but he gave you flower for you to feel better."
                inv.flower += 1
            elif dice <= 9:
                out_text = "you approached the elf, greeting him in his own language. and used all 5 phrases if elven you remembered.\
                çelf looked slightly amuzed by your effords and gave you one of his rings as a token of friendship."
                inv.ring += 1
            else:
                out_text = "you remembered every lesson of elven from the school and you engaged in deep and satisfying conversation with the elf.\
                çin the end you felt different. his wisdom changed you forever. and he even gave you his ring. shiny..."
                inv.ancient_knowledge += 1
                inv.ring += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "you run away from wise and gentle elf. why?"
        player.acts_of_cowardness += 1
        run_away(player,self.x, self.y, 0, 3, displayed_map)
        return out_text

class vicious_salmon():
    def __init__(self,x,y):
        self.defence = 4
        self.name = "vicious salmon"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        if (atp - self.defence) > 0:
            out_text = "you killed and gutted the salmon. you found somethin!"
            inv.ring += 1
            player.salmon_kills +=1
        else:
            out_text = "you tried to attack the salmon, \
            çbut he was faster and bit you several times instead."
            player.number_of_scars += 3
            decrease_life(player, 15)
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 5:
            out_text = "you, for some reason, wanted to pet the salmon...\
            çhe did not like the idea. he bit you and left"
            player.number_of_scars +=1
            decrease_life(player, 5)
        else:
            out_text = "you stared into the eyes of salmon.\
            çhe yielded and left you with his ring"
            inv.ring += 1
        return out_text

    def run(self,player,map,displayed_map):
        out_text = "you swimmed away"
        run_away(player,self.x, self.y, 0, 3, displayed_map)

        return out_text

class zombie_rabbit():
    def __init__(self,x,y):
        self.defence = 5
        self.name = "strangely looking rabbit"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        if (atp - self.defence) > 0:
            out_text = "you cut his head and you see no blood comming out.\
            çit was a ZOMBIE rabbit! good that u killed it."
            player.acts_of_bravery += 1
            player.zombierabbit_kills += 1
        else:
            out_text = "you tried to hunt down the rabbit but he turned on you with unexpected rage.\
            çhe went straight for you brain! fortunatelly you managed to fight him off soon."
            player.number_of_scars += 3
            decrease_life(player, 30)
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 2:
            out_text = "you wanted to play with the rabbit.\
            çslowly approaching him, you tried to seem as friendly as possible.\
            çwhat you did not expect was that he will jump to your throath and cut both of your arteries!.\
            çwhile you life was slowly leaving you, you felt how he is clawing his way to you brain."
            player.health = 0
            player.end_cause = "rabbit"
        else:
            out_text = "you wanted to catch the rabbit. you were slowly approaching the rabbit and then saw it.\
            çthe dead look in his eyes. you realized that something is not quite right and wisely left."

        return out_text

    def run(self,player,map,displayed_map):
        out_text = "he DID look strange"
        run_away(player,self.x, self.y, 0, 3, displayed_map)

        return out_text

class magic_rabbit():
    def __init__(self,x,y):
        self.defence = 38
        self.name = "strangely looking rabbit"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        player.atrocities += 1
        if (atp - self.defence) > 0:
            out_text = "you killed a helpful magic rabbit. world, and especially its master, will never forgive you."
            inv.pelt += 1
        else:
            out_text = "you saw that the rabbit is strange, yet you still attacked him.\
            çyou were hit by fireball to the face.\
            çit was magical rabbit and he swiftly defeated you."
            player.number_of_scars += 5
            decrease_life(player, 60)
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        dice = random.randint(1,10)
        if dice <= 3:
            out_text = "you wanted to catch the rabbit, but he flew away leaving a rainbow trail behind him."
        elif dice <= 9:
            out_text = "you saw that the rabbit fur is shiny so you approached him without fear.\
            ç'what do you wish of me?', he said to you. so you asked for a ring."
            inv.ring += 1
        else:
            out_text = "you inspected the rabbit and saw that his eyes are out of rubbies and his fur out of gold.\
            çit was an avatar of rabbit-god PISKPISKL! you felt on the ground and bow in front of him.\
            çhe approached you and spoke to you 'you are faithful one, i shall reward you.'"
            player.health = 100
            inv.ancient_knowledge += 1
            inv.ring += 1
            inv.diamond += 1

        return out_text

    def run(self,player,map,displayed_map):
        out_text = "he DID look strange"
        run_away(player,self.x, self.y, 0, 3, displayed_map)

        return out_text

class witch():
    def __init__(self,x,y):
        self.defence = 20
        self.name = "elderly witch"
        self.x = x
        self.y = y

    def attack(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        atp = cal_atp(inv)
        player.acts_of_bravery += 1
        if (atp - self.defence) > 0:
            out_text = "using all you weapons, cunning and skill you slain the wicked witch."
            inv.ring += 1
            player.witch_kills += 1
        else:
            out_text = "she turned you into a frog and boiled you alive."
            player.end_cause = "witch"
            player.health = 0
        return out_text

    def interact(self,player,inv,map):
        map[self.x,self.y]["monster"] = 0
        player.acts_of_bravery += 1
        dice = random.randint(1,10)
        if dice <= 3:
            out_text = "you said to the witch that she is ugly. she wasn't pleased.\
            çshe hit you with her stick and screamed some curses. hopefully they will not work"
            decrease_life(player, 5)
        elif dice <= 9:
            out_text = "you behaved nicely to the witch, so she healed you a bit."
            if player.health < 80:
                player.health += 20
            else:
                player.health = 100
        else:
            out_text = "you offered a small gift to the witch, which she accepted.\
            çin return she healed you and shared some of her dark knowledge."
            inv.ring -= 1
            player.health = 100
            inv.ancient_knowledge += 1


        return out_text

    def run(self,player,map,displayed_map):
        out_text = "who would want to deal with that?"
        run_away(player,self.x, self.y, 0, 3, displayed_map)

        return out_text