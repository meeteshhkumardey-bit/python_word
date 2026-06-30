name1=input("Enter your name: ")
name2=input("Enter his/her name: ")

combined_string=name1+name2
print("Combined string:", combined_string)

combine_string=combined_string.lower()

t=combine_string.count('t')
r=combine_string.count('r')
u=combine_string.count('u')
e=combine_string.count('e')

true= t+r+u+e

l=combine_string.count('l')
o=combine_string.count('o')
v=combine_string.count('v')
e=combine_string.count('e')

love= l+o+v+e

love_score=int(str(true)+str(love))

if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif (love_score>=40) and (love_score<=50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")