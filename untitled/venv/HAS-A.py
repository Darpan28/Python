class User:
    def __init__(self,name,phone,email,oRef):
        self.name = name
        self.phone = phone
        self.email = email
        self.oRef = oRef

    def showUserDetails(self):
        print("=====",self.name,"=====")
        print("Phone is:",self.phone)
        print("Email is:",self.email)
        #self.oRef.showOrderDetails()
        for o in self.oRef:
            o.showOrderDetails()

class Order:
    def __init__(self,name,brandname,price,quantity):
        self.name = name
        self.brandname = brandname
        self.price = price
        self.quantity = quantity

    def showOrderDetails(self):
        print(">>>>>",self.name,"<<<<<")
        print("The Brand is:",self.brandname)
        print("The Price is:",self.price)
        print("The quantity is:",self.quantity)

oRef = Order("Note 6 Pro","RedMi",13000,2)
o1 = Order("iPhone x","Apple",80000,1)
o2 = Order("Galaxy S9+","Samsung",65000,1)
orders =[oRef,o1,o2]
uRef = User("Jack","+91 98765 56789","jack@example.com",orders)


#print(uRef.__dict__)
#print(oRef.__dict__)

uRef.showUserDetails()