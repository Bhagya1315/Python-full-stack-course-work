'''
Exception handling :Exception handling is used to handle runtime errors and prevent program crash

Keywords:
try → contains risky code
except → handles the error
else → runs if no exception
finally → always executes
'''

'''
try:
    a=int(input("Enter the integer:"))


except ValueError:
    print("Please enter the integer:")

else:
    print("a=",a)

finally:
    print("End of the program:")

'''

'''
try:
    l=[1,23]
    print(1[7])
    d={1:2,3:2,4:5}
    print(d[9])
    a=int(input("Enter the integer:"))
    print(10/0)
    print('a'+10)


except TypeError:
    print("Give the same type")

except zerodivisionerror:
    print("can't divide with zero")

except keyerror:
    print("key is not present")

except indexerror:
    print("list index out of range")

except ValueError:
    print("Please enter the integer:")

else:
    print("a=",a)

finally:
    print("End of the program:")
'''    


'''
try:
    l = [1, 23]
    d = {1:2, 3:2, 4:5}
    
    print(10/0)
    print('a' + 10)

except (TypeError, ZeroDivisionError, KeyError, IndexError, ValueError) as e:
    print("Error occurred:", e)

else:
    print("a=", a)

finally:
    print("End of the program:")
'''

'''
try:
    #print(b)
    l=[1,23]
    #print(1[7])
    d={1:2,3:2,4:5}
    #print(d[9])
    #a=int(input("Enter the integer:"))
    print(10/0)
    print('a'+10)

except Exception as e:
    print("Error occured:",e)
    
else:
    print("a=",a)

finally:
    print("End of the program:")
'''
'''
try:
    balance=1000
    amount=-10
    if amount<0:
        raise Exception('Amount needs to be positive')
    balance+= amount

except Exception as e:
    print("Error occured:",e)

else:
    print("a=",a)

finally:
    print("End of the program:")

'''

'''
#open - read /write /append - close

try:
    file = open('student.txt','r')

except FileNotFoundError:
    print("File is not present")

else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
'''

'''
try:
    with open('student.txt','r') as file:
        print(file.read())
        file.seek(0)
        print(file.readline())
        file.seek(0)
        print(file.readlines())

except FileNotFoundError:
    print("File is not present")
'''

'''
try:
    with open('student.txt','a') as file:
        file.write('\nHima')
        file.write('\nSanjusha')

except Exception as e:
    print("Error:", e)
'''

'''
try:
    with open('student.txt','w') as file:
        file.write('Hima')
        file.write('\nSanjusha')

except Exception as e:
    print("Error:", e)

'''

'''
with open('student.txt','w+') as file:
    file.write('Hima')
    file.write('\nSanjusha')
    file.seek(0)
    print(File.read())
'''
