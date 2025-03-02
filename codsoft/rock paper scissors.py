
import random
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_image = ["rock,paper,scissors"]


user_choice = int(input("what did you choose : 0 for rock ,1 for paper, 2 for sissors :"))
print(f"user_choice{user_choice}:")
print(game_image[user_choice])
computer_choice = random.randint(0,2)
print(f"computer_choice {computer_choice}")
print(game_image[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("you win ")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you loose")   
elif computer_choice > user_choice :
    print ("you loose")
elif computer_choice == user_choice:
    print("it's draw ")  
else:
    print(" you entered invaild input ")          
