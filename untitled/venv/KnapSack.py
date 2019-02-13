maxWeight = 20
currentWeight = 0
currentValue = 0
maxValue = 0

Weights = [20,10,9,4,2,1]
Values = [4000,3500,1800,400,1000,200]
len = Values.__len__()
Result = [0,0,0,0,0,0]
Chosen = [0,0,0,0,0,0]
numOfIterations = 64

for i in range (0,64):
    for j in range ((len-1),0,-1):
        if Chosen[j] == 1:
            Chosen[j] =0
        else:
            Chosen[j] =1
            break
    currentValue =0
    currentWeight = 0
    for ele in range(0,Chosen.__len__()):

        if Chosen[ele] == 1:
            currentValue+= Values[ele]
            currentWeight+= Weights[ele]

        if ((currentValue>maxValue) and (currentWeight<=maxWeight)):
            maxValue = currentValue

            for x in range (0,Chosen.__len__()):
                Result[x] = Chosen[x]

for a in range(0,Result.__len__()):

    if(Result[a]==1):
        Result[a] = Weights[a]

print("The best combinations of weights by which we get the max. value is:-")

for t in Result:

    if t!=0:
        print(t,end=" ")

print()
print("The max. value is:",maxValue)
