class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} vehicle started.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Camry")
car1.start()
car1.show_info()


class Account:
    def __init__(self, balance):
        self.balance = balance
    def show_balance(self):
        print(f"Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance * self.interest_rate /100


acc = SavingsAccount(1000, 5)
acc.add_interest()
acc.show_balance()


class User:
    def __init__(self, username):
        self.username = username
    def access(self):
        print(f"{self.username} has user access.")

class Admin(User):
    def access(self):
        print(f"{self.username} has admin access.")

admin1 = Admin("admin_john")
admin1.access()


class Employee:
    def __init__(self, name):
        self.name = name
    def show_role(self):
        print("General employee")


class Manager(Employee):
    def show_role(self):
        print("Manager with team responsibilities")

mgr = Manager("Ravi")
mgr.show_role()


class Shape:
    def __init__(self, color):
        self.color = color
    def display_color(self):
        print(f"Color: {self.color}")

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

rect = Rectangle("Blue", 4, 5)
rect.display_color()
print("Area:", rect.area())



class Appliance:
    def __init__(self, brand):
        self.brand = brand

class WashingMachine(Appliance):
    def wash(self):
        print(f"{self.brand} washing clothes.")

wm = WashingMachine("LG")
wm.wash()


class Member:
    def __init__(self, name):
        self.name = name

    def benefits(self):
        return "Basic access"

class PremiumMember(Member):
    def benefits(self):
        return "Premium access + free delivery"

pm = PremiumMember("Akash")
print(pm.benefits())



class Vehicle:
    def drive(self):
        print("Driving a vehicle")

class Bike(Vehicle):

    def wheel_count(self):
        print("2 wheels")

b = Bike()
b.drive()
b.wheel_count()


class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} teaches in general")

class MathTeacher(Teacher):
    def teach(self):
        print(f"{self.name} teaches mathematics")

t = MathTeacher("Mrs. Kapoor")
t.teach()



class Device:
    def power_on(self):
        print("Device is powered on.")

class Laptop(Device):
    def open_ide(self):
        print("IDE opened.")

l = Laptop()
l.power_on()
l.open_ide()
