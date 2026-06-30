#pizza order!!!!

size=input("What size pizza do you want? S, M, or L: ")
add_pepperoni=input("Do you want pepperoni? Y or N: ")

if size=='S':
    bill=15
    if add_pepperoni=='Y':
        bill+=2
    else:
        bill+=0
else:
    if size=='M':
        bill=20
        if add_pepperoni=='Y':
            bill+=3
        else:
            bill+=0
    else:
        bill=25
        if add_pepperoni=='Y':
            bill+=3
        else:
            bill+=0

            print(f"Your final bill is: ${bill}")