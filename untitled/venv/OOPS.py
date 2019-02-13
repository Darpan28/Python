"""
    Objects : User
    Attributes : Name
                 Phone
                 email
                 gender
                 address

"""
# Creating a User defined(By developer) type for object called User
class User:
    pass

# Object construction
# u1 and u2 are not objects ; they are refrence variables
u1 = User()
u2 = User()

#print("u1 is:",u1)
#print("u2 is:",u2)
u1.name = "John"
u1.phone = "+91 99999 88888"
u1.email = "John@example.com"
u1.age = 30
u1.gender = "Male"
u1.address = "redwood Shores"

u2.name = "Jinnie"
u2.gender = "Female"
u2.age = 22
u2.email = "jinnie@example.com"
u2.phone = "+91 77777 88888"

print("The data of U1 is:",u1.__dict__)
print("te data of u2 is",u2.__dict__)

# These objects are not standarized.