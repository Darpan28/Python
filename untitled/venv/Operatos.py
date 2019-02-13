a = int(input("Enter the 3 digit no."))
b = a//100
c = a % 100
d = c//10
e = c%10
f = b+d+e
print("The sum of digits of no. you entered is: ",f)