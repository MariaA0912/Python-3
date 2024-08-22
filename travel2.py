#create a function called trip_planner_welcome() that takes 1 parameter called name
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 "+ name)

#call function with a name as an argument
trip_planner_welcome("Maria")

#define a function called estimated_time_rounded() with estimated_time as its only parameter
def estimated_time_rounded(estimated_time):
  #create var rounded_time using built-in round() and using estimated_time as a parameter
  rounded_time = round(estimated_time)

  #return rounded_time
  return rounded_time


estimate = estimated_time_rounded(2.5)

#function destination_setup with 4 given parameters
def destination_setup(origin, destination, estimated_time, mode_of_transport= "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately "+ str(estimated_time) + " hours")

destination_setup("United States", "Italy", estimate)



