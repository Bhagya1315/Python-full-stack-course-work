'''i=20
while i<=30:
    if i==25:
        break
    print(i)
    i+=1'''

'''i=20
while i<=30:
    if i==25:
        continue
    print(i)
    i+=1'''
    
'''i=20
while i<=30:
    if i==25:
        pass
    print(i)
    i+=1'''

'''i=20
while i<=30:
    print(i)
    i+=1'''


'''bullets=10
while bullets>0:
    print(f"{bullets} bullets are left, you can shoot!!")
    bullets-=1
else:
    print("Game over")'''


'''moves = 32
winning_point = 8
while moves>0:
    if moves == winning_point:
        print("You win the game")
        break
    print(f"{moves} moves are left, you can play!!")
    moves-=1
else:
    print("Game over")'''




'''data={}
n=int(input('no.of students: '))
for i in range(n):
    name=input('Enter the name: ')
    data[name]=False
#print(data)
for name in data:
    status = int(input(f'enter the {name} status(0-Absent, 1-Present): '))
    data[name]=bool(status)
print(data)'''




