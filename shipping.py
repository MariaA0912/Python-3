#Program to take the weight of a package and determine the cheapest way to ship that package using Sal's Shippers.

#include: ground shipping, ground shipping premium, drone shipping

#variables
weight = 41.5
price_per_pound = 0.00
flat_charge_ground = 20.00
total_price = 0.00
ground_premium = 125.00
#Ground Shipping
if weight <= 2:
  total_price = 0.00
  price_per_pound = 1.50
  total_price = (price_per_pound * weight) + flat_charge_ground
  print("Total Charge: $" + str(total_price))

elif ((weight > 2) and (weight <= 6)):
  total_price = 0.00
  price_per_pound = 3.00
  total_price = (price_per_pound * weight) + flat_charge_ground
  print("Total Ground Shipping Charge: $" + str(total_price))
  
elif ((weight > 6) and (weight <= 10)):
  total_price = 0.00
  price_per_pound = 4.00
  total_price = (price_per_pound * weight) + flat_charge_ground
  print("Total Ground Shipping Charge: $" + str(total_price))

elif ((weight > 10)):
  total_price = 0.00
  price_per_pound = 4.75
  total_price = (price_per_pound * weight) + flat_charge_ground
  print("Total Ground Shipping Charge: $" + str(total_price))

else:
  print("Error!")

#Premium ground shipping

print("Premium Ground Shipping Cost: $" + str(ground_premium))

#Drone Shipping
if weight <= 2:
  total_price = 0.00
  price_per_pound = 4.50
  total_price = price_per_pound * weight
  print("Total Drone Shipping Charge: $" + str(round(total_price, 2)))

elif ((weight > 2) and (weight <= 6)):
  total_price = 0.00
  price_per_pound = 9.00
  total_price = price_per_pound * weight
  print("Total Drone Shipping Charge: $" + str(round(total_price, 2)))
  
elif ((weight > 6) and (weight <= 10)):
  total_price = 0.00
  price_per_pound = 12.00
  total_price = price_per_pound * weight
  print("Total Drone Shipping Charge: $" + str(round(total_price, 2)))

elif ((weight > 10)):
  total_price = 0.00
  price_per_pound = 14.25
  total_price = price_per_pound * weight
  print("Total Drone Shipping Charge: $" + str(round(total_price, 2)))

else:
  print("Error!")
