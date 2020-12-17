import random
import time

#attack_dic = {melee_attacks : ["hit", "attack", "melee", "rage", "slash", "thrust"], spell_attacks : ["spell", "cast", "bewitch"]}
end = False
numbers = 0

#The types of classes that the player can choose to be, 7 player maximum.
magic_types = [
  "magic",
  "melee",
  "ice",
  "fire",
  "electric",
  "spirit",
  "energy"
]

for x in magic_types:
    numbers += 1
    print(numbers, x)

#This variable will keep track of how many plaers are in the game, and therefore, will be used to determine the characters in the game.
how_many = int(input("How many players are there? "))

#The dictionary below is used to keep track of each players damage type, and their level.
players = {}
player_count = 0

#The while loop here is used to record the player's character architypes. 
while how_many > 0:
    player_count += 1
    #The list here is used to contain the attributes for a single character
    player_attrib = []
    
    attrib1 = input("Choose your character's damage type: ")
    attrib2 = input("What is your current level? ")

    player_attrib.append(attrib1)
    player_attrib.append(attrib2)
    #This will then append the character's information to the dictionary for the specific player.
    players[player_count] = player_attrib

    how_many -= 1

print(players)

#enemy_ac = " "
#level = 1
#bonus_dmg = level + random.randint(1,20)

#PLACEHOLDER = 4

#battle = False

#enemy_grunt = 500
#enemy_health_boss = 1000
#big_bad = 5000

#danger = 1

#grunt_dmg = level * danger


class algorithm:
    #The dictionary below contains the resistance of the horde that the player / players will have to face.
        #The resistances will change depending on the outcome of the resistance varaible.
    horde_resistance = {magic_res : 0, melee_res : 0 , ice_res : 0 , fire_res : 0, electric_res : 0, spirit_res : 0, energy_res : 0}

    def __init__(self, type1, level, power, resistance):
        self.type1 = type1
        self.level = level
        self.power = power
        self.resistance = resistance

    def resistance(self):
        #This function contains the code that will be randomly assigned to the hordes when the players have to fight them.
        rand_horde_num = random.randint(1,10)
        resist = 1

        if self.type1 == "magic":
            #Depending on what type or architype the player chooses, the resistance of the mobs will change depending on that.
                #The resistance will increase with the level of the player so that they won't be able to instantly defeat the horde.
            magic_dmg = resist * self.level
            horde_resistance[magic_res] = magic_dmg
        elif self.type1 == "melee":
            melee_dmg = 10 * self.level
            horde_resistance[melee_res] = melee_dmg
        elif self.type1 == "ice":
            ice_dmg = 10 * self.level
            horde_resistance[ice_res] = ice_dmg
        elif self.type1 == "fire":
            fire_dmg = 10 * self.level
            horde_resistance[fire_res] = fire_dmg
        elif self.type1 == "electric":
            electric_dmg = 10 * self.level
            horde_resistance[electric_res] = electric_dmg
        elif self.type1 == "spirit":
            spirit_dmg = 10 * self.level
            horde_resistance[spirit_res] = spirit_dmg
        elif self.type1 == "energy_dmg":
            energy_dmg = 10 * self.level
            horde_resistance[energy_res] = energy_dmg

    def enemy_move(self):
        attack_who = random.ranint(1, self.amount_of_players)



    def algorithm(self):
        time.sleep(600)
        while end != True:
            random.randint(1, 10)
            fight = 0

            fight += random.randint(1,10)
            if fight >= 7:
                #Enemy choice and health of the enemy horde.
                rand_bigbad = random.ranint(1,4)
                if rand_bigbad == 1:
                    horde = danger * enemy_grunt 
                elif rand_bigbad == 2:
                    horde = (danger / 2) * enemy_heath_boss
                elif rand_bigbad == 3:
                    horde = (danger * enemy_grunt) + (danger/2 * enemy_health_boss)

                #Damage from the players to the horde.
                if bonus_dmg * level >= horde:
                    print("You've successfully killed off the entire horde!")
                    EnemyHealth = EnemyHealth - (bonus_dmg + possibility)
                    if EnemyHealth < horde:
                        kills = horde % (level*bonus_dmg)
                        horde -= level*bonus_dmg
                        print("You've killed", kills, "enemies.")
                        enemy_move()
                else:
                    print("You we're unable to pull of the move.")

                if battle == True:
                    move = input("What move are you gonna do?")

                    move_words = move.split()

                    for x in move_words:
                        for y in keywords:
                            if x == y:
                                possibility = random.randint(1,20)
                                damage(PLACEHOLDER)
                time.sleep(450)
                fight = 0
                algorithm()
            else:
                time.sleep(300)
                fight = 0
                algorithm()