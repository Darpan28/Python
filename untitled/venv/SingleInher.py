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
        self.ram = ram
        self.memory = memory
        self.os = os

    def ShowMobileDetails(self):
        Product._Product__ShowProductDetails(self)
        print("The ram is:",self.ram,"gb")
        print("The memory is:",self.memory,"gb")
        print("The os is:",self.os)


#p1 = Product("iPhoneX","Apple",80000)
m1 = Mobile("iPhoneX","Apple",80000,4,128,"iOs")
m1.ShowMobileDetails()
print("==================================")
#print("The prod dict",p1.__dict__)
print("The prod dict",Product.__dict__)

