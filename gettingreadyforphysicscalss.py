# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

#function f_to_c that tales input f_temp should return c_temp
#function Temp(C) = (Temp(F)-32) * 5/9
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9

  return c_temp

#test function with 100 Fahrenheit
f100_in_celcius = f_to_c(100)

#print(f100_in_celcius)

#write function c_to_f that takes an input c_temp convert f_temp 
#function Temp(F) = Temp(C) * (9/5) + 32
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#test with value of 0 celcius
c0_in_fahrenheit = c_to_f (0)

#print(c0_in_fahrenheit)

#define function get_force that takes mass & acceleration
def get_force(mass, acceleration):
  return mass * acceleration

#saving result called train_force test get_force by calling function and using train_mass and train_acceleration
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

#define function get_energy that takes mass and c
#set c to default 3*10**8

def get_energy(mass, c = 3*10**8):
  return mass * (c**2)

#test get_energy
bomb_energy = get_energy(bomb_mass)

#print a statement
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#define get_work that takes mass, acceleration, & distance 
#work = force * distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  result = force * distance
  return result

#Test get_work using train_mass, train_acceleration and train_distance save in train_work var
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over Y meters.")

