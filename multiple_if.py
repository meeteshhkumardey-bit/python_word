height = int(input("Enter your height in feet: "))
bill = 0
if height >= 3:
    print('can ride')
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 150
        print("Ticket price is $150")
    elif age <= 18:
        bill = 200
        print("Ticket price is $200")
    else:
        bill = 250
        print("Ticket price is $250")  


    want_photo = input("Do you want a photo taken? Y or N: ")
    if want_photo =='y' or want_photo == 'Y':
        bill += 50
        print(f"Your final bill is ${bill}")  
              