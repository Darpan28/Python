class orders:
    def __init__(self,oid,restaurent,price):
        self.oid = oid
        self.restaurent = restaurent
        self.price = price

    def orderToCSV(self):
        return "{},{},{}\n".format(self.oid,self.restaurent,self.price)

o1 = orders(1,"Basant",1000)
o2 = orders(2,"Subway",500)
o3 = orders(3,"B7",1500)

#print(o1.orderToCSV())
#print(o2.orderToCSV())
#print(o3.orderToCSV())

file = open("MyOrders.csv","a")
file.write(o1.orderToCSV())
file.write(o2.orderToCSV())
file.write(o3.orderToCSV())
print("Data is written")
file.close()