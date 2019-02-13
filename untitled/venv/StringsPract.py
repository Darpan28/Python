name1 = "Darpan Garg"
name3 = "Darpan Garg"
name4 = name3
print(name1)

name2 = name1.upper()
print(name2)

print("The size of name1 is:",name1.__sizeof__())
print(type(name1.__sizeof__()))
print("the lenght of name1 is:",name1.__len__())

print("************")

lenght = name1.__len__()
print("the length of name is: ",lenght)

print(name1[1])
print(name1[0 :6])
print("**********")
print(name1[(1) : -5])

if name1 is name2:
    print("Name1 == Name2")
else:
    print("Name1 != Name2")

if name1 is name3:
    print("Name1 == Name3")
else:
    print("Name1 == Name3")

if name4 == name1:
    print("Name4 == Name1")
else:
    print("Name4 != Name1")


print("------------------------")

data = "John is 20 yrs old and live in Model Town"
print(data)
#age = int(input("Enter the age: "))
#data1 = "{} is {} yrs old and lives in {}".format("John",age,"Model Town")
#print(data1)

data2 = "\u20b9 500"
print(data2)