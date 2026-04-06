import collections
s='python programming'
'''res= collections.Counter(s)#count of the cariables how many the word is repeted
l=[1,2,3,12,34,1,1,2,3,4,2,3]#count of the number how many times repeted
r='this is that that is this'.split() #gives the output as words repeted times

res1= collections.Counter(s)
res2=collections.Counter(r)
print(res)
print(res1)
print(res2)'''


'''res={}
for i in s:
    if i in res:
        res[i]+=1
    else:
        res[i]=1

print(res)'''


'''res=collections.defaultdict(int)#with out usingthis the result is empty dictionary
for i in s:
    res[i]=res[i]+1
print(res)'''


''''q=collections.deque([])
q.append(20)
q.append(30)
q.append(60)
q.append(70)
q.append(90)
q.popleft()#feom left side onwards it is poped out
q.popleft()
q.popleft()
q.append(10)
q.append(40)


print(q)
'''







q=collections.deque([])
q.appendleft(20)
q.appendleft(30)
q.appendleft(60)
q.appendleft(70)
q.appendleft(90)
q.pop()#from left side onwards it is poped out
q.pop()
q.pop()
q.appendleft(10)
q.appendleft(40)


print(q)

