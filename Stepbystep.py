from rooms import get_rooms, enter_room
from player import get_player
from command_interface import check_room_subject, execute_room_command, check_item_subject, execute_item_command,execute_special_cases,check_enemy_subject,execute_enemy_command

import time

list_of_rooms = get_rooms()
player1 = get_player()

def play():
    print_welcome()
    enter_room(list_of_rooms[0])
    while execute_command():
        pass

#
def execute_command():
    words = read_command()
    
    if(len(words) != 0):
        command = words[0]
        if(len(words) > 1):
            subject = words[-1]
    
            if(check_room_subject(subject)):
                execute_room_command(command, subject)
    
            elif(check_item_subject(subject)):
                execute_item_command(command, subject, player1)
            
            elif(check_enemy_subject(subject)):
                execute_enemy_command(command,subject,player1)

            else:
                print("I dont understand: '%s'" % " ".join(words))
        
        elif(command in ("help","quit")):
            return execute_special_cases(command)
            
        else:
            print("please type in two words")

    return True

def read_command():
    word = input(": ")
    return word.strip(".?!").split(" ")

def print_welcome():
    print("***Welcome to this little Adventure***")
    print("")
    print("please type: 'help' any time to get help with the game\n How to play: Please type in your commands in only two words!\n\n \
          For example: \n go west\n examine area \n show inventory \n \n If you feel save with a solution you got, try other words before trying another solution\n")
    print("To end the game type 'quit'. There is no possibility to save the game")
    print("")
    print("**************************************")
    time.sleep(7)

play()


