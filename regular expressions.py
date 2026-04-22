import re
# match is for first thing of the patteren
#search is for it is valid in the string or not
'''text = "Python programming "
pattern = r'[A-Z]'
result = re.match(pattern,text)

print(result.group(0) if result else "No match found")
'''



'''
text = "Python programming 90 "
pattern = r'[0-9]'
result = re.search(pattern,text)

print(result.group(0) if result else "No match found")


text = "Python programming "
pattern = r'[a-b]{2}'
result = re.match(pattern,text)

print(result.group() if result else "No match found")
'''

#finedall
'''text = "Python 12567890 5678 890 version 1897653 windows 10 mqrks 85 programming"
pattern = r'[0-9]{2,}'
result = re.findall(pattern,text)
print(result)

#print(result.group(0) if result else "No match found")

'''#finditer is get to anumber
'''text = "Python 12567890 5678 890 version 1897653 windows 10 mqrks 85 programming"
pattern = r'[0-9]{2,}'
result = re.finditer(pattern,text)
for i in result:
    print(i.group(),i.start())
print(result)


'''




'''
text = "'9876543210"
pattern = r'[0-9]{10}'
result = re.fullmatch(pattern,text)
print(result.group() if result else "No match found")
'''



'''
text = 'Python programming'
pattern = r'[aeiouAEIOU]'
result = re.sub(pattern,'*',text)
print(result)
'''
'''
text = 'Python,java;mysql)flask programming'
pattern = r'[,;,)]'
result = re.split(pattern,text)
print(result)
'''
'''
text = 'hat hot hit head hear heat hate'
pattern= r'h.t'
result = re.findall(pattern,text)
print(result)
'''

'''
#if it is ending with it get or else empty list
text = 'hat hot hit head hear heat hate'
pattern= r'h$'
result = re.findall(pattern,text)
print(result)
'''

'''
text = 'h ht httt htttttttttttttt'
patteren = r'ht*'
result = re.findall(patteren,text)
print(result)
'''

'''
text = 'h ht httt htttttttttttttt'
patteren = r'ht+'
result = re.findall(patteren,text)
print(result)
'''


'''
text = 'hy hhhht httt htttttttttttttt'
patteren = r'ht?'
result = re.findall(patteren,text)
print(result)
'''

'''
text='sowmya@gmail.com'
patteren =r'[a-z@.]'
result = re.findall(patteren,text)
print(result)
'''



'''text='sowmya@gmail.com'
patteren =r'[a-z@.]'
result = re.findall(patteren,text)
print(result)
'''
'''
text='sowmya@gmail.com'
patteren =r'[sowmya]'
result = re.findall(patteren,text)
print(result)
'''



'''text='3456 7689 56 6578 768 65 89'
patteren =r'\d'
result = re.findall(patteren,text)
print(result)
'''

'''
text='sowmya@gmail.com'
patteren =r'\S'
result = re.findall(patteren,text)
print(result)
'''


text='sowmya@gmail.com'
patteren =r'\W'
result = re.findall(patteren,text)
print(result)
