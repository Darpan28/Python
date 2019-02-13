Hindi = "\u0905\u0906\u0907\u0908\u0909\u090A\u090F\u0910\u0913\u0914\u0915\u0916\u0917\u0918\u091A\u091B\u091C\u091D\u091E\u091F\u0920\u0921\u0922\u0923\u0924\u0925\u0926\u0927\u0928\u092A\u092B\u092C\u092D\u092E\u092F\u0930\u0932\u0935\u0936\u0937\u0938\u0939"
English = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for n in Hindi:
    print(n,end=" ")

print()

for n in English:
    print(n,end=" ")

print()
#Eng = input("Enter the name: ")

Eng = "John"
Eng2 = Eng.upper()
print(Eng2)
print(Eng2[0])
for i in Eng2:
    #print(i)

    for j in English:
        if j == i:
            print(j,"found")
            break




