import time
id_item_dict = {}
item_list = []
item_name_dict = {}
item_place_dic = {}

class Item:
    def __init__(self,name,description,takeable,stats,item_funcs):
        self.name = name
        self.description = description
        self.takeable = bool(takeable)
        self.stats = stats
        self.item_funcs = item_funcs

def get_item_names():
    global item_list
    part_list = []
    for item in item_list:
        part_list.append(item.name)
    return part_list

def get_items(items):
    global item_list
    global id_item_dict
    global item_place_dic
    global item_name_dict
    
    if(len(item_list) == 0):
        handle = open("Items.txt","r")
        handle.readline()
        for line in handle:
            record = line.split(",")
            new = record[0].strip() 
            new = Item(record[1].strip(),record[2].strip(),\
                       record[3].strip(),record[4].strip(),\
                       record[5].strip())
            if(record[3] == "False"):
                new.takeable = False
            
            item_list.append(new)
            id_item_dict[record[0].strip()] = new
            item_name_dict[new.name] = new

    part_list = []        
    for item in items:
        item2 = item.split(":")
        if(item2[0] not in (""," ")):
            item3 = id_item_dict[item2[0]]
            item_place_dic[item3]=item2[1]   #I1 --> Ein Stab lehnt an der Wand
            part_list.append(item3)
        
    return part_list

def describe_items(name):
    print("You take the Item in your hand and look sharp at it")
    time.sleep(2)
    global item_name_dict
    item = item_name_dict[name]
    print(item.description)
    
def get_item_loc():
    global item_place_dic
    return item_place_dic

def get_item_name_dict():
    global item_name_dict
    return item_name_dict        