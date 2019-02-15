from rooms import get_rooms, enter_room, execute_go, examine_room
from items import get_item_names, describe_items
import time
list_of_rooms = get_rooms()

# the current room

def play():
    print("*************WELCOME******************")
    print("You are walking down a path...")
    time.sleep(2)
    enter_room(list_of_rooms[0])
    while execute_command():
        pass

def execute_command():
    words = read_command()
    
    if(len(words) != 0):
        if (words[0] == "go"):
            if (len(words) > 2 and words[1] == "to"):
                execute_go(words[2])
            elif (len(words) == 2):
                execute_go(words[1])
            else:
                print("Where shall I go?")
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
        else:
            print("I dont understand: '%s'" % " ".join(words))
    return True

def read_command():
    word = input(": ")
    return word.strip(".?!").split(" ")

play()


