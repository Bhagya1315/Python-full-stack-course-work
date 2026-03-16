products=[['laptop',56000],
          ['phone', 76000],
          ['charger',2000],
          ['mouse',700],
          ['buds',3500]]

def view_products():
    print("Product Name".ljust(15,' '),'price')
    for i in products:
        print(i[0].ljust(15,' '),i[1])

def add_product():
    product_name = input('Enter the Product name: ')
    price = int(input("Enter the product Price: "))
    products.append([product_name,price])
    print(f'{product_name} is added')

def del_product():
    product_id = int(input('Enter the Product Id: '))
    print(f'{products[product_id]} is deleted')
    products.pop(product_id)

while True:
    print("--------------------Welcome to the flipkart admin side---------------")
    print("1.view products")
    print("2.add product")
    print("3.Delete product")
    print("4.Exit")

    ch=int(input('Enter your choice: '))
    if ch==1:
           view_products()
    elif ch==2:
        add_product()
    elif ch==3:
        del_product()
    elif ch==4:
        print("Thank you")
    break
           
    
          


