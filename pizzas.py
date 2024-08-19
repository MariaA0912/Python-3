# Your code below:

#track kinds of pizzas sold using variable called toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies","mushrooms"]

#keep track of cost of each pizza in a list called prices
prices = [2,6,1,3,2,7,2]

#count number of occurrences of 2 in price list, store result in var called num_two_dollar_slices
num_two_dollar_slices = prices.count(2)

#find length of toppings list and store in var num_pizzas
num_pizzas = len(toppings)

#print "We sell [num_pizzas] different kinds of pizza!"
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#create a new two-dimensional list called pizza_and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#print pizza_and_prices
print(pizza_and_prices)

#sort pizza_and_prices in ascending order
pizza_and_prices.sort()

#store first element in pizza_and_prices in a variable called cheapest_pizza
cheapest_pizza = pizza_and_prices[0]

#Get the last item of pizza_and_prices list and store it in a variable called priciest_pizza
priciest_pizza = pizza_and_prices[-1]

#remove priciest pizza 
pizza_and_prices.pop()

# add a pizza [2.5, "peppers"]
pizza_and_prices.insert(4,[2.5, "peppers"])

#save 3 lowest cost pizzas called three_cheapest
three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
