import mysql.connector

class Student:
    def __init__(self,roll,name,standard,section,phone,address,email):
        self.roll = roll
        self.name = name
        self.standard = standard
        self.section = section
        self.phone = phone
        self.address = address
        self.email = email

    def showStudentDetails(self):
        print("=====",self.roll,"=====")
        print("Name is:",self.name)
        print("Standard is:", self.standard)
        print("Section is:", self.section)
        print("Phone is:", self.phone)
        print("Address is:", self.address)
        print("E-mail is:", self.email)
        print("=======================")

    def saveStudentinDB(self):
        sql = "insert into Student values(null,'{}','{}','{}','{}','{}','{}')".format(self.name,self.standard,self.section,self.phone,self.address,self.email)
        con = mysql.connector.connect(user="root",password="",host="localhost",database="pythonpract")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Student Saved!!")


reply ="yes"
while reply =="yes":
    print(">>>>>Add Student details<<<<<")
    name = input("Enter the name of student:")
    standard= int(input("Enter the standard:"))
    section = input("Enter the section:")
    phone = input("Enter the phone no.:")
    address = input("Enter the address:")
    email = input("Enter the email:")
    reply = input("Do you want to add more student? ")
    s1 = Student(0,name,standard,section,phone,address,email)
    s1.saveStudentinDB()
    s1.showStudentDetails()


