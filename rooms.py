from items import get_items, describe_items
current_room = None
room_id_dict = {}

class Room:
    def __init__(self, name, description, visited=False,):
        self.name = name
        self.description = description
        self.exits = {}
        self.visited = visited
        self.items = []
        self.enemies = []
        
def enter_room(room):
    global current_room
    current_room = room
    describe_room()
    
def describe_room():
    global current_room
    if(current_room.visited == False):
        print(current_room.name)
        print(current_room.description)
        current_room.visited = True
    else:
        print(current_room.name)
    if(len(current_room.items) != 0):
        describe_items(current_room.items)
    
def get_rooms():
    list1 = []
    global room_id_dict
    rooms = open("rooms.txt","r")
    rooms.readline()
    
    for line in rooms:
        record= line.split(",")
        
        new = Room(record[1],record[2])
        room_id_dict[str(record[0])] = new
        list1.append(new)
        
        #add exits
        exits = record[3].split(";")
        for dirs in exits:
            new.exits[dirs.split(":")[0]]=dirs.split(":")[1].replace("\n","")
        #add items
        items = record[4].split(":")
        if(len(items) > 0):
            new.items = get_items(items)  
        
    return list1

def execute_go(direction):
    global current_room
    room_exits = current_room.exits
    try:
        request = room_exits[direction]
        room = room_id_dict[request]
    
        if room:
            print("Du gehst nach %s" %direction)
            enter_room(room)
        else:
            raise KeyError
    except:
        print("Du kannst nicht nach %s gehen." % direction)