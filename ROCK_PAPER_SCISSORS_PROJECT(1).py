import random

user_choice = int(input("Enter your choice (Type 0 for rock, 1 for paper, 2 for scissors): "))
computer_choice = random.randint(0, 2)

print('Computer Choice:', computer_choice)

if(computer_choice==user_choice):
    print("It's a tie!")

elif((user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1)):
    print("You win!")

elif((user_choice==0 and computer_choice==1) or (user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==0)):
    print("Computer wins!")

elif(user_choice>2):
    print("Invalid input! Please enter a valid choice.")

elif(user_choice<0):
    print("Invalid input! Please enter a valid choice.")

else:
    print("Invalid input! Please enter a valid choice.")