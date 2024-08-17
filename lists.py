inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#Jiho wants to know how many items are in the warehouse
inventory_len = len(inventory)

#select first item in inventory and save in var called first
first = inventory[0]

#select the last element from inventory save to var called last
last = inventory[-1]

#selet items from inventory starting at index 2-6 not including 6
#save answer to a variable called invenotry_2_6
inventory_2_6 = inventory[2:6]

#select first 3 items of inventory. Save in var called first_3
first_3 = inventory[:3]

#how many 'twin bed' are in inventory save to twin_beds
twin_beds = inventory.count("twin bed")

#remove the 5th element in the inventory save to removed_item
removed_item = inventory.pop(4)

#add a new item called "19th Century Bed Frame" 
inventory.insert(10,"19th Century Bed Frame")

#sort inventory 
inventory.sort()

#print inventory 
print(inventory)

