import random
import time

instructions = "Below you have 5 catagories which are used to give your character different attributes so that you'll be able to have a greater chance of success when an action that you want to do relies on that speciifc ability."
    
#The following dictionary contains the attributes that the player can have.
skills = {"Strength" : 0, "Magic" : 0, "Stamina" : 0, "Speed" : 0, "Intelligence" : 0}
points = 50

#The following 2 definitions work in tandom with one another, and are used to create a character.
def character_creation():
    print("Hello, and welcome to *INSERT GAME NAME HERE*!")
    print(instructions)
    #The points variable here is to show the player how many points they have left to spend on the categories.

    print("You have ", str(points), "to spend on the categories listed.")
    print("Add points of the following categories:")

    loop()

#The following for loop is used to append the skills points that the player wants for each category to the specific category.
def loop():
    global points, skills

    #The loop here is used to create a iterate through the keys inside of the dictionary so as to assign the points that the user wants to give them.
    for x in skills.keys():
        print("You have", points, "left.\n" +  str(x) + ":")
        skills[x] = int(input())
        #Each attribute is capped off at 20
        if skills[x] < points and skills[x] <= 20:
            points -= skills[x]
        else:
            skills[x] = 0
            print("You don't have that many points")
            for x in skills.keys():
                skills[x] = 0
            points = 50
            loop()

    for x in skills:
        print(x)

    #Calling this function will result in the player being assinged his role as either a hybrid, melee, or magic dealer. 
    player_type()

def player_type():
    global character_type

    if skills["Strength"] > skils["Magic"]:
        character_type = "melee"
    elif skills["Strength"] < skills["Magic"]:
        character_type = "wizard"
    elif skills["Strength"] = skills["Magic"]:
        character_type = "hybrid"

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
#while how_many > 0:
    #player_count += 1
    #The list here is used to contain the attributes for a single character
    #player_attrib = []
    
    #attrib1 = input("Choose your character's damage type: ")
    #attrib2 = input("What is your current level? ")

    #player_attrib.append(attrib1)
    #player_attrib.append(attrib2)
    #This will then append the character's information to the dictionary for the specific player.
    #players[player_count] = player_attrib

    #how_many -= 1

print(players)

#This function is used to outline when a fight is to occur.
def fighting():
    global character_type

    battle = False

    while end = False:
        time.sleep(300)
        #To add randomness to the game, depending on what value "rand" is equal to, then the algorithm will be initialized, and a battle sequence will occur.
        rand = random.randint(1,5)
        if rand >= 4:
            battle = True
            begin = algorithm(character_type, 1, skills["stamina"], skills["speed"], skills["intelligence"])
            begin.algorithm()
        else:
            fighting()

class algorithm:
    #The dictionary below contains the resistance of the horde that the player / players will have to face.
        #The resistances will change depending on the outcome of the resistance varaible.
    horde_resistance = {magic_res : 0, melee_res : 0 , hybrid_res : 0}

    def __init__(self, type1, level, stamina, speed, intelligence):
        self.type1 = type1
        self.level = level
        self.stamina = stamina
        self.speed = speed
        self.intelligence = intelligence

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
        elif self.type1 == "hybrid":
            hybrid_dmg = 10 * self.level
            horde_resistance[hybrid_res] = hybrid_dmg

    def horde_health(self):
        if self.level < 10:
            hh = 100 * self.level
        elif self.level > 10 and self.level < 20:
            hh = 200 * self.level
        elif self.level == 30:
            hh = 300 * self.level

    #def enemy_move(self):
        #attack_who = random.ranint(1, self.amount_of_players)



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