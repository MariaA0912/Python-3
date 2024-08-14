last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#create a list called subjects and fill with classes: physics, calculus, poetry, history
subjects = ["physics", "calculus", "poetry", "history"]

#create a list called grades and fill with scores: 98, 97, 85, 88
grades = [98, 97, 85, 88]

#manually create a 2-D list to combine subjects and grades. Assign into variable called gradebook
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#print gradebook
#print(gradebook)

#use .append() method to add a list with the values of "computer science" and an associated grade value of 100 to the 2-d gradebook
gradebook.append(["computer science", 100])

#append ["visual arts", 93] to gradebook
gradebook.append(["visual arts", 93])

#print(gradebook)

#switch from numerical grade value to Pass/Fail option for poetry class

#remove grade value using .remove()
gradebook[2].remove(85)

#use .append() method to then add new "Pass"

gradebook[2].append("Pass")

#print(gradebook)

#grades from last semester stored in last_semester_gradebook

#create new variable fill_gradebook

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
