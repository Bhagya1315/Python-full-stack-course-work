'''a=[]
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)

l=[i for i in range(1,100) if i%2==0]
print(l)'''


'''a=[]
for i in range(3,100):
    if i%3==0:
        a.append(i)
print(a)

l=[i for i in range(3,100,3)]
print(l)'''



'''a=[]
for i in range(1,101):
    a.append(i)
print(a)

l=[i for i in range(1,101)]
print(l)'''



'''l=[i*i for i in range(1,11)]
print(l)'''


'''s='python Programming'
vol='aeiouAEIOU'
l=[i for i in s if i in vol]
print(l)'''


'''s='python Programming'
vol='aeiouAEIOU'
l=['*' if i in vol  else i for i in s]
print(l)'''

#list comprehension
'''l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
a=[0 if i%2==0 else i for i in l]
print(a)'''

#set comprehension
'''l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
a={0 if i%2==0 else i for i in l}
print(a)'''


#tuple comprehension use generator in case no using of tuple
'''l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
a=tuple(0 if i%2==0 else i for i in l)
print(a)'''

#dictionary comprehension here the count gives the number how many times the same number is repeted
'''l=[7,3,2,5,1,5,6,4,1,2,8,5,6,7,3,8]
a={i: l.count(i) for i in l}
print(a)'''





