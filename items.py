id_item_dict = {}
item_list = []

class Item:
    def __init__(self,name,description,attack,defense,regeneration):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.regeneration = regeneration

def get_items(items):
    global item_list
    global id_item_dict
    
    if(len(item_list) == 0):
        handle = open("Items.txt","r")
        handle.readline()
        for line in handle:
            record = line.split(",")
            new = record[0] 
            new = Item(record[1],record[2],record[3],record[4],record[5])
            
            item_list.append(new)
            id_item_dict[record[0]] = new

    part_list = []        
    for item in items:
        if(item not in (""," ")):
            item2 = id_item_dict[item]
            part_list.append(item2)
        
    return part_list

def describe_items(items):
    print("Du siehst die Gegenstände:")
    for item in items:
        print(item.name)
    
            