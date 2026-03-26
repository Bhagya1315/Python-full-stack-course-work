'''password = input("Enter the password: ")
check=set()
if len(password)>=8:
    for i in password:
        if i.islower():
            check.add('l')
        elif i.isupper():
            check.add('u')
        elif i.isdigit():
            check.add('n')
        else:
            check.add('s')

    if len(check) == 4:
        print("strong password")
    else:
        print("weak password")
else:
    print("Weak password")'''

#average of marks and gives appriciation
data={
    'anju':{'status':True,'python':99,'mysql':90,'django':97},
    'manideep':{'status':True,'python':70,'mysql':60,'django':50},
    'bhuvan':{'status':True,'python':80,'mysql':75,'django':77},
    'himaja':{'status':True,'python':58,'mysql':49,'django':62},
    'manoj':{'status':True,'python':44,'mysql':39,'django':46},
    'deepak':{'status':True,'python':18,'mysql':29,'django':16},
    'vijay':{'status':False,'python':None,'mysql':None,'django':None},
    }

name = input("Enter the student name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+data[name]['mysql']+data[name]['django']
        avg = sum/3
        if avg>=90:
            print(f'Congrats {name}, you got first class')
        elif avg>=75:
            print(f'Good {name}, wish you all the best next time')
        elif avg>=50:
            print(f'{name}, need improvement')
        elif avg>=35:
            print(f'Bad {name}, Work hard next time')
        else:
            print(f'{name}, you failed in the exam, bring your parents')
    else:
        print(f'{name}, you have not written the exams. Please bring your parents.')
else:
    print(f'{name} data not found')
            


