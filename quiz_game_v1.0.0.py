# Quiz Game version 1.0.0
import time
from PIL import Image

#----------Full Score----------#
def full():
    if score == 5:
        print("Congratulations! You have 5/5!\nYou have passed the quiz!")
    else:
        print("Your score is " + str(score) + "/5")
#--------------------------------#

print("\nWelcome to the Quiz game!")

play = input("Do you want to play? ")

if play.lower() == "yes" or play.lower() == "yeah":
    print("Great! Let's start!")

else:
    quit()
score = 0

time.sleep(1)
question = input("\nWhat does ROM stand for? ")
if question.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


question = input("\nWhat color is often a very high quality motherboard? ")
if question.lower() == "grey" or question.lower() == "black":
    time.sleep(1)
    print("That is correct.")
    score += 1
else:
    print("Incorrect!")
    

question = input("\nWho invented the first computer? ")
if question.lower() == "charles babbage" or question.lower() == "babbage":
    time.sleep(1)
    print("Correct...")
    time.sleep(0.7)
    print("I hope you aren't using google...")
    time.sleep(2)
    score += 1
else:
    print("Incorrect!")


question = input("\nWho was the first known computer programmer? ")
if question.lower() == "ada lovelace" or question.lower() == "lovelace":
    time.sleep(1)
    print("You are definitely using google!")
    time.sleep(1.2)
    print("...")
    time.sleep(1.5)
    print("ALRIGHT THEN")
    time.sleep(1)
    print("IF YOU WANNA PLAY DIRTY")
    time.sleep(1)
    print("WE WILL PLAY DIRTY")
    time.sleep(1.5)
    score += 1
    #-----------------LAST QUESTION------------------#
    print("\nLAST QUESTION\n")
    time.sleep(2)
    last_question = input("What have I got in my pocket?\nYou have 3 guesses. ")
else:
    print("Incorrect!")
    time.sleep(2)
    print("\nYour score is " + str(score) + "/5")
    quit()

#___________________HELP___________________

while last_question.lower() != "a ring" and last_question.lower() != "the ring":
    last_question = input("Wrong! Guess again. ")
    if last_question.lower() != "a ring" and last_question.lower() != "the ring":
        last_question = input("Wrong again. Last guess. ")
    if last_question.lower() != "a ring" and last_question.lower() != "the ring":
#image (gif link: https://tenor.com/view/lotr-gollum-times-up-gif-14341656)
        im = Image.open("lotr-gollum.png")
        im.show()
        break
else:
    score += 1
    time.sleep(2)
    print("Okay, you win.")
    time.sleep(1)
    
    



#___________________________________________

#----------Full Score----------#
if score == 5:
    print("Congratulations! You have 5/5!\nYou have passed the quiz!")
else:
    print("\nYour score is " + str(score) + "/5")
    
    


