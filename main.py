#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random 
from art import logo
import os
def PlayGame():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  NumberRange = [int(input("The range you want, starting with the smallest number: ")), int(input("The largest number: ")) ]
  
  Dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  NumberOfLives = 0
  if Dificulty == "hard":
    NumberOfLives = 5
  else: NumberOfLives = 10
  RandomNumber = random.randint(NumberRange[0],NumberRange[1])
  print(RandomNumber)
  
  NumberGussed = False
  while not NumberGussed:
    if NumberOfLives > 0:
      print(" ")
      print(f"You have {NumberOfLives} attempts remaining to guess the number.")
      Guess = int(input("Guess the number: "))
      if Guess > RandomNumber:
        NumberOfLives -= 1
        print("Too high")
      elif Guess < RandomNumber:
        NumberOfLives -= 1
        print("Too low")
      else:
        print("You Won!")
        NumberGussed = True
    else:
      print("You've run out of guesses, you lost.")
      NumberGussed = True
    

PlayGame()
Play = input("Would you like to play again? type yes or no:")
if Play == "yes":
  os.system('clear')
  PlayGame()
else:
  print("Thanks for playing!")