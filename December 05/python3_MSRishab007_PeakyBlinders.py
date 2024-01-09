inputList=list(map(int,input("Input: ").strip("[] ").split(",")))
totalSumOfList=sum(inputList)
averageOfList=totalSumOfList/len(inputList)
requiredSum=0
for i in inputList:
    if i>=averageOfList:
        requiredSum=requiredSum+i
print("Output: ",requiredSum)