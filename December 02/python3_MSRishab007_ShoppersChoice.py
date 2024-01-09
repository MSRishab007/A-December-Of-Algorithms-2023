print("Input:")
inputList=list(map(int,input().strip("[] ").split(",")))
uniqueInputList=[]
for i in inputList:
    if i not in uniqueInputList:
        uniqueInputList.append(i)
outputList=[]
for i in uniqueInputList:
    elementFrequency=0
    for j in inputList:
        if i==j:
            elementFrequency=elementFrequency+1
    outputList.append(elementFrequency)
print("Output:")
print(outputList)