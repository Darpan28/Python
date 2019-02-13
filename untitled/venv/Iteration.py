"""i=1
sum = 0
while i<10:
    a = i+1
    b = i+2
    i = b+1
    c = a+b
    sum = sum +c


print(sum)
"""

for i in range (0,6):

    for j in range (i,i+1):
        for k in range (i,j+i+1):
            print(k,end=" ")
        print("")



