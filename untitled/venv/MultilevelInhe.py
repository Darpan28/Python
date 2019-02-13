class Product:
    def __init__(self,name,brand,price):
        self.name = name
        self._brand = brand
        self.__price = price

    def __ShowProductDetails(self):
        print(">>>>>",self.name,"<<<<<")
        print("The Brand is:",self._brand)
        print("The price is:",self.__price)

class Mobile(Product):

    def __init__(self,name,brand,price,ram,memory,os):
        Product.__init__(self,name,brand,price)
        self._ram = ram
        self.__memory = memory
        self.os = os

    def ShowMobileDetails(self):
        Product._Product__ShowProductDetails(self)
        print("The ram is:",self._ram,"gb")
        print("The memory is:",self.__memory,"gb")
        print("The os is:",self.os)

class Mobile1(Mobile):
    def __init__(self,name,brand,price,ram,memory,os,camera,processor):
        Mobile.__init__(self,name,brand,price,ram,memory,os)
        self.camera = camera
        self.processor = processor

    def _showMobile1Details(self):
        Mobile.ShowMobileDetails(self)
        print("The camera is:", self.camera, "mp")
        print("The processor is:", self.processor)




#p1 = Product("iPhoneX","Apple",80000)
#m1 = Mobile("iPhoneX","Apple",80000,4,128,"iOs")
#m1.ShowMobileDetails()

m2 = Mobile1("OnePlus 6T","OnePlus",55000,8,256,"Android",20,"SnapDragon845")
m2._showMobile1Details()

print("==================================")
#print("The prod dict",p1.__dict__)
#print("The prod dict",Product.__dict__)

print("The Mob1 dict",m2.__dict__)
print("The Mob1 dict ",Mobile1.__dict__)