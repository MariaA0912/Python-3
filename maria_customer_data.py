# Your code below: 
#Turn list of curstomer first names into a list
first_names  = ["Ainsley", "Ben", "Chani", "Depak"]

#track all customer's preferred sizes with a list
preferred_size = ["Small", "Large", "Medium"]

#Add Depak's Size
preferred_size.append("Medium")

#Print preferred_size
print(preferred_size)

#Create 2D list called customer_data
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]

#Print customer_data
print(customer_data)

#Change data value for "Chani"'s shipping prefrense to False
customer_data[2][2] = False

#Print customer_data
print(customer_data)

#remove the True or False Value for Ben's data
customer_data[1].remove(False)

#Print customer_data
print(customer_data)

#Add new customer "Amit" and "Karim"

#create new variable customer_data_final
customer_data_final = [["Amit", "Large", True], ["Karim", "X-Large", False]]

#combine customer_data with 2nd list using + (+ should be at the end of customer_data)
customer_data_final = customer_data + customer_data_final 

#print customer_data_final
print(customer_data_final)
