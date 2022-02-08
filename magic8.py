#  magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
# the name of the person who will be asking the Magic 8-Ball.
name = "Yassine"
# question you’d like to ask the Magic 8-Ball.
question = "Will the Seahawks win the superbowl next year"
# store the answer of the Magic 8-Ball in another variable
answer = ""
# importing randowm to generate answer
import random
# a variable to store the randomly generated value
random_number = random.randint(1, 9)
print(random_number)
#  assign different answers for each randomly generated value.
if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2: 
  print("It is decidedly so.")
elif random_number == 3: 
  print("Without a doubt.")
elif random_number == 4: 
  print("Reply hazy, try again.")
elif random_number == 5: 
  print("Ask again later.")
elif random_number == 6: 
  print("Better not tell you now.")
elif random_number == 7: 
  print("My sources say no.")
elif random_number == 8: 
  print("Outlook not so good.")
elif random_number == 9: 
  print("Very doubtful.")
else:
  print("Error")
# statement to output the asker’s name and their question
print(name + " asks: " + question)
# statement that will output the Magic 8-Ball’s answer
print("Magic 8-Ball's answer: " + answer)
