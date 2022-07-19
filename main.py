#This program allows the user to pick a number between 1-10 and adds a score of 1 for every right guess then displays the final score
import random

def random_guess():
  rounds = 5
  score = 0
  
  while rounds != 0:
    random_num = random.randint(1, 10)
    user_num = input("Pick your lucky number between 1 and 10: \n")
    user_num = int(user_num)
    
    if user_num == random_num:
      rounds -= 1
      print("You guessed right! The lucky number is " + str(random_num) + "\n" + str(rounds) + " round(s) remaining\n")
      score += 1
      
    else:
      rounds -= 1
      print("Oops! Wrong number. The number was " + str(random_num) + "\n" + str(rounds) + " round(s) remaining\n")

  if score >= 3:
    print("You Scored {} ᕙ(▀̿ĺ̯▀̿ ̿)ᕗ".format(score))
  else:
    print("You Scored {} ( ͡°Ĺ̯ ͡° )".format(score))
    
random_guess()  

'''
while True:
    try:
        user_num = 0
        while user_num > 0 and user_num < 6:  
          user_num = int(input("Pick a num btwn 1-5: "))
          print("Play Game")
        
          
    except ValueError:
        print("This is an unaccepted response, enter a valid value")
        continue
    else:
        break
'''