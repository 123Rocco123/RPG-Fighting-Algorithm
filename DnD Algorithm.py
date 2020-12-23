import random
import time

#The dictionary below is used to determine the words that the player would use to see if they want to attack of hit something. 
attack_dic = {melee_attacks : ["hit", "attack", "melee", "rage", "slash", "thrust"], 
              spell_attacks : ["spell", "cast", "bewitch"], 
              flight : ["run away", "escape", "leave", "get lost", "bounce", "retreat"], 
              surrender : ["give up", "accept fate", "surrender", "quit", "lay down", "roll over"],
              intelligence : ["out think", "smarten out", "outwit",  "wits", "intelligence", "IQ"]
              }

#This varaible is used to determine if the game is at an end or not. 
end = False

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

    #Player's character's archetype will be determined by seeing if one category is overwhelmingly higher compared to another. 
    if skills["Strength"] >= skils["Magic"] + 10:
        character_type = "melee"
    elif skills["Magic"] >= skills["Strength"] + 10:
        character_type = "wizard"
    else:
        character_type = "hybrid"

#This function is used to outline when a fight is to occur.
def fighting():
    global character_type

    battle = False

    while end == False:
        time.sleep(300)
        #To add randomness to the game, depending on what value "rand" is equal to, then the algorithm will be initialized, and a battle sequence will occur.
        rand = random.randint(1,10)
        if rand >= 7:
            battle = True
            begin = algorithm(character_type, 1, skills["stamina"], skills["speed"], skills["intelligence"])
            begin.algorithm_fun()
        else:
            fighting()

