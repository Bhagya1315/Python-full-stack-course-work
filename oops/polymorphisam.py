#polymerphisam
#same method different actions
#polymorphisam have two methods 1. method overloading    2.methor overriding
#1.method overloading - same method, different parameters, same/diff classes         its not supported in python
#2.method overriding - same method, same parameters, parent/child classes

'''class Hotstar:
    def __init__(self, username):
        print(f"Hi,{username} !\n welcome to the hotstar!!!")
    def promo(self):
        print("You can watch the promos")
    def login(self):
        print("You can login the hotstar")
    def search(self):
        print("You can search the movies")
    def profile(self):
        print("You can edit your profile")
    def videocontrollers(self):
        print("You can pause and play")
    def suggistions(self):
        print("You can check out the suggestions")

    def movie(self):
        print("You can have access for old movies")
    def ads(self):
        print("ads will be run")
    def download(self):
        print("You can't downoad the movie")
    def quality(self):
        print("You can watch movie upto limited quality")

sai = Hotstar('sai')
sai.promo()
sai.login()
sai.search()
sai.profile()
sai.videocontrollers()
sai.suggistions()
sai.movie()
sai.ads()
sai.download()
sai.quality()


print('\n')


class PremiumHotstar(Hotstar):
    def __init__(self, username):
        print(f"Hi,{username} !\n welcome to the PremiumHotstar!!!")
    def promo(self):
        print("You can watch the promos")
    def login(self):
        print("You can login the hotstar")
    def search(self):
        print("You can search the movies")
    def profile(self):
        print("You can edit your profile")
    def videocontrollers(self):
        print("You can pause and play")
    def suggistions(self):
        print("You can check out the suggestions")

    def movie(self):
        print("You can have access for old movies")
    def ads(self):
        print("ads won't be run")
    def download(self):
        print("You can download the movie")
    def quality(self):
        print("You can watch movie upto limited quality")

Bhagi = PremiumHotstar('Bhagi')
Bhagi.promo()
Bhagi.login()
Bhagi.search()
Bhagi.profile()
Bhagi.videocontrollers()
Bhagi.suggistions()
Bhagi.movie()
Bhagi.ads()
Bhagi.download()
Bhagi.quality()
'''    


#Different pauyment methods

class Payment:
    def __init__(self,bill):
        pass
    def yourbill(bill):
        print(f"your bill is  {bill}")
    def creditcard(bill):
        print("you can pay the cash through card")

    def Handpayment(bill):
        print("You can pay the cash through Hand")

p=Payment(1000)
p.yourbill()
p.creditcard()
p.Handpayment()


