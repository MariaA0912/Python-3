#create class
class Menu():
  #constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  #string representation method
  def __str__(self):
    match self.name:
      case 'Brunch':
        return "{Menu} is offered at {start_time}am to {end_time}pm".format(Menu = self.name, start_time = self.start_time, end_time = self.end_time)
      case 'Early Bird':
        return "{Menu} is offered at {start_time}pm to {end_time}pm".format(Menu = self.name, start_time = self.start_time, end_time = self.end_time)
      case 'Dinner':
        return "{Menu} is offered at {start_time}pm to {end_time}pm".format(Menu = self.name, start_time = self.start_time, end_time = self.end_time)
      case 'Kids':
        return "{Menu} is offered at {start_time}am to {end_time}pm".format(Menu = self.name, start_time = self.start_time, end_time = self.end_time)
      case ' ':
        return "{Menu} is offered at {start_time}am to {end_time}pm".format(Menu = self.name, start_time = self.start_time, end_time = self.end_time)
  #calculate_bill method with one parameter
  def calculate_bill(self, purchased_items):
    bill = 0.00
    #adding everything up to return bill total
    for item in purchased_items:
        bill += self.items[item]
    return bill    

# create menues
brunch = Menu('Brunch',{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 4 )
early_bird = Menu('Early Bird',{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 3, 6)

dinner = Menu("Dinner",{'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 5, 11)

kids = Menu("Kids",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 9)

#trying out string representation method
print(brunch)

#testing out calculate_bill method
print(str(brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])))

print(str(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])))

#creating franchise class
class Franchise():
  #constructor with 2 parameter
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #string representation
  def __str__(self):
    return "Location address: {address}".format(address = self.address)
  
  def available_menus(self, time):
    self.time = time
    available_menus =[]
    for menu in self.menus:
      if menu.start_time <= self.time <= menu.end_time:
        available_menus.append(menu.name)
    return 'The available menu\'s at this time are: {menus}'.format(menus=", ".join(available_menus))

#creating first 2 franchises
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])
  
print(flagship_store)

#available_menus() is not working properly, will come back to fix later. 
print(flagship_store.available_menus(5))

