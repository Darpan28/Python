# List of Lists
indiaPopulation = [[1212,1313,2323,4545],
                   [5656,4646,7878,1545],
                   [1325,1256,3258,6587]]

popCount =[]
for i in range(0,len(indiaPopulation)):
    total = 0
    for j in range(0,len(indiaPopulation[i])):
        total = total + indiaPopulation[i][j]
    print(total)
    popCount.append(total)
print(popCount)

if (popCount[0]>popCount[1] and popCount[0]>popCount[2]):
    print(popCount[0]," is greatest.")

elif(popCount[1]>popCount[0] and popCount[1]>popCount[2]):
    print(popCount[1]," is greatest.")

else:
    print(popCount[2]," is greatest.")