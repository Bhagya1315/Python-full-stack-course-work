Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name= input('enter the name: ')
enter the name: bhagi
name
'bhagi'
age=input('Enter the AGE: ')
Enter the AGE: 22
age
'22'
age=int(input('Enter the age : '))
Enter the age : 24
age
24
type(age)
<class 'int'>
price=input('Enter the price: ')
Enter the price: 99.99
price
'99.99'
price=float(input('Enter the price: '))
Enter the price: 99.99
price
99.99
type(price)
<class 'float'>
'anjusree himaja himabindhu'
'anjusree himaja himabindhu'
'anjusree himaja himabindhu'.split()
['anjusree', 'himaja', 'himabindhu']
KeyboardInterrupt
'anjusree himaja himabindhu'.split(',')
['anjusree himaja himabindhu']
'anjusree, himaja, himabindhu'.split(',')
['anjusree', ' himaja', ' himabindhu']
names= input('Enter the names :')
Enter the names :anjusree himaja himabindhu
names
'anjusree himaja himabindhu'
names=input('Enter the names: ').split()
Enter the names: anjusree himaja himabindhu
names
['anjusree', 'himaja', 'himabindhu']
numbers=input('Enter the numbers: ').split()
Enter the numbers:  12 3 4 5 7 
numbers
['12', '3', '4', '5', '7']
numbers=int(input("Enter the numbers : ").split())
Enter the numbers : 76 8
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    numbers=int(input("Enter the numbers : ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
numbers = list(map(int,input('Enter the numbers : ').split()))
Enter the numbers : 1 2 3 4 5 6
numbers
[1, 2, 3, 4, 5, 6]
numbers=list(map(float,input('Enter the numbers: ').split()))
Enter the numbers: 1 2 3 4 5 
numbers
[1.0, 2.0, 3.0, 4.0, 5.0]
numbers=tuple(map(int,input('Enter the numbers: ').split()))
Enter the numbers: 1 2 3 4 5 6 7
numbers
(1, 2, 3, 4, 5, 6, 7)
numbers=tuple(map(float,input('Enter the numbers: ').split()))
Enter the numbers: 1 2 3  45 6 7 8 
numbers
(1.0, 2.0, 3.0, 45.0, 6.0, 7.0, 8.0)
names=tuple(input('Enter the names: ').split())
Enter the names: anjusree himaja himabindhu
names
('anjusree', 'himaja', 'himabindhu')
names=set(input('Enter the names: ').split()))
SyntaxError: unmatched ')'
names=set(input('Enter the names: ').split())
Enter the names: anjusree himaja himabindhu
names
{'anjusree', 'himaja', 'himabindhu'}
numbers=set(map(float,input('Enter the numbers: ').split()))
Enter the numbers: 16 785 3 5 2 6 
numbers
{2.0, 3.0, 5.0, 6.0, 16.0, 785.0}
numbers=set(map(int,input('Enter the numbers: ').split()))
Enter the numbers: 1 3 78 65 333
numbers
{65, 1, 3, 333, 78}
d = eval(input('Enter the input: '))
Enter the input: {1:1,2:4,3:9,4:16}
d
{1: 1, 2: 4, 3: 9, 4: 16}
d=eval(input('Enter the input:'))
Enter the input:1 2 35 
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d=eval(input('Enter the input:'))
  File "<string>", line 1
    1 2 35 
      ^
SyntaxError: invalid syntax
d=eval(input('Enter the input: '))
Enter the input: 1 3 4 6
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d=eval(input('Enter the input: '))
  File "<string>", line 1
    1 3 4 6
      ^
SyntaxError: invalid syntax
d=eval(input('Enter the input:'))
Enter the input:[1 2 3 4 5]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d=eval(input('Enter the input:'))
  File "<string>", line 1
    [1 2 3 4 5]
     ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
username,password=['py','py123']
username
'py'
password
'py123'
a,b,c=list(map(int,input('enter the sides:').split()))
enter the sides:7 6 8
>>> a
7
>>> b
6
>>> c
8
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a//b
2
>>> a%b
0
>>> a**b
100000
>>> b*8a
SyntaxError: invalid decimal literal
>>> b**a
9765625
>>> a>b
True
>>> a<b
False
>>> b>a
False
>>> b<a
True
>>> a==b
False
>>> a<=b
False
>>> a>=b
True
>>> a/=10
>>> a
1.0
