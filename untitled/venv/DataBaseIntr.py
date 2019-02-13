import mysql.connector

class Customer:
    def __init__(self,cid,name,phone,age,address):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address

    def showcustomer(self):
        print("==",self.cid,"|",self.name,"==")
        print("Names is:",self.name)
        print("Phone is:", self.phone)
        print("Age is:", self.age)
        print("Address is:", self.address)
        print("==============================")

    def saveCustomerInDb(self):
        sql = "insert into Customer values(null,'{}','{}','{}','{}')".format(self.name,self.age,self.phone,self.address)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="pythonpract")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Customer saved")

cRef1 = Customer(0,"jim","+91 96325 52369",22,"BRS Nagar")
cRef1.showcustomer()
cRef1.saveCustomerInDb()