#recursion syntax
'''def fun():
    if base_con:
        return
    fun()'''


'''def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
    
display(1)'''

'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
    
    
display(1)'''

'''def display(n):
    if n>10:
        return
    print("before:",n)
    display(n+1)
    print("After: ",n)
    
display(1)'''

'''def display(s,i):
    if i==len(s):
        return
    print(s[i])
    display(s,i+1)

display("python programming",0)'''


'''def display(s,i):
    if i==len(s):
        return
    display(s,i+1)
    print(s[i])

display("python programming",0)'''

'''def display(s,i):
    if i==len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display("Python programming",0)'''
    

'''def display(s,i):
    if i==len(s):
        return
    display(s,i+1)
    print(s[:i+1])

display("Python programming",0)'''


'''def display(s,i):
    if i<=0:
        return
    print(s*i)
    display(s,i-1)
    print(s*i)

display("abc",6)'''

'''def display(s,i):
    if i<=0:
        return
    display(s,i-1)
    print(s*i)

display("abc",6)'''

'''def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
   
display("abcdefg",0,3)'''



'''def display(s,i,n):
    if i==len(s)-n:
        return
    display(s,i+1,n)
    print(s[i:i+n])

display("abcdefg",0,3)'''

'''def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])
    
print(display([1,2,3,4,5,6,7,8],0,0))'''


'''def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])
    
print(display(['python','java','html','css','javascript','flask'],0,' '))'''


#pass by value
#passing immutable items the in and out will be effected like list
#int,float,str,list,tuple,set,dict

#pass by value       tuple
'''def display(n):
    n+=(8,9)
    print('inside: ',n)

n=(1,2,3,4)
display(n)
print('outside: ',n)'''

#                   list
'''def display(n):
    n+=[8,9]
    print('inside: ',n)

n=[1,2,3,4]
display(n)
print('outside: ',n)'''



def display(n):
    n{8}=9
    print('inside: ',n)

n={1:1,2:2,3:3,4:4}
display(n)
print('outside: ',n)









          


    
    

    
    

    
    