class algorithm:
    #The dictionary below contains the resistance of the horde that the player / players will have to face.
        #The resistances will change depending on the outcome of the resistance varaible.
    horde_resistance = {magic_res : 0, melee_res : 0}
    health = 500 + (100*level)

    #The following varaibles are used to the determine what was the person's first choice. 
        #Depending on what they chose, the next time, they won't be allowed to choose that option. 
    stamina_first = False
    intelligent_first = False
    fighting_first = False

    #This varaible is used to decrease the required points to successfully run away from hordes.
    easy_mode_stamina = 10

    #This will determine the number of hordes that the player will be up against.
        #As the horde number increases, so will their strength, keeping the challenge resonable and not allowing the player to breeze through the game. 
    hordes = 1

    def __init__(self, type1, level, stamina, speed, intelligence):
        self.type1 = type1
        self.level = level
        self.stamina = stamina
        self.speed = speed
        self.intelligence = intelligence

    def resistance(self):
        #Depending on what type or architype the player chooses, the resistance of the mobs will change depending on that.
                #The resistance will increase with the level of the player so that they won't be able to instantly defeat the horde.
        if self.type1 == "magic":
            magic_dmg = (2 * self.level) * hordes
            horde_resistance[magic_res] = magic_dmg
        elif self.type1 == "melee":
            melee_dmg = (2 * self.level) * hordes
            horde_resistance[melee_res] = melee_dmg
        elif self.type1 == "hybrid":
            melee_dmg = (2 * self.level) * hordes
            magic_dmg = (2 * self.level) * hordes
            
            horde_resistance[melee_res] = melee_dmg
            horde_resistance[magic_res] = magic_dmg

    #This function is used to determine the damage that the player will inflict on the enemy hordes. 
    def player_dmg(self):
        if player_action == attack_dic[melee_attacks]: 
            p1_dmg = (skills["Strength"] - horde_resistance[melee_res]) + (0.25 * skills["Magic"])
        elif play_action == attack_dic[spell_attack]:
            p1_dmg = (skills["Magic"] - horde_resistance[magic_res]) + (0.25 * skills["Strength"])

    #The function here is used to determine if the health of the enemy horde.
        #The health will either increase or decrease depending on the level of the players.
    def horde_health(self):
        if self.level < 10:
            hh = 100 * self.level
            init_hh = hh
        elif self.level > 10 and self.level < 20:
            hh = 200 * self.level
            init_hh = hh
        elif self.level == 30:
            hh = 300 * self.level
            init_hh = hh

    #This function is used to determine how much health the player will lose depenig on the health of the enemy horde. 
        #When the horde will have 25% of their health, then they will enter a "bonus damage" of sorts, where they'll deal an extra 25% damage to the player.
    def enemy_move(self):
        attack = (self.level**2) * 5

        if hh > 0:
            player_health -= attack
        elif hh == (0.25 * init_hh):
            player_health -= attack + (attack * 0.25)

    #This function is used to determine what is to happen if the player is to fail their intelligence option. 
    def failed_genius(self):
        print("You weren't able to talk your way out of this one, and now the horde is angry with you.\n Your only options are that of fighting horde, running away, or accepting your faith.")

        player_action = input("What do you want to do? ")
                                
        #This while loop is here to make sure that if the player fails to beat the horde with intellect, then they'll have to either fight them, run, or accept their fate. 
        while hh > 0:
            if player_action == attack_dic[melee_attacks] or attack_dic[spell_attacks]:
                #Damage from the players to the horde
                self.player_dmg()
                hh -= p1_dmg
                self.enemy_move()
            if player_action == attack_dic[flight]:
                flight_escape_prob = random.randint(1,5) * self.speed

                if flightflight_escape_prob >= 60 + (self.level *2):
                    print("You've managed to escape from the horde, even though you failed to outwit them.\nIt seems that sometimes its best just to run instead of using YOUR head...")

                    hh = 0
                    horde += 1
            elif player_action == attack_dic[surrender]:
                print("You've accepted your fate")
                                        
                hh = 0
                time.sleep(2)
                exit()

    #This function is used for when a player wants to do an action that uses their character's wits to get out of a situation. 
    def intelligence_func(self):
        intelligent_escape = random.randint(1,5) * self.intelligence

        #Depending on the player's level, the probabilities required to escape the horde will change. This is to make sure that the player will not just have to invest to a certain level, and then be able to beat all of the hordes. 
        if intelligent_escape >= 15 and self.level < 5:
            print("You've managed to outwit the horde, even though you failed to outrun them.")

            horde += 1
            hh = 0

        elif intelligent_escape >= 20 and self.level < 10 and self.level >= 5:
            print("You've managed to outwit the horde, even though you failed to outrun them.")

            horde += 1
            hh = 0

        elif intelligent_escape >= 40 and self.level >= 10 and self.level <= 15:
            print("You've managed to outwit the horde, even though you failed to outrun them.")

            horde += 1
            hh = 0
        
        elif intelligent_escape >= 70 and self.level > 15:
            print("You've managed to outwit the horde, even though you failed to outrun them.")

            horde += 1
            hh = 0

        else:
            if intelligent_first == True:
                self.failed_genius()
            else:
                print("You're not smart enough to outwit the horde, and sick of your games, they rip you apart... Sorry.")

                hh = 0
                time.sleep(10)
                exit()

    #This function is to execute a different scenerio if the player is to fail escaping from enemy horde. 
    def failed_runner(self):    
        print("You've failed to escape from the horde\n")
                                
        while hh > 0:
            print("Your current health is:", health)

            player_action = input("What do you want to do? ")
                                    
            #This if statement is used to see what the palyer wants to do after they had failed their "flight". 
            if player_action == attack_dic[melee_attacks] or attack_dic[spell_attacks]:
                #Damage from the players to the horde
                self.player_dmg()
                hh -= p1_dmg
                self.enemy_move()
            
            #This if statement is used to determine if the player wants to use their wits to talk their way out of defeating this horde, and whats to happen if they fail.
                #The difference with the previous if statemetnts of this genre is that instead of being given another opportunity, its either they outwit the horde, or they end up dying. 
            
            if player-action == attack_dic[intelligence]:
                #This will call the intelligence function that will execute the probabilities of success depending on the player's statistics. 
                self.intelligence_func()
            
            elif player_action == attack_dic[surrender]:
                print("You've accepted your fate")
                                    
                time.sleep(2)
                exit()
        horde += 1
            
    #This function is used to determine what is to occur if the player wants to run away from the enemy horde. 
    def runner(self):
        if skills["Stamina"] + 10 > skills["Speed"]:
            escape_prob_stamina = (random.randint(1,5) * self.speed)
            
            if escape_prob_stamina >= 20 and self.player < 5:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            elif escape_prob_stamina >= 30 and self.player < 10 and self.player >= 5:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            elif escape_prob_stamina >= 50 and self.player >= 10 and self.player <= 15:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            elif escape_prob_stamina >= 75 and self.player > 20:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            #This else statement is used to determine what the player is able to do when they're eventually caught up by the horde if they're not lucky enough to get meet the escape probability. 
            else:
                self.failed_runner()
        else:
            escape_prob = (random.randint(1,5) * self.speed)
         
            #Depending on the level of the player, a different if statement is going to be executed which allows the difficulty of the game to scale with the player.
            if escape_prob >= 15 and self.player < 5:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            elif escape_prob >= 25 and self.player < 10 and self.player >= 5:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            elif escape_prob >= 45 and self.player >= 10 and self.player <= 15:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1

            elif escape_prob >= 70 and self.player > 15:
                print("You've succesfully run away from the horde")
            
                hh = 0
                horde += 1
            else:
                self.failed_runner()

    #This function is the actual algorithm that will determine the outcome of the fight, as well as when it will occur. 
    def algorithm_fun(self):
        while end != False:
            if battle == True:
                #These functions will be called to initialize the functions, and set the algorithm in motion.
                self.horde_health()
                self.resistance()

                #The while loop is here to constantly repeat as the hordes are alive. 
                while hh > 0:
                    #The health varaible here refers to the health of the player.
                    if health <= 0:
                        print("You died, better luck next time.")

                        hh = 0
                        exit()
                    elif health > 0:
                        print("Your current health is", health, "and the hordes is", hh, "\n")
                        player_action = input("What do you want to do? ")
                        
                        if player_action == attack_dic[melee_attacks] or attack_dic[spell_attacks]:
                            #Damage from the players to the horde
                            self.player_dmg()
                            hh -= p1_dmg
                            self.enemy_move()
                        #This conditional statement is used to determine what is to occur when a player wants to do an action that relates to running away. 
                        elif player_action == attack_dic[flight]:
                            self.runner()

                        #This else if statement is used to determine if the player wants to use their wits to beat the horde rather than just running away or fighting them. 
                        elif player_action == attack_dic[intelligence]:
                            intelligent_first = True
                            self.intelligence_func()

                time.sleep(450)
                fight = 0
                battle = False
            else:
                time.sleep(300)
                fight = 0
                algorithm()

#This function is used to initalize the character creation, and set the circumstances for a battle and the algorithm to start in motion. 
def game_start():
    character_creation()
    player_type()

    fighting()

game_start()