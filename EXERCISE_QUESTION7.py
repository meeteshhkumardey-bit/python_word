#wap which will select a random name form a list of names and the person selected will have to pay for everybody's food bill!!!

import random

names=input("Enter names separated by comma: ")
names_list=names.split(" , ")
length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} is selected to pay for everyone's food bill!")