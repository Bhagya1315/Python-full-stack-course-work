'''class whatsappv0:
    def status(self):
        print("You can upload image and videos")

class whatsappv1(whatsappv0):
    def status(self):
        super().status()
        print("You can like, react and reply")


class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and filters also")


sai = whatsappv2()
sai.status()
'''



class whatsappv0:
    def status(self):
        print("You can upload image and videos")

class whatsappv1:
    def status(self):
        print("You can like, react and reply")


class whatsappv2(whatsappv0,whatsappv1):
    def status(self):
        whatsappv0.status(self)
        whatsappv1.status(self)
        
        print("You can add music and filters also")


sai = whatsappv2()
sai.status()
