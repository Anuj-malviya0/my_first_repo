print('This is my first program on git hub\n')
print("My name is Anuj Malviya and I'm 17 years old\n")
print('\nPlay rock paper scissor with me\n')
#--------------------------------------------------
from random import *
li = ["rock","paper","scissors"]
print("Available choices\nrock\npaper\nscissors")
result = choice(li)
def judge():
    user = str(input("enter your choice \n"))
    print(result)
    if user == "rock" and result == "paper":
        print("you lost, paper covers rock")
    elif user == "rock" and result == "scissors":
        print("you won, rock breaks scissors")
    elif user == "rock" and result == "rock":
        print ("it's a ty ")
#----------------------------------------------
    elif user == "paper" and result == "rock":
        print ("you won, paper covers rock")
    elif user == "paper" and result == "scissors":
        print ("you lost,scissor cuts paper ")
    elif user == "paper" and result == "paper":
        print ("it's a ty ")
#----------------------------------------------
    elif user == "scissors" and result == "rock":
        print ("you lost, rock breaks scissors")
    elif user == "scissors" and result == "paper":
        print ("you won,scissor cuts paper ")
    elif user == "scissors" and result == "scissors":
        print ("it's a ty ")
    else:
        print("opps something went wrong")

judge()

