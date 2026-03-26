'''def wish (name):
    return f'Hello {name}, Welcome to python'''

''''wish = lambda name: f'Hello {name}, Welcome to python'
print(wish("bhagi"))
print(wish("sai"))'''



''''add = lambda a,b,c:(a+b+c)/3
print(add(1,2,3))
print(add(6,7,8))'''

'''iseven = lambda n:"Even" if n%2==0 else "Odd"
print(iseven(13))
print(iseven(28))
'''


'''greater = lambda a,b:  a if a >b else  b
print(greater(13,15))
print(greater(28,15))
'''


'''isvowel = lambda a: "vol" if a in vol else"con"
vol="aeiouAEIOU"
print(isvowel('a'))
print(isvowel('k'))
'''


#map()

'''l=['arun','haritha','sai','bhagi','manoj']
res=list(map(lambda i:i.title(),l))
print(res)



#in real function
def fun(l):
    for i in range(len(l)):
        l[i]=l[i].title()
    return l
'''


'''
def fun(l):
    res=[]
    for i in range(len(l)):
        if l[i]%3==0:
            res.append(l[i])
    return res

l= [20,30,40,50,60,70,80,90,100]


res = list(filter(lambda i:i%3==0,l))


print(fun(l))
print(res)
'''


'''
def fun(l):
    res=[]
    for i in range(len(l)):
        if l[i]>60:
            res.append(l[i])
    return res

l = [20,30,40,50,60,70,80,90,100]

res = list(filter(lambda i :i>60,l))
print(fun(l))
print(res)
'''
'''
l={'laptop':True,
   'Iphone':False,
   'mouse':True,
   'Tablet':False,
   'Charger':True
   }
res = list(filter(lambda i:l[i],l))
print(res)
'''



'''l=[1,0,2,3,0,1,3,4,5,5,6,2,3,5,6,7,8,2]
res = list(filter(lambda i:i%2==0,l))
print(res)
'''


#reduce
'''from functools import reduce
l=[1,2,3,1,3,4,5,5,6,1,2,5,6,7,8,2]
res=reduce(lambda a,b:a*b,l)
print(res)'''

'''from functools import reduce

l=['python','java','c++','c','html','reactjs']
res = reduce(lambda a,b:a+' '+b,l)
print(res)'''

'''res=[20,30,40,50]=map
res1=[20,40]=filter
res2=100=reduce
'''



d={
    'apple':30,
    'orange':25,
    'pineapple':60,
    'mango':50,
    'grapes':120,
    'banana':40
    }
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))




