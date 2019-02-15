from rooms import get_rooms, enter_room, execute_go, examine_room
from items import get_item_names, describe_items, get_item_name_dict
from player import get_player

import time
list_of_rooms = get_rooms()
player1 = get_player()

def play():
    print("*************WELCOME******************")
    print("You are walking down a path...")
    time.sleep(1)
    enter_room(list_of_rooms[0])
    while execute_command():
        pass

def execute_command():
    words = read_command()
    
    if(len(words) != 0):
        if (words[0] in ("go", "enter")):
            execute_go(words[-1])
            
        elif (words[0] == "help"):
            print("Help will come soon... I promise")
            
        elif (words[0] == "quit"):
            print("Until the next time")
            return False
        
        elif (words[0] == "examine"):
            try:
                if(words[1] in ("room", "place","floor","area")):
                    examine_room()
                elif(words[1] in (get_item_names())):
                    describe_items(words[1])
                else:
                    print("What do you want to examine?")
            except IndexError:
                print("what do you want to examine?")
        
        elif(words[0] == "take"):
            if(words[-1] in (get_item_name_dict())):
                player1.take_item(words[-1].strip())
            else:
                print("What do you want to take?")
        
        elif(words[0] == "drop"):
            item_name_dic = get_item_name_dict()
            try:
                item = item_name_dic[words[-1].strip()]
                if(item in player1.inventory):
                    player1.drop_item(item)
                else:
                    print("This Item is not in your inventory")
            except KeyError:
                print("There is no Item with that name")
        
        elif(words[0] in ("inventory", "i")):
            player1.show_inventory()
            
        else:
            print("I dont understand: '%s'" % " ".join(words))
    return True

def read_command():
    word = input(": ")
    return word.strip(".?!").split(" ")

play()


