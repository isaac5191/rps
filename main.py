import random
while True:
 user=input("Enter a choice: (for R is for Rock. P is for paper. and S is for scissor)")
 a= ['R','P','S']
 comp_choice=random.choice(a)
 print("The game starts now:")
 #print(f"\n YOU CHOSE{user},computer chose{comp_choice}.\n")
#user_action=input("Enter a choice: (for R is for Rock. P is for paper. and S is for scissor)")
 for letter in user:
    if letter in  a :
        continue 
    else:
        break
 #print("Invalid value entered")
 print(f"your choice is :",user)
 print(f"COMPUTER CHOICE IS :",comp_choice)
 if user ==comp_choice:
  print('WE got a tie here')
 elif user=='R' and comp_choice =='P':
    print("Computer wins")
 elif user =='R' and comp_choice =='S':
    print("Congrats you won ")
 elif user =='P' and comp_choice =='R':
    print("Congrats you won")
 elif user =='S' and comp_choice =='R':
    print("Computer wins")
 elif user =='P' and comp_choice =='S':
     print("Computer wins")
 elif user=='S' and comp_choice =='P':
    print("Congrats you won")   
 elif user not in a :
    print('wrong input')
    print('do you want to play again: y or n')
    c=input('enter y to continue or n to end:')
    
    if c.lower()!="y":
        break
        
     #print("your choice is :",c)
#a= ['R','P','S']
#comp_choice=random.choice(a)
#user_action=input("Enter a choice: (for R is for Rock. P is for paper. and S is for scissor)")
