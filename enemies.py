import random
import time

name_enemy_dict = {}

class Human_Enemy():
    def __init__(self, first_description):
        #Stats
        self.first_description = first_description
        self.name = "human"
        self.titel = "it"
        self.profession = "adventurer"
        self.health = random.randint(7,10)
        self.strength = random.randint(2,4)
        self.mood = random.randint(1,4)
        self.alive = True
            
        #A cool random name from random list
        name_text = open("names.txt")
        name_list = name_text.readlines()
        global name_enemy_dict
        
        #No enemy twice
        loop1 = True
        while loop1:
            index = random.randint(0,len(name_list)-1)
            self.name = name_list[index].replace("\n","").strip()
            if(self.name not in name_enemy_dict):
                loop1 = False
    
        #Gender
        self.titel = None
        self.gender = random.randint(1,3)
        if(self.gender == 1):
            self.titel = "she"
        elif(self.gender == 2):
            self.titel = "he"
        else:
            self.titel = "it"
        
        #former profession
        profession_text = open("professions.txt")
        profession_list = profession_text.readlines()
        index = random.randint(0,len(profession_list)-1)    
        self.profession = profession_list[index].replace("\n","").strip() 

def get_enemy(description):
    global name_enemy_dict
    enemy1 = Human_Enemy(description)
    name = enemy1.name.split(" ")
    name_enemy_dict[name[0]] = enemy1
    name_enemy_dict[name[1]] = enemy1
    return enemy1
    
def examine_enemy(room):
    enemy = get_enemy_class(room)
    if(enemy):
        print("Two legs, one head... clearly, its a Human")
        time.sleep(1)
        print("A famous one too ... the Humans name is "+ enemy.name)
        print("Before becoming a well known adventurer, this Human worked as " \
          + enemy.profession)    
        time.sleep(2)
        print("Hmmm...what else...")        
        
        if(enemy.gender == 1):
            print ("I am not sure, but I think she is a woman")
        elif(enemy.gender == 2):
            print ("He looks like a male, but who knows...")
        else:
            print("It doesnt know its gender...")

        if(enemy.mood == 1):
            print ("And %s is really mad at you" % enemy.titel)
        elif(enemy.mood == 2):
            print ("And %s is annoyed by the life of an adventurer" % enemy.titel)
        elif(enemy.mood == 3):
            print ("And %s is quite bored by the situation" % enemy.titel)
        else:
            print(enemy.name + " is extremely happy seeing you")
    
        print (" ")
        time.sleep(2)
        print("According to my data, "+ enemy.name + " has the following stats: ")
        print("Strength: "+ str(enemy.strength))
        print("Health: " + str(enemy.health)) 
        
def show_stats():
    enemy = get_enemy_class()
    if(enemy):
        print("According to my data, "+ enemy.name + " has the following stats: ")
        print("Strength: "+ str(enemy.strength))
        print("Health: " + str(enemy.health))
        if(enemy.mood == 1):
            print("Mood: Mad")
        elif(enemy.mood == 2):
            print("Mood: Annoyed")
        elif(enemy.mood == 3):
            print("Mood: Bored")
        else:
            print("Mood: Happy")
        print(" ")
            
def hug_enemy(room):
    enemy = get_enemy_class(room)
    if(enemy):
        print("You hug "+enemy.name)
        time.sleep(2)
        enemy.mood = 4
        print(enemy.name + " is surprised")
        print("%s hugs you back" % enemy.titel)
        print("%s is extremely happy" % enemy.titel)
        print(" ")

def get_enemy_class(room):
    current_room = room
    if(len(current_room.enemies)!= 0):
        return current_room.enemies[0]
    else:
        print("There is no one here")
        return False
        







