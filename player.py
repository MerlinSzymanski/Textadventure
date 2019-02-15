from rooms import get_current_room
from items import get_item_name_dict

class Player:
    def __init__(self):
        self.health = 10
        self.strength = 2
        self.inventory = []
        self.equipped = []

    def take_item(self,name):
        if(len(self.inventory) <= 5):
            item_name_dict = get_item_name_dict()
            item = item_name_dict[name]
            if(item.takeable == True):
                self.inventory.append(item)
                print("you placed the "+str(item.name)+" in your inventory")
                print("you have "+ str(5- len(self.inventory))+" more free slots in it")
            else:
                print("You cant take this item")
        else:
            print("Your inventory is full... please remove an item first")
        
    def show_inventory(self):
        if(len(self.inventory)==0):
            print("Your inventory is empty")
        else:
            print("You have the following Items in your Inventory:")
            for item in self.inventory:
                print(item.name)
    
    def drop_item(self, item):
        current_room = get_current_room()
        self.inventory.remove(item)
        current_room.items.append(item)
        print("you dropped the "+item.name)
        
def get_player():
    player1 = Player()
    return player1     