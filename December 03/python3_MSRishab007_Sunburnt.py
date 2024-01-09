print("Input:")
numberOfBuildings=int(input("N = "))
inputList=list(map(int,input("H[] = ").strip("{} ").split(",")))[:numberOfBuildings]
countOfBuilding=1
print(inputList)
highestHeight=inputList[0]
for i in range(1,len(inputList)):
    if inputList[i]>highestHeight:
        highestHeight=inputList[i]
        countOfBuilding=countOfBuilding+1
print("\n")
print("Output:")
print(countOfBuilding)