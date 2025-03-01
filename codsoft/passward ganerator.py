# student_scores = [180, 124, 165, 173,189,169,146]
# max_score = 0
# for score in student_scores :
#     if score > max_score:
#         max_score = score
# print(max_score)     

# total = 0
# for number in range(1,101):
#     total += number
# print (total)    

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','&','*','(', ')''+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print( "welcome to my passward generator " )
letters1 = int(input("how many letters would you like in your passward ? "))
symbols1 = int(input("how many symbols would you like ? "))
numbers1 = int(input ("how many number would you like ? "))

passward = []
for character in range(0,letters1):
    passward += random.choice(letters)
for character in range(0,symbols1):
    passward +=random.choice(symbols)
for character in range(0,numbers1):
    passward += random.choice(numbers)    
print (passward)    
random.shuffle(passward)
print(passward)

passward_list= ""
for character in passward:
    passward_list += character
print(f"your passward is : {passward_list}")