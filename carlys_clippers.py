hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#create a variale total_price and set to 0
total_price = 0
#create variable average_price
average_price = 0
#loop through the prices list and add each price to the variable total_price
for price in prices:
  total_price += price

average_price = total_price / len(prices)

#print average_price with "Average Haircut Price: "
print("Average Haircut Price: " + str(average_price))

#cut prices by 5 dollars
new_prices = [price - 5 for price in prices]

print(new_prices)

#Revenue:

#create a variable called total_revenue set to 0
total_revenue = 0

#use for loop to create var i that goes from 0- len(hairstyles)

for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i]

print("Total Renenue: " + str(total_revenue))

#find average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))

#create list called cuts_under_30 
cuts_under_30 = [hairstyles [i] for i in range(len(new_prices)-1) if new_prices[i] < 30]

print(cuts_under_30)
