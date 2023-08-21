class Business:
  #Constructor
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


class Franchise:
  #Constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #Representation
  def __repr__(self):
    return self.address

  #Time conversion
  def time_conversion(self, time):
    if len(time) == 4:
      if time[2:4] == 'pm':
        time = int(time[0:2]) + 12
      else:
        time = int(time[0:2])
    else:
      if time[1:3] == 'pm':
        time = int(time[0:1]) + 12
      else:
        time = int(time[0:2])
    return time

  #Available Menus
  def available_menus(self, time):
    time = self.time_conversion(time)
    available_op = []
    for menu in self.menus:
      st = self.time_conversion(menu.start_time)
      et = self.time_conversion(menu.end_time)
      print(st, et, time)
      if time <= et and time >= st:
        available_op.append(menu)
    return available_op

#
class Menu:
  #Constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  #Representation
  def __repr__(self):
    return self.name + " menu available from " + self.start_time + " to " + self.end_time

  #Calculate Bill
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price+= self.items[item]
    return total_price


#Brunch Menu
brunch_item = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('brunch', brunch_item, '11am', '4pm')

#Early_bird_menu
early_bird_item = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
early_bird = Menu('early_bird', early_bird_item, '3pm', '6pm')

#dinner_menu
dinner_item = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner = Menu('dinner', dinner_item, '5pm', '11pm')

#kids menu
kids_item =  {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kids', kids_item, '11am', '9pm')

#arepas_menu
arepas_item = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas = Menu('arepas', arepas_item, '10am', '8pm')


print(brunch)

p1 = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(p1)

p2 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(p2)

#---------------------------
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street", menus)

arepas_place = Franchise("189 Fitzgerald Avenue", menus)


print(flagship_store.available_menus('0pm'))
print(flagship_store.available_menus('5pm'))


franchises = [flagship_store, new_installment, arepas_place]

business_1 = Business("Basta Fazoolin' with my Heart", franchises)
business_2 = Business("Take a' Arepa", franchises)
