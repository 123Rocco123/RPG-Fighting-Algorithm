import random
import time

attack_dic = {melee_attacks : ["hit", "attack", "melee", "rage", "slash", "thrust"], spell_attacks : ["spell", "cast", "bewitch"]}

enemy_ac = " "
level = 1
bonus_dmg = level + random.randint(1,20)

PLACEHOLDER = 4

battle = False

enemy_grunt = 500
enemy_health_boss = 1000
big_bad = 5000

danger = 1


def algorithm():
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
                if EnemyHealth <= 0:
                    print("You've defeated the enemy!")
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