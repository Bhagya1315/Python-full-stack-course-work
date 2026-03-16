Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

== RESTART: C:/Users/HELLO/Desktop/python full stack course/day-8/examples.py ==
2+3
5
l=[]
l=list()
a=[1,2,3]
b=[2,3,4]
a+b
[1, 2, 3, 2, 3, 4]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
names=['anju','himaja','bhuvan','manoj']
names
['anju', 'himaja', 'bhuvan', 'manoj']
names[1]
'himaja'
names[2]
'bhuvan'
names[-1]
'manoj'
names[:3]
['anju', 'himaja', 'bhuvan']
names[:1]
['anju']
names[1:]
['himaja', 'bhuvan', 'manoj']
'anju' in names
True
'sumalatha' not  in names
True
a,b,c=[10,20,30]
a
10
b
20
c
30
names
['anju', 'himaja', 'bhuvan', 'manoj']
a,b,c,d= names
a
'anju'
b
'himaja'
c
'bhuvan'
d
'manoj'
names
['anju', 'himaja', 'bhuvan', 'manoj']
names[1] = 'hima bindhu'
names
['anju', 'hima bindhu', 'bhuvan', 'manoj']
id(names)
2930155899904
names[0]= 'keerthi'
id(names)
2930155899904
names.append('tharun')
names
['keerthi', 'hima bindhu', 'bhuvan', 'manoj', 'tharun']
names.append('teja')
names.append('anil')
names
['keerthi', 'hima bindhu', 'bhuvan', 'manoj', 'tharun', 'teja', 'anil']
names.extend(['anju','himaja','sujith','govind'])
names
['keerthi', 'hima bindhu', 'bhuvan', 'manoj', 'tharun', 'teja', 'anil', 'anju', 'himaja', 'sujith', 'govind']
['keerthi', 'hima bindhu', 'bhuvan', 'manoj', 'tharun', 'teja', 'anil', 'anju', 'himaja', 'sujith', 'govind']
['keerthi', 'hima bindhu', 'bhuvan', 'manoj', 'tharun', 'teja', 'anil', 'anju', 'himaja', 'sujith', 'govind']
names.insert91,'prsanna')
SyntaxError: unmatched ')'
names.insert(1,'prasanna')
names
['keerthi', 'prasanna', 'hima bindhu', 'bhuvan', 'manoj', 'tharun', 'teja', 'anil', 'anju', 'himaja', 'sujith', 'govind']
names.insert(5, 'kushal')
names
['keerthi', 'prasanna', 'hima bindhu', 'bhuvan', 'manoj', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja', 'sujith', 'govind']
id(names)
2930155899904
names.pop()
'govind'
names
['keerthi', 'prasanna', 'hima bindhu', 'bhuvan', 'manoj', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja', 'sujith']
names.pop()
'sujith'
names
['keerthi', 'prasanna', 'hima bindhu', 'bhuvan', 'manoj', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja']
names.pop(0)
'keerthi'
names
['prasanna', 'hima bindhu', 'bhuvan', 'manoj', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja']
names.pop(2)
'bhuvan'
names
['prasanna', 'hima bindhu', 'manoj', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja']
names.remove('manoj')
names
['prasanna', 'hima bindhu', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja']
del names[1]
names
['prasanna', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja']
names
['prasanna', 'kushal', 'tharun', 'teja', 'anil', 'anju', 'himaja']
names.clear()
names
[]
id(names)
2930155899904
>>> del names()
SyntaxError: incomplete input
>>> del names
>>> names
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    names
NameError: name 'names' is not defined
>>> id(names)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    id(names)
NameError: name 'names' is not defined
>>> l=[10,20,303,34,12,576,142,78,89]
>>> l
[10, 20, 303, 34, 12, 576, 142, 78, 89]
>>> max(l)
576
>>> len(l)
9
>>> min(l)
10
>>> sorted(l)
[10, 12, 20, 34, 78, 89, 142, 303, 576]
>>> sum(l)
1264
>>> sorted(l)
[10, 12, 20, 34, 78, 89, 142, 303, 576]
>>> l
[10, 20, 303, 34, 12, 576, 142, 78, 89]
>>> l.sort()
>>> l
[10, 12, 20, 34, 78, 89, 142, 303, 576]
>>> [10, 12, 20, 34, 78, 89, 142, 303, 576]
[10, 12, 20, 34, 78, 89, 142, 303, 576]
>>> l.reverse()
>>> l
[576, 303, 142, 89, 78, 34, 20, 12, 10]
>>> l.sort(reverse=True)
>>> l
[576, 303, 142, 89, 78, 34, 20, 12, 10]
