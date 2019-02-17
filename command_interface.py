import time
from rooms import get_current_room, examine_room,change_room
from items import get_item_names, describe_items
from enemies import hug_enemy, examine_enemy

area_synonym_dict = {"enter":"go", "go":"go","move":"go","run":"go","look":"examine",
                     "examine":"examine","check":"examine","analyze":"examine",
                     "inspect":"examine","study":"examine","leave":"leave"}
item_synonym_dict = {"examine":"examine","check":"examine","analyze":"examine","look":"examine",
                     "inspect":"examine","study":"examine","show":"examine",
                     "destroy":"destroy","kill":"kill",
                     "take":"take", "pick":"take","store":"take",
                     "drop":"drop", "leave":"drop",}
enemy_synonym_dict = {"examine":"examine","check":"examine","analyze":"examine",
                     "inspect":"examine","study":"examine","look":"examine", "hug":"hug","love":"hug",
                     "attack":"attack","kill":"attack","trade":"trade"} 


#Hier soll geschaut werden, ob das Subjekt mit de Raum zusammenhängt. Also z.B. "examine forrest"
#"forrest" soll erkannt werden und das verb "examine" in diesem Kontext gewertet werden               
def check_room_subject(subject):
    subject_list = ["area","room","place","level","around"]
    name_list = get_area_names()
    exit_list = get_exit_names()
    subject_list.extend(name_list)
    subject_list.extend(exit_list)
    if(subject in subject_list):
        return True
    else:
        return False

#Hier kommen nun Befehle, die man mit der Umgebung machen kann
def execute_room_command(command, subject):
    if(command in area_synonym_dict):
        command = area_synonym_dict[command]
        if(command == "examine"):
            examine_room()
        elif(command == "go"):
            change_room(subject)
        elif(command in ("leave", "return")):
            print("try: 'go back' or 'go out'")


#Hier soll geschaut werden, ob das Subjekt mit dem Item zusammenhängt. Also z.B. "examine staff"
#"staff" soll erkannt werden und das verb "examine" in diesem Kontext gewertet werden 
def check_item_subject(subject):
    subject_list = ["item","loot","i","inventory"]
    subject_list.extend(get_item_names())
    if(subject in subject_list):
        return True
    else:
        return False
    
def execute_item_command(command, subject, player1):
    if(command in item_synonym_dict):
        command = item_synonym_dict[command]
        if(command == "examine"):
            if(subject in ("i","inventory")):
                player1.show_inventory()
            else:
                describe_items(subject)
            
        elif(command == "take"):
            if(subject in (get_available_items())):
                player1.take_item(subject)
        
        elif(command == "drop"):
            player1.drop_item(subject)
        
        elif(command == "destroy"):
            time.sleep(2)
            print("...this would be stupid...")
            
        elif(command == "kill"):
            print("How am I supposed to do this?")
            
    else:
        print("What do you want to do with the item?")

def check_enemy_subject(subject):
    subject_list = ["enemy"]
    enemy_list = get_enemy_names()
    subject_list.extend(enemy_list)
    if(subject in subject_list):
        return True
    else:
        return False
    
def execute_enemy_command(command,subject,player1):
    if(command in enemy_synonym_dict):
        command = enemy_synonym_dict[command]
        if(command == "examine"):
            examine_enemy(get_current_room())
        elif(command == "hug"):
            hug_enemy(get_current_room())
        elif(command == "attack"):
            print("this function is not yet availabe")
        elif(command == "trade"):
            print("This does not work yet... but the enemy really has to like you")
    else:
        print("what shall I do with the enemy?")
    

def get_area_names():
    current_room = get_current_room()
    name = current_room.name
    name = name.replace("*","")
    words = name.split(" ")
    names_list = []
    for i in range(len(words)):
        if(words[i].lower() == "the"):
            names_list.append(words[i+1].lower())
    return names_list
        
def get_exit_names():
    current_room = get_current_room()
    exit_list = list(current_room.exits)
    return exit_list

def get_available_items():
    current_room = get_current_room()
    room_items = []
    if(len(current_room.items) != 0):
        for item in current_room.items:
            room_items.append(item.name)
    else:
        print("You search for it, but you it seems to be elsewhere")
    return room_items

def get_enemy_names():
     current_room = get_current_room()
     list1 = []
     if(len(current_room.enemies)!= 0):
         enemy = current_room.enemies[0]
         text = enemy.first_description
         text = text.split("*")
         list1.append(text[1].lower())
         names = enemy.name.split(" ")
         list1.extend(names)
         return list1
     else:
         return []
         
    
def execute_special_cases(command):
    if (command == "help"):
        print("Help will come soon... I promise")
        return True
    
    elif(command == "quit"):
        print("thank you for playing")
        print("good bye")
        return False
    