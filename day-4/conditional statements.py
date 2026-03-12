'''min_bal =5000
current_balance=2000

if current_balance<min_bal:
    print("send message and cut some amout")

    
min_charge =20
cur_charge =15
if cur_charge<min_charge:
    print('send alert to the charge the phone')




data =("user@gmail.com","user@123")
mail = input("Enter the email: ")
password = input("Enter the password: ")

if data == (mail,password):
    print("Login successful")
else:
    print("Invalid login")





fruits = ['mango','apple','papaya','pine apple']
search_item = input("search here: ")

if search_item in fruits:
    print(f'{search_item} found! Buy now')
else:
    print(f'{search_item} is out of stock we will notify it is available')


time=(int(input("enter the hour: ")))

if 0<= time <=6:
    print("kaveri\nzing bus\nflix \nbus")
elif 7<= time <= 12:
    print("Bus1\nBus19\nbus5")
elif 13<=time <=18:
    print("bus5\nbus7\nbus18")
elif 18<= time <= 24:
    print("bus90\nbus80\nbus70")
else:
    print("Enter the time in the given range")



print("welcome to the Uber, book your ride: ")
print("1.Bike\n 2.Auto\n 3.Car")

choice = int(input("choose the option: "))
if choice == 1:
    print("Hey, you have booked successfully.\n Driver is on the way. Wear helemet")
elif choice==2:
    print("Hello, you have booked successfully.\n Driver is on the way, please be on track")
elif choice == 3:
    print("Hello, you have booked the cab succeessfully.\n Driver is on the way, wear a seatbelt")
else:
    print("choose the correct option please")'''

login_status = True
premium_account= False
if login_status:
    if premium_account:
        print("Play the video with high quality and without ads")
    else:
        print("Play the video with normal quality and ads")
else:
    print("Invalid account")





