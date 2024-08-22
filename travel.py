#initializing a variable current_budget
current_budget = 3500.75

#define a function print_remaining_budget with input variable budget
def print_remaining_budget(budget):
  #printing out the remaining budget
  print("Your remaining budget is: $" + str(budget))

#calling function
print_remaining_budget(current_budget)

# Write your code below: 

#create a new function deduct_expense() with two parameters budget and expense
def deduct_expense(budget, expense):
  return budget - expense

#Create a variable shirt_expense
shirt_expense = 9

#create variable called new_budget_after_shirt
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

#want users to see the remaining budget
print_remaining_budget(new_budget_after_shirt)
