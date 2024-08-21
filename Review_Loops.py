# Your code below:
#create a list called single_digits with numbers 0-9 inclusive
single_digits = list(range(10))

#create a list called squares assign it to be empty
squares = []
#create a for loop that goes through and prints each number
for digits in single_digits:
  print(digits)
  squares.append(digits * digits)

print(squares)

#create a list cubes where each element is an element of single_digits taken to the third power
cubes = [digits * digits * digits for digits in single_digits]

print (cubes)


