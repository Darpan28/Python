#These objects are standarized
class Product:
    def __init__(self,pid,name,brand,color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.color = color

    def showProduct(self):
        print("*************")
        print(self.name)
        print(self.brand)
        print(self.color)
        print("**************")

p1 = Product(2001,"Note 6","Mi","Black")
#print("The data of p1 is:",p1.__dict__)
p1.showProduct()

p2 = Product(3001,"Galaxy S9+","Samsung","Blue")
p2.showProduct()