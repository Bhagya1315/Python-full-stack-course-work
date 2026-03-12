'''products = {'bread','butter','milk','sugar','salt'}
for item in products:
    print(item)

    
products = {'bread':30,'butter':50,'milk':20,'sugar':45,'salt':60}
for item in products:
    print(item)
    print(item,products[item])

    
products = {'bread':30,'butter':50,'milk':20,'sugar':45,'salt':60}
for item in products:
    print('Product name: ',item)
    print("product price:",products[item])
    print("Buy Now | Add to cart")
    print("Add to fav")
    print('--------------------------------------------')'''


'''s = 'python programming'
for ch in s:
    print(ch)'''

'''for i in range(1,11):
    print(i)

for i in range(30,61):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(5,96,5):
    print(i)'''

'''n=int(input("enter the number: "))
for i in range(1,21):
    print(f'{n}*{i}={n*i}')'''


'''for i in range(10):
    if i==5:
        break
    print(i)'''

'''for i in range(10):
    if i==5:
        continue
    print(i)'''


'''for i in range(10):
    if i==15:
        break
    print(i)
else:
    print("end of the numbber")'''



pin=1234
for i in range(5):
    user_pin=int(input("enter the pin: "))
    if user_pin == pin:
        print("Login successfully")
        break
    else:
        print("invalid password, Try again")
else:
    print("You reached maximum attempts, try again after 5 mins")
    
