import random

#Setting up variables
name = "Camila"
question = "What is the meaning of life?"
answer = ""

random_number = random.randint(1,15)

# 8 ball messages
if random_number == 1:
  answer = "Yes - definitely"

elif random_number == 2:
  answer = "It is decidedly so"

elif random_number == 3:
  answer = "Without a doubt"

elif random_number == 4:
  answer = "Reply hazy, try again"

elif random_number == 5:
  answer = "Ask again later" 

elif random_number == 6:
  answer = "Better not tell you now"

elif random_number == 7:
  answer = "My sources say no"

elif random_number == 8:
  answer = "Outlook not so good"

elif random_number == 9:
  answer = "Very doubtful"

elif random_number == 10:
  answer = "NO!"

elif random_number == 11:
  answer = "Maybe...."

elif random_number == 12:
  answer = "YES!"

elif random_number == 13:
  answer = "Emptiness..."

elif random_number == 14:
  answer = "I don't think so..."

elif random_number == 15:
  answer = "There is nothing to say about this."
else:
  answer = "Error"
  
#if name is empty then print out "Question: ..." else name + " asks: "
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

#if question is empty then print out statement else print out 8-balls answer
if question == "":
  print("No fortune for you my friend!")
else:
  print("Magic 8 Ball's answer: " + answer)
