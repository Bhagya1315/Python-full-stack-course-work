Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python'
s
'python'
s="python"
s
'python'
s="""python"""
s
'python'
s='''python'''
s
'python'
s+' lang'
'python lang'
s
'python'
s*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'-'*20
'--------------------'
'09876'*12
'098760987609876098760987609876098760987609876098760987609876'
'*'*10
'**********'
s
'python'
s[4]
'o'
s[5]
'n'
s[0]
'p'
s[9]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[9]
IndexError: string index out of range
s[-2]
'o'
s[-3]
'h'
s[3]
'h'
s[-1]
'n'
names='manideep venkat tharun prdhuvi bhuvan manoj'
names
'manideep venkat tharun prdhuvi bhuvan manoj'
names[0]
'm'
names[-5]
'm'
names[:8]
'manideep'
names[10:16]
'enkat '
names[9:16
      names[9:15]
      
SyntaxError: '[' was never closed
names
      
'manideep venkat tharun prdhuvi bhuvan manoj'
names[9:16]
      
'venkat '
names[9:15]
      
'venkat'
names[16:22]
      
'tharun'
names[23:30]
      
'prdhuvi'
names[31:37]
      
'bhuvan'
names[38:]
      
'manoj'
names
      
'manideep venkat tharun prdhuvi bhuvan manoj'
names[::-1]
      
'jonam navuhb ivuhdrp nuraht taknev peedinam'
names[-5:]
      
'manoj'
names[-12:-6]
      
'bhuvan'
names[-21:-13]
      
' prdhuvi'
names[-1:-6:-1]
      
'jonam'
names[-7:-13:-1]
      
'navuhb'
names
      
'manideep venkat tharun prdhuvi bhuvan manoj'
names[::2]
      
'mnde ekttau rhv hvnmnj'
names
      
'manideep venkat tharun prdhuvi bhuvan manoj'
'venkat' in names
      
True
'bhuvan' in names
      
True
'anju' not in names
      
True
names
      
'manideep venkat tharun prdhuvi bhuvan manoj'
>>> len(names)
...       
43
>>> maxx(names)
...       
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    maxx(names)
NameError: name 'maxx' is not defined. Did you mean: 'max'?
>>> max(names)
...       
'v'
>>> min(names)
...       
' '
>>> chr(89)
...       
'Y'
>>> chr(65)
...       
'A'
>>> chr(90)
...       
'Z'
>>> chr(91)
...       
'['
>>> ord('a')
...       
97
>>> ord('z')
...       
122
>>> names
...       
'manideep venkat tharun prdhuvi bhuvan manoj'
>>> sorted(names)
...       
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'b', 'd', 'd', 'e', 'e', 'e', 'h', 'h', 'h', 'i', 'i', 'j', 'k', 'm', 'm', 'n', 'n', 'n', 'n', 'n', 'o', 'p', 'p', 'r', 'r', 't', 't', 'u', 'u', 'u', 'v', 'v', 'v']
