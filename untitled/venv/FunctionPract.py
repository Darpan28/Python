""""
def fun(n):

    i=1
    sumEven = 0
    sumOdd = 0
    while i<=n:
        print(i,end=" ")
        sumOdd = sumOdd + i
        i = i + 2
    print()
    print(sumOdd)
    print()


    for i in range(2,n+1,2):
        print(i,end=" ")
        sumEven = sumEven + i

    print()
    print(sumEven)

    if sumEven > sumOdd:

        print("Sum of Even is Greater")
    else:

        print("Sum of Odd is Greater")


fun(100)

"""

#num = int(input("Enter the number of terms: "))
#a = 0
#b = 1
#print(a)
#print(b)
"""
def Fibo(num):

    global a
    global b
    i = a+b
    print(i)
    a = b
    b = i
    if b<=(num):
        Fibo(num)

Fibo(10)

def Factorial(num):
    if num==0:
        return 1;
    else:
        return (num*Factorial(num-1))
print(Factorial(4))
"""
n1 = 0
n2 = 1
#print(n1)
#print(n2)
def Fibo(num):
    global n1
    global n2
    if num > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
        Fibo(num-1)

Fibo(10) 