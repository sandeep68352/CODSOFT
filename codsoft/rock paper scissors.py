# random_integer = random. randint (1, 10)
# print (random_integer)

# random_number_0_to_1 = random. random () * 10
# print(random_number_0_to_1)

# random_float = random. uniform(1, 10)
# print(random_float)


# import random
# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("heads")
# else:
#     print("tails")     



# choice = int(input("what did you choose : 0 for rock ,1 for paper , 2 for sissors :"))
# print(f"user choice :{choice}")
# computer_choice = random.randint(0,2)
# print(f"computer_choice: {computer_choice}")
# if choice == 0 or computer_choice == 1:
#     print("you win")
# elif choice < computer_choice:
#     print("you lose")    
# elif choice == 0 > computer_choice and choice == 0 > computer_choice :
#     print ("you win")
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