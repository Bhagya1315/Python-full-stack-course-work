products=['rice','wheat flour','sugar','milk','eggs(12pcs)','cookinoil','tea powder','salt','bread','soap']
prices=[60,45,40,25,70,130,90,20,30,25]
print("Welcome to grocery store")
print("here are the availble products:\n")

print('Index'.ljust(6,' '),'products'.ljust(15,' '),'price'.ljust(6,' '))
for i in range(10):
    print(str(i+1).ljust(6,' '),products[i].ljust(15,' '),str(prices[i]).ljust(6,' '))

items=list(map(int,input("Enter the indexes: ").split()))
print("selectedd items: ")
total_amount = 0
for item in items:
    print(products[item-1],prices[item-1])
    total_amount += prices[items-1]

print(f'Total amount to pay: rs. {total_amount},Thank you for shopping with us')



