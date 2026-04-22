#hiding the complexity is called abstraction
from abc import ABC, abstractmethod    #ABC means abstract base class
class BankAccount:
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def current_balance(self):
        print("You can check your balance")
    def view_history(self):
        print("You can check out your transactions")

class SavingAccount(BankAccount):
    def deposit(self):
        print("upto 10l per account")
    def withdraw(self):
        print("Maintain minimum balance")

class CurrentAccount(BankAccount):
    def deposit(self):
        print("Unlimited transactions")
    def withdraw(self):
        print("Unlimited withdraws")
        
class JointAccount(BankAccount):
    def deposit(self):
        print("Any holder can deposit")
    def withdraw(self):
        print('Joint or either can withdraw')

class StudentAccount(BankAccount):
    def deposit(self):
        print("small deposit")
    def withdraw(self):
        print("limitations")
        

class ODAccount(BankAccount):
    def deposit(self):
        print("Overdraft")
    def withdraw(self):
        print("With draw uppto bamk account")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("salary credits+extra deposits allowed")
    def withdraw(self):
        print("Easy with draws")


sai =  SavingAccount()
print("___________________________sai_______________________________________")
sai.deposit()
sai.withdraw()
sai.view_history()
sai.current_balance()



bhagi = CurrentAccount()
print("_____________________________Bhagi_________________________________________")
bhagi.deposit()
bhagi.withdraw()
bhagi.view_history()
bhagi.current_balance()


manasa = JointAccount()
print("___________________________Manasa_______________________________________")
manasa.deposit()
manasa.withdraw()
manasa.view_history()
manasa.current_balance()


dhruvika = StudentAccount()
print("_____________________________________Dhruvika__________________________________")
dhruvika.deposit()
dhruvika.withdraw()
dhruvika.view_history()
dhruvika.current_balance()



haritha = ODAccount()
print("___________________________________Haritha______________________________________")
haritha.deposit()
haritha.withdraw()
haritha.view_history()
haritha.current_balance()

arun = SalaryAccount()
print("________________________________________Arun______________________________________")
arun.deposit()
arun.withdraw()
arun.view_history()
arun.current_balance
