"""
alphabets = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)

total = 0
word1 = input("Enter the word 1:")
word2 = input("Enter the word 2:")
word3 = word1.upper()
word4 = word2.upper()

for i in word3:

    for j in alphabets:
        if j == i:
            index = alphabets.index(j)
            total= total + numbers[index]
            w1 = total

for x in word4:
    for y in alphabets:
        if y == x:
            index1 = alphabets.index(y)
            total = total + numbers[index1]
            w2 = total

print("Total is:",total)
print(word1,"+",word2,"=",w1+w2)
print(word1,"-",word2,"=",w1-w2)
print(word1,"*",word2,"=",w1*w2)
print(word1,"/",word2,"=",w1//w2)
"""

alphabets = {"A":1, "B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

word1 = input("Enter the word 1: ").upper()
word2 = input("Enter the word 2: ").upper()
sum1 = 0
sum2 = 0
for ch in word1:
    sum1 = sum1 + alphabets[ch]

for ch in word2:
    sum2 = sum2 + alphabets[ch]

print("Sum1 is:",sum1)
print("Sum2 is:",sum2)

