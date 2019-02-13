# Non standardized Objects
class Dish:
    pass
D1 = Dish()
D1.name = "Shahi Paneer"
D1.color = "Light Yellow"
D1.type = "Spicy"
D1.quantity = "1 Plate"
D1.topping = "Garnish with Corriender leaves"

print("The ordered dish is:",D1.__dict__)

d2 = Dish()
d2.name = "Oreo Shake"
d2.quantity = "Large"
d2.type = "Chilled"
d2.addition = "Extra Ice Cream"
d2.topping = "With oreo and ice cream"
print("The ordered shake is: ",d2.__dict__)
print("------------------------------------")
# Standardized Objects

class Dish2:
    def __init__(self,name,toppings,type):
        self.name = name
        self.toppings = toppings
        self.type = type

    def showDish(self):
        print("==================")
        print(self.name)
        print(self.toppings)
        print(self.type)
        print("===================")

d3 = Dish2("Mango Shake","Extra Ice Cream","Large")
d3.showDish()
del d3.type

