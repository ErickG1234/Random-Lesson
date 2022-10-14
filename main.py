from random import randint
from random import shuffle
# random
# Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
#show you two useful functions for now.
print("random")
dice1 = randint(1,7)
print(f"dice1 : {dice1}")
dice2 = randint(1,7)
print(f"dice2 : {dice2}")
rolled_doubles = dice1 == dice2
if rolled_doubles:
  print("You rolled dobules! ")

  # create a way to roll snake eyes
  if dice1 and dice2 == 1:
    print("You rolled snake eyes! ")
  else: print("You did not roll snake eyes. ")
# from random import shuffle
# # This shuffles the list "in-place" meaning it won't return
# # anything, instead it will effect the list passed
my_list = range(1,51)
print("My new List: ")
print(list(my_list))
my_list = list(my_list)
shuffle(my_list) #Should work alone 
print(my_list)

random = randint(1,201)
print("Random number: ")
print(random)

if random % 2 == 0:
  print("Your number is even! ")
else: print("Your number is odd. ")
  


  
# shuffle(mylist)
# mylist
  
# [40, 10, 100, 30, 20]
# from random import randint
# # Return random integer in range [a, b], including both end points.
# randint(0,100)
# 25
  
  
# # Return random integer in range [a, b], including both end points.
# randint(0,100)
# 91
  
  
  
################################################random in python#################################################
# Random Practice #1
# Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.
  
  
# Random Practice #2
# Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.
  
  
# Random Practice #3
# Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.
  
# names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
  
  
