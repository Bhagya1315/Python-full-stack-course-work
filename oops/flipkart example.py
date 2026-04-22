'''class Flipkart:
    #class attribute
    discount = 0

    
    @classmethod
    def updateDiscount(cls,new_discount):
        cls.discount = new_discount

    @staticmethod
    def welcome():
        print('Welcome to the flipkart')

    def myorders(self,order_id):
        #instant attribute
        self.order_id = order_id
        print(f'You have order these product with id:{self.order_id}')

#class att, class meth, ints att, ints meth, static => object
#class att, class meth, static +> class

sai= Flipkart()
bhagi=Flipkart()
print(sai.discount)
print(Flipkart.discount)
sai.myorders(1)
print(sai.order_id)


sai.updateDiscount(20)
sai.myorders(20)
sai.welcome()

Flipkart.updateDiscount(20)
Flipkart.welcome()

sai.myorders(1)
sai.myorders(2)
eshu.myorders(3)
eshu.myorders(1)
eshu.myorders(4)
'''


#Encapsulation
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts=[]

    @property
    def myposts(self):
        return self._posts

    @myposts.setter
    def myposts (self,postname):
        self._posts.append(postname)



    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.__password=new_password
    

        print(f'Hello {self.username}, Welcome to Instagram')


sai = Instagram('sai','Sai@123')

print("Before Updating:",sai.username)
sai.username = ' Bhagi'
print('After updating: ',sai.username)

bhagi= Instagram('bhagi',B'hagi@123')
hima = Instagram('Hima','Hima@123')



print("Before updating:",sai.get_password())
sai.set_password = 'Bhaagi'
print("After updating:",sai.get_password())

print(sai.myposts)
sai.myposts = 'sunset.png'
sai.myposts = 'beach.mp4'
print(sai.myposts)


















      

























































































































































        





