import random

rock ='''
    ________
----'   _____)
        (_____)
        (______)
        (_____)
----,_______)        
'''
paper = '''
    ________
----'   _____)___
        _________)
        ___________)
        _________)
----,_______)   
     
'''
scissors = '''
    ________
----'  (____)____
        _________)
        ___________)
____,  (____)
      (____)        

'''
game_images =[rock,paper,scissors]

user_choice =int(input("Choice a number between 0 to 2..Type 0 for Rock ,Type 1 for paper ,Type 2 for scissors.\n"))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer choose ")
print(game_images[computer_choice])
if (user_choice > 2) or (user_choice < 0):
    print("You typed a invalid number")

elif(user_choice == 0 ) and computer_choice ==2:
    print("You win!")
elif (user_choice == 2) and computer_choice == 0:
  print("You lose")

elif computer_choice > user_choice:
   print("You lose")
elif user_choice > computer_choice:
   print("You win!")
elif computer_choice == user_choice :
  print("Its draw")


