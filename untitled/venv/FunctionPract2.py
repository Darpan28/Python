"""

def addNumbers(num1, num2):
    sum =num1 + num2
    print("The sum is: ",sum)

addNumbers(20,30)

"""
#For N no.s of input then we take a list

"""
def addNumbers(numbers):
    sum =0
    for n in numbers:
         sum = sum + n
    print("Sum is: ",sum)

nums = {10,20,30,40,50}
#addNumbers(nums)
addNumbers((10,20,30,40,50))

"""

"""
def addNumbers(*numbers):  # Here *numbers and *args both are same; names are different; working is same.
    print(numbers)
    print(type(numbers))
    sum = 0
    for n in numbers:
        sum = sum +n
    print("The sum is:",sum)

addNumbers(10,20,30,40,50)
"""

"""
def funct(**kwargs):
    print(kwargs)
    print(type(kwargs))
funct(a=10,b=20,c=30,name="Darpan",last = "Garg")

"""
"""
def show(*agrs1,**kwargs1):
    print(agrs1)
    print(type(agrs1))
    print(kwargs1)
    print(type(kwargs1))


show(10,20,30, a = 50, b = 60, name = "Darpan", lastname = "Garg")

"""


