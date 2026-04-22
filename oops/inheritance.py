# inheritance
'''class Instagramv1:
    def reel(self):
        print("you can post the reel")

print('Sai - Instagramv1')
sai = Instagramv1()
sai.reel()
'''
#single inheritence
'''class Instagramv1:
    def reel(self):
        print("you can post the reel")


class Instagramv2(Instagramv1):
    def story(self):
        print("you can upload a story")

print('Sai - Instagramv1')
sai = Instagramv1()
sai.reel()

print('Bhagi - Instagramv2')
Bhagi = Instagramv2()
Bhagi.reel()
Bhagi.story()
'''

#Multtilevel inheritance
'''class Instagramv1:
    def reel(self):
        print("you can post the reel")


class Instagramv2(Instagramv1):
    def story(self):
        print("you can upload a story")

class Instagramv3(Instagramv2):
    def note(self):
        print("You can add your thoughts")

print('Sai - Instagramv1')
sai = Instagramv1()
sai.reel()

print('Bhagi - Instagramv2')
Bhagi = Instagramv2()
Bhagi.reel()
Bhagi.story()



print('Manoj -Instagramv3')
manoj = Instagramv3()
manoj.reel()
manoj.story()
manoj.note()
'''



#multiple inheritance
'''class Instagramv1:
    def reel(self):
        print("you can post the reel")


class Instagramv2(Instagramv1):
    def story(self):
        print("you can upload a story")

class Instagramv3(Instagramv2):
    def note(self):
        print("You can add your thoughts")

class meta(Instrgramv3):
    def ai(self):
        print("YOu can use the AI")

class crossplatform(Instagramv3):
    def integrating(self):
        print("You can integrate with whatsapp and facebook")


class Instagramv4(meta,crossplatform,Instagramv3):
    def repost(self):
        print("You can repost the post")


print('Sai - Instagramv1')
sai = Instagramv1()
sai.reel()

print('Bhagi - Instagramv2')
Bhagi = Instagramv2()
Bhagi.reel()
Bhagi.story()



print('Manoj -Instagramv3')
manoj = Instagramv3()
manoj.reel()
manoj.story()
manoj.note()



print('Sai - Instagramv1')
sai = Instagramv1()
sai.reel()

print('Bhagi - Instagramv2')
Bhagi = Instagramv2()
Bhagi.reel()
Bhagi.story()



print('Manoj -Instagramv3')
manoj = Instagramv3()
manoj.reel()
manoj.story()
manoj.note()


class Instagramv4(meta,crossplatform,Instagramv3):
    def repost(self):
        print("You can repost the post")

print('Sai - Instagramv1')
sai = Instagramv1()
sai.reel()

print('Bhagi - Instagramv2')
Bhagi = Instagramv2()
Bhagi.reel()
Bhagi.story()



print('Manoj -Instagramv3')
manoj = Instagramv3()
manoj.reel()
manoj.story()
manoj.note()
                                                            
print('sumathi - InstagramV4')
sumathi = Instagramv4()
sumathi.reel()
sumathi.story()
sumathi.note()
sumathi.ai()
sumathi.integrating()
sumathi.repost()
'''

#hierarchial inheritence  one parent two or more child clss

class Instagramv3(None):
    def note(self):
        print("You can add your thoughts")

class meta(Instrgramv3):
    def ai(self):
        print("YOu can use the AI")

class crossplatform(Instagramv3):
    def integrating(self):
        print("You can integrate with whatsapp and facebook")
sumathi=Instagramv3
sumathi.reel()
sumathi.story()
sumathi.note()
sumathi.ai()
sumathi.integrating()
sumathi.repost()














'''#single
class a:
classb(a):

#multilevel
class a:
class b(a):
class c(b):

#multiple
class a:
'''
