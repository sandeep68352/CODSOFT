import random
game_over = False
while not game_over :

    user_choice = input("what did you choose : 'rock' ,'paper', 'sissors' :").lower()
    items = ('rock','paper','sissors')
    print(f"user_choice : {user_choice}")
    
    computer_choice = random.choice(items)
    print(f"computer_choice :{computer_choice}")
    
    if user_choice == "rock" and computer_choice == "sissors" :
        print("you win ")
    elif user_choice == "sissors" and computer_choice == "paper" : 
        print(" you win ")  
    elif user_choice == "paper" and computer_choice == "rock"  :
        print("you win")      
    elif computer_choice == "rock" and user_choice == "sissors" :
        print("you loose")   
    elif computer_choice == "sissors" and user_choice == "paper" :
        print ("you loose ")  
    elif computer_choice == "paper" and user_choice == "rock"  :
        print("you loose")    
    elif computer_choice == user_choice:
        print("it's draw ")  
    else:
        print(" you entered invaild input ")   
    stop_game = input("type 'y' for play again and 'n' for end the game :").lower()
    if stop_game == "n":
        game_over = True
        print("GAME END")
    elif stop_game == "y":
        game_over = False 
        print("PLAY AGAIN")
    else:
        game_over = True
        print("YOUB ENTERD INVALID VALUE")
