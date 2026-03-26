Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={}
type(s)
<class 'dict'>
s=set()
s
set()
s={5678,546,23,454,124,57667,1324}
s
{124, 546, 57667, 454, 23, 1324, 5678}
s.add(124)
s
{124, 546, 57667, 454, 23, 1324, 5678}
s.remove(124)
s
{546, 57667, 454, 23, 1324, 5678}
s.add(12.3)
s
{546, 57667, 454, 23, 1324, 12.3, 5678}
s.add('string')
s
{57667, 454, 12.3, 'string', 23, 546, 1324, 5678}
s.add(2+3j)
s
{57667, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.add({1,2,3})
TypeError: unhashable type: 'set'
s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: unhashable type: 'dict'
s
{57667, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.add(False)
s
{False, 57667, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s+{1,2}
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s+{1,2}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
s*2
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
s
{False, 57667, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
23 in s
True
s[1:2]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s[1:2]
TypeError: 'set' object is not subscriptable
s
{False, 57667, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.add(1)
s
{False, 1, 57667, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.update({2,3,4})
s
{False, 1, 2, 57667, 3, 4, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.pop()
False
s.pop()
1
s.pop()
2
s.pop()
57667
s
{3, 4, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.remove(3)
s
{4, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.remove(3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.remove(3)
KeyError: 3
s
{4, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
s.discard(3)
s
{4, 454, (2+3j), 12.3, 'string', 23, 546, 1324, 5678}
for i in s:
    print(i)

4
454
(2+3j)
12.3
string
23
546
1324
5678
a={9,7,5,3,1}
b={2,3,4,5}
a & b
{3, 5}
a|b
{1, 2, 3, 4, 5, 7, 9}
a-b
{1, 9, 7}
#{9} {7}{5}{3}{1}{9,7}{7,5}{5,3}
{9}>a
False
>>> {9}<a
True
>>> a.isdisjoint(b)
False
>>> {0}.isdisjoint(a)
True
>>> a.union(b)
{1, 2, 3, 4, 5, 7, 9}
>>> a.intersection(b)
{3, 5}
>>> a
{1, 3, 5, 7, 9}
>>> len(a)
5
>>> max(a)
9
>>> min(a)
1
>>> a.subset(b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.subset(b)
AttributeError: 'set' object has no attribute 'subset'. Did you mean: 'issubset'?
>>> subset(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    subset(a)
NameError: name 'subset' is not defined
>>> {9}.issubset(a)
True
>>> {9}.issuperset(b)
False
>>> {9}.issubset(b)
False
>>> {9}.issuperset(a)
False
>>> max(a)
9
>>> sorted(a)
[1, 3, 5, 7, 9]
