from items import get_items, describe_items, get_item_loc
import time
from enemies import get_enemy

current_room = None
room_id_dict = {}
item_location_dic = get_item_loc()
enemy_location_dic = {}

class Room:
    def __init__(self, name, description, description_short, description_items,\
                 visited=False, items_descr = False):
        self.name = name
        self.description = description
        self.description_short = description_short
        self.description_items = description_items
        self.exits = {}
        self.closed_exits = {}
        self.visited = visited
        self.items = []
        self.enemies = []
        self.items_descr = items_descr
        
def enter_room(room):
    global current_room
    current_room = room
    describe_room()
    
def describe_room():
    global current_room
    if(current_room.visited == False):
        print(current_room.name + "\n")
        print(current_room.description)
        current_room.visited = True
    else:
        print(current_room.description_short)
    
def get_rooms():
    list1 = []
    global room_id_dict
    rooms = open("Texts/rooms.txt","r")
    rooms.readline()
    
    for line in rooms:
        record= line.split(",")
        
        new = Room(record[1].strip(),record[2].strip(),\
                   record[3].strip(),record[4].strip())
        room_id_dict[str(record[0].strip())] = new
        list1.append(new)
                
        #add exits
        record5 = record[5].strip()
        exits = record5.split(";")
        for dirs in exits:
            order = dirs.split(":")[0]
            room = dirs.split(":")[1]
            if(order.startswith("CLOSED")):
                new.closed_exits[order.replace("CLOSED","")] = room.replace("\n","")
            else:
                new.exits[order]=room.replace("\n","")
        #add items
        record6 = record[6].strip()
        items = record6.split(";")
        if(len(items) > 0):
            new.items = get_items(items)  
        #add enemy:
        record7 = record[7].strip()
        temp = record7.split(":")
        if(temp[0] not in (""," ")):
            number_of_enemies = int(temp[0])
            
            for i in range(number_of_enemies):
                new.enemies.append(get_enemy(temp[1]))
            
    return list1

def change_room(direction):
    global current_room
    room_exits = current_room.exits
    room_closed = current_room.closed_exits
    try:
        if(direction in room_exits):
            request = room_exits[direction]
            room = room_id_dict[request]
    
            if room:
                print("you move from this place")
                print(" ")
                enter_room(room)
        elif(direction in room_closed):
            if(not check_for_enemy()):
                print("You cant enter this place, it is locked")
        else:
            raise KeyError
    except:
        print("There is no path in that direction")
        
def examine_room():
    print("You look around")
    time.sleep(1)
    
    global current_room
    global item_location_dic
    
    print(current_room.description_short)
    if(current_room.items_descr == False):
        print(current_room.description_items)
        current_room.items_descr = True
    if (len(current_room.items) != 0):
        for item in current_room.items:
            print(item_location_dic[item])
    if (len(current_room.enemies)!=0):
        for enemy in current_room.enemies:
            print(enemy.first_description.replace("*",""))
      
def unlock_room(subject, player1):
    global current_room
    room_exits = current_room.exits
    room_closed = current_room.closed_exits
    if(subject in room_exits):
        print("The path is already cleared. please enter")
    elif(subject in room_closed):
        if(not check_for_enemy()):
            for item in player1.inventory:
                if(len(item.opens) >= 2):
                    if(room_closed[subject] == item.opens):
                        for order in list(room_closed):
                            if(room_closed[order] == item.opens):
                                del room_closed[order]
                                room_exits[order] = item.opens

                        print("You unlocked the room")
                        print("You may now enter")
                        return True
        print("You cant unlock the Room")
    else: 
        print("I dont know what to do")
        
def check_for_enemy():
    global current_room
    global room_id_dict
    if(len(current_room.enemies) != 0):
        if(current_room == room_id_dict["R6"]):
            print("You hear a 'Hrrrrm Hrrrm'")
            time.sleep(5)
            print(str(current_room.enemies[0].name) + " says: ")
            print("Please dont ignore me... I cant let you go there. That is what guards are for")
            return True
        else:
            print("There is an enemy here")
    return False


def get_current_room():
    global current_room
    return current_room

def get_room_id_dict():
    global room_id_dict
    return room_id_dict