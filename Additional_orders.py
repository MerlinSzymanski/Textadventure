import time
from rooms import get_current_room, get_room_id_dict

def execute_say(words):
    current_room = get_current_room()
    print("You say '"+words+"'")
    print("")
    time.sleep(2)
    if(len(current_room.enemies) != 0):
        if(current_room == get_room_id_dict()["R6"]):
            conversation_loop1(words)
    else:
        print("Nothing happens, there is no one here")

def conversation_loop1(text):
    print("***You are in conversation with the Guard***")
    print("***To leave enter 'leave'***")
    while text.strip() != "leave":
        bool1 = go_into_conversation1(text)
        if(bool1 == False):
            break
        text = input("you say: ")
    print("you left the conversation")
    
def go_into_conversation1(text):

    
    current_room = get_current_room()
    enemy = current_room.enemies[0].name
    mood = current_room.enemies[0].mood
    
    words = text.split(" ")
    if(words[0] in ("hello","greetings","good","cheers")):
        print(enemy+" says 'Hello to you'")
    if(words[0] == ("how")):
        if(words[-1] in ("doing","mood","feeling","you")):
            print(enemy +" says: 'Well' ...")
            if(mood == 1):
                print ("'... I am really pissed off you! Walking around the area like you are the king of this world. I could just kill you!'")
                print("'But... I have to control myself! You are not so hateable at all...'")
                print(current_room.enemies[0].titel +" smiles")
                mood = 2
            elif(mood == 2):
                print ('"My life is very hard lately... I think, that I have to do something else with me. Being a famous adventurer is not really what I wanted..."')
                print("'you know, I once was a "+current_room.enemies[0].profession+". But this was long ago'")
                question = input("'Do you think I should should do something else?")
                if(question in ("yes","no","maybe")):
                    if(question == "yes"):
                        print("'You are just telling me what I want to hear... This is so classy'")
                        print("please leave me alone'")
                        mood = 1
                    elif(question == "no"):
                        print("'You are right... I should bite myself through!. I have to stop being such a pussy.'")
                        print("'If you need help with something, please let me know!'")
                        print("'Thank you'")
                        print(current_room.enemies[0].titel +" looks happy at you")
                        mood = 4
                    elif(question == "maybe"):
                        print("'Whatever ... thanks anyway'")
                        print(current_room.enemies[0].titel +"looks around, you feel ignored")
                        mood = 3
                else:
                    print(current_room.enemies[0].titel+"looks confused")
                    print("'You are not helpful at all... Maybe I should not have asked you'")
                    print(current_room.enemies[0].titel+"looks around... you feel ignored")
                    mood = 3

            elif(mood == 3):
                print ("'I am dont really want to talk to you... This is so boring!'")
                print ("'please go'")
            else:
                print("'I am just glad you are here!! I am just extremely happy seeing you'")
                print("'How are you feeling today?'")
                answer = input()
                print("you say:'"+answer+"'")
                print("'Magificent! Just amazing! You really are my hero'")
        elif(words[-1] in ("enter","in","castle","through")):
            print(enemy+" looks at you")
            print(current_room.enemies[0].titel+ "says:")
            if(mood == 4):
                print("'I actually wanted to trick you... but you are my friend so I will not. Dont give me the key, I have to destroy it'")
            else:
                print("'Find the key to this door and give it to me. I will let you in then'")
    elif(words[0] in ("please","could","would","let")):
        if(words[-1] in ("enter","in","inside")):
            print(enemy + " says: ")
            print("You could actually help me!")
            time.sleep(3)
            print("I forgot the password for the WLAN and I could really need some distraction")
            print("can you find it for me?")
            password = input("please enter WLAN passwort:")
            if(password == "test123"):
                print(enemy + " says: ")
                print("Thank you very much!!")
                time.sleep(3)
                print("ähhhm... I.. have to go")
                print("dont do anything stupid while i am gone")
                enemy = current_room.enemies[0]
                current_room.enemies.remove(enemy)
                return False
            else:
                print("'This is not the right password...What a shame'")
                print("Come back, when you found it")
    elif(words[-1] in ("password","wlan","test123")):
        password = input("please enter WLAN passwort:")
        if(password == "test123"):
            print(enemy + " says: ")
            print("Thank you very much!!")
            time.sleep(3)
            print("ähhhm... I.. have to go")
            print("dont do anything stupid while i am gone")
            enemy = current_room.enemies[0]
            current_room.enemies.remove(enemy)
            return False
    elif(words[0] == "what"):
        if(words[-1] in ("doing","to")):
            print("'I am guarding this door'")
            print("'You may not enter!'")