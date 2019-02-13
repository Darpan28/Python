class Student:
    def __init__(self,name,rollNo,std,phone,email):
        self.name = name
        self.rollNo = rollNo
        self.std = std
        self.phone = phone
        self.email = email

    def showData(self):
        print("=====Roll No.:",self.rollNo,"=====")
        print("Name is:",self.name)
        print("Standard is:", self.std)
        print("Phone is:", self.phone)
        print("Email is:", self.email)


student = []
reply = "yes"

while reply == "yes":
    print("Add Student Details:")
    name = input("Enter the name of student:")
    std = int(input("Enter the std:"))
    rollNo = int(input("Enter the roll No.:"))
    phone = input("Enter the phone no.:")
    email = input("Enter the email:")
    reply = input("Want to add another student?")
    s = Student(name,rollNo,std,phone,email)
    student.append(s)

for i in range(0,len(student)):
    student[i].showData()
    if (student[i].rollNo < student[i+1].rollNo):
        student[i].rollNo = student[i+1].rollNo
        print("Roll no.",student[i].showData())


#req = input("want to see data in ascending order of roll no. or std").lower()
#if req == "roll no.":

    

