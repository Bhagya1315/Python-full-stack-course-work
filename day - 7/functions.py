'''def function_name(arguments):
    #stmts
    return
function_name(parameters)'''


'''def wish(name):
    print(f'Hello {name}, Welcome to python 100 days of program')
wish('swarna')
wish('manisha')
wish('tharun')
wish('Aditya')
wish('bhuvan')'''



'''def display(username,email,password):
    print("user name: ",username)
    print('email: ',email)
    print('password: ',password)

display('sudheer','sudheer@gmail.com','s@123')
display('sudheer@gmail.com','sudheer','s@123')
display('s@123','sudheer@gmail.com','sudheer')'''


'''def display(username,email,password):
    print("user name: ",username)
    print('email: ',email)
    print('password: ',password)

display(username='sudheer',email='sudheer@gmail.com',password='s@123')
display(email='sudheer@gmail.com',username='sudheer',password='s@123')
display(password='s@123',email='sudheer@gmail.com',username='sudheer')'''


'''def display(username,email,password,phoneno('+91')):
    print("user name: ",username)
    print('email: ',email)
    print('password: ',password)
    print('phone no:',phoneno)

display(username='sudheer',email='sudheer@gmail.com',password='s@123','123456')
display(email='sudheer@gmail.com',username='sudheer',password='s@123')
display(password='s@123',email='sudheer@gmail.com',username='sudheer')'''










def display(*names):
    print(names)

display('tharun','gowtham','bharath')
display('tharun','gowtham')
display('tharun')








def display(**names):
    print(names)

display(n1='tharun',n2='gowtham',n3='bharath')
display(n1='tharun',n2='gowtham')
display(n1='tharun')
