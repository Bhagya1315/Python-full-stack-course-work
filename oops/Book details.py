'''class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"title:{self.title}, author: {self.author}, price: ${self.price} ")

book1 = Book("Clean code", "Robert Martin", 450)
book1.display()
'''
'''
class Employee:
    def __init__(self,name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_annual_salary(self):
        annual_salry = self.base_salary*12
        print(annual_salry)
        
e1= Employee("Hima",30000)
e1.calculate_annual_salary()
'''
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        avg = sum(self.marks) / len(self.marks)
        return avg >= 40
# Object and method call
s1 = Student("Priya", [45, 56, 60])
print("Passed:", s1.is_passed())
'''
'''
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def show_balance(self):
         print(f"Balance: {self.balance}")

# Use case
acc = BankAccount("Arjun")
acc.deposit(1000)
acc.withdraw(500)
acc.show_balance()
'''
'''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0
    def drive(self, km):
        self.odometer += km
    def show_odometer(self):
        print(f"Odometer: {self.odometer} km")

# Create object
car1 = Car("Toyota", "Innova")
car1.drive(120)
car1.drive(30)
'''

'''
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    def is_family_friendly(self):
        return self.rating < 13

# Use case
m1 = Movie("Finding Nemo", "Animation", 8)
print("Family Friendly:", m1.is_family_friendly())
'''
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
    def show_price(self):
        print(f"Discounted price: {self.price}")

# Create and apply
p = Product("Laptop", 50000)
p.apply_discount(10)
p.show_price()
'''
'''
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    def to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

# Example usage
temp = Temperature(25)
print("Fahrenheit:", temp.to_fahrenheit())
print("Celsius from 98F:", temp.to_celsius(98))
'''

'''
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def update_quantity(self, amount):
        self.quantity += amount
    def display(self):
        print(f"{self.name}: {self.quantity} in stock")

# Object usage
item = InventoryItem("Mouse", 50)
item.update_quantity(-5)
item.display()
'''

class Order:
    def __init__(self, order_id, status="Pending"):
        self.order_id = order_id
        self.status = status
    def update_status(self,new_status):
        self.status = new_status
    def show_status(self):
        print(f"Order {self.order_id} status: {self.status}")
        
# Create and update
o = Order("ORD123")
o.update_status("Shipped")
print(o.show_status())
