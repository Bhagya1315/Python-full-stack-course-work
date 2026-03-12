Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myvar=15
my_var=15
My_var=15
my var =15
SyntaxError: invalid syntax
my@var=10
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
My_Var=15
my_var=15
_myvar=15
13myvar=15
SyntaxError: invalid decimal literal
myvar13=15
myvar=13
myvar=15
myvar
15
myvar
15
Myvar=13
Myvar
13
myvar
15
if =28
SyntaxError: invalid syntax
f =1000
f
1000
type(f)
<class 'int'>
lc=56
lc
56
type(lc)
<class 'int'>
fo=15.3
fo
15.3
type(fo)
<class 'float'>
a=3+6j
a
(3+6j)
type(a)
<class 'complex'>
a=3+6J
a
(3+6j)
type(a)
<class 'complex'>
s='python programming')
SyntaxError: unmatched ')'
s=('Python')

s
'Python'
type(s)
<class 'str'>
pn="laptop"
s
'Python'
s[0]
'P'
s[1]
'y'
s[2]
't'
s[3]
'h'
s[4]
'o'
s[4]
'o'
s[5]
'n'
s[6]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s[6]
IndexError: string index out of range
n=['a'.'b','c','d','e']
SyntaxError: invalid syntax
n=['a','b','c','d','e']
n
['a', 'b', 'c', 'd', 'e']
n[1]
'b'
n[2]
'c'
n[0]
'a'
n.append('b')
n
['a', 'b', 'c', 'd', 'e', 'b']
t=(1,1,1,1,2,3,4,5)
t
(1, 1, 1, 1, 2, 3, 4, 5)
t[0]
1
t[1]
1
t[2]
1
t.append(0)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t.append(0)
AttributeError: 'tuple' object has no attribute 'append'
type(t)
<class 'tuple'>
type(n)
<class 'list'>
s={123,2344,57,456}
s
{2344, 57, 123, 456}
s.append(1)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s.append(1)
AttributeError: 'set' object has no attribute 'append'
s.add(1)
s
{1, 2344, 456, 57, 123}
p={'pid' : 1, 'pname' : 'laptop', 'price':75000}
st=True
type(st)
<class 'bool'>
type(s)
<class 'set'>
type(p)
<class 'dict'>
s=false
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s=false
NameError: name 'false' is not defined. Did you mean: 'False'?
s=False
s
False
a=None
a=10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
a=12.3
int(a)
12
str(a)
'12.3'
complex(a)
(12.3+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
bool(a)
True
a=4+2j
a
(4+2j)
int(a)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
'(4+2j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
bool(a)
True
l=[1,2,3,4,5,6,7]

l
[1, 2, 3, 4, 5, 6, 7]
int(l)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[1, 2, 3, 4, 5, 6, 7]'
tuple(l)
(1, 2, 3, 4, 5, 6, 7)
dict(l)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5)
int(t)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
list(t)
[1, 2, 3, 4, 5]
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
str(t)
'(1, 2, 3, 4, 5)'
s={1,2,3,4}
s
{1, 2, 3, 4}
int(s)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
list(s)
[1, 2, 3, 4]
str(s)
'{1, 2, 3, 4}'
tuple(s)
(1, 2, 3, 4)
dict(s)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
d={1:1,2:4,3:9}
d
{1: 1, 2: 4, 3: 9}
int(d)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> list(d)
[1, 2, 3]
>>> set(d)
{1, 2, 3}
>>> tuple(d)
(1, 2, 3)
>>> str(d)
'{1: 1, 2: 4, 3: 9}'
>>> bool(d)
True
>>> a = True
>>> int(a)
1
>>> float(a)
1.0
>>> complex(a)
(1+0j)
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> str(a)
'True'
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
