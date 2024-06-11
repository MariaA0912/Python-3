#Reciepts for Lovely Loveseats
#Created 06-11-2024

lovely_loveseat_description = '''
Lovely Loveseat. Tufted Polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. 
'''
#create a price for the loveseat and set to 254.00

lovely_loveseat_price = 254.00

#extend inventory with another characteristic piece of furniture

stylish_settee_description = '''
Stulish Settee. Faux leather on birch. 
29.50 inches high x 54.75 inches wide x 28 inches deep. Black. 
'''

#set the price for Stylish Settee

stylish_settee_price = 180.50

#add one more item...

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''
#set a price for Luxurious Lamp

luxurious_lamp_price = 52.15

#sales tax 8.8%
sales_tax = 0.088

#first customer
customer_one_total = 0

#list of descriptions of things they're purchasing
customer_one_itemization = ""

#purchase Lovely Loveseat 
customer_one_total += lovely_loveseat_price

#keeping track of items purchased
customer_one_itemization += lovely_loveseat_description

#purchased Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#calculate customer 1 tax
customer_one_tax = customer_one_total * sales_tax

#add tax to total
customer_one_total += customer_one_tax

#print out heading for their itemization
print("Customer One Items:")
#print itemization
print(customer_one_itemization)
#add heading for total cost
print("Customer One Total: ")
#print out total
print(format(customer_one_total, '.2f'))
