from rooms import get_rooms, enter_room, execute_go
list_of_rooms = get_rooms()

# the current room

def play():
    enter_room(list_of_rooms[0])
    while execute_command():
        pass

def execute_command():
    words = read_command()
    
    if(len(words) != 0):
        if (words[0] in ("gehe", "geh", "nach")):
            if (len(words) > 2 and words[1] == "nach"):
                execute_go(words[2])
            elif (len(words) == 2):
                execute_go(words[1])
            else:
                print("Wohin soll ich gehen?")
        elif (words[0] == "ende"):
            print("Bis zum nächsten Mal")
            return False
        else:
            print("Ich verstehe '%s' nicht." % " ".join(words))
    return True

def read_command():
    word = input(": ")
    return word.strip(".?!").split(" ")

play()


