import ast
inputString=input("Input: ")
inputList=ast.literal_eval(inputString)
lastIndex=0
outputList=[]
for i in range(len(inputList)-1):
    currentword=inputList[i]
    nextWord=inputList[i+1]
    count=0
    if len(currentword)!=len(nextWord):
        break
    for letterCurrentWord,letterNextWord in zip(currentword,nextWord):
        if letterCurrentWord!=letterNextWord:
            count=count+1
    else:
        if count!=1:
            break
        else:
            outputList.append(currentword)
            lastIndex=lastIndex+1
if len(outputList)!=0:
    outputList.append(inputList[lastIndex])
    print("Output: ",outputList)
else:
    print("Output: No valid chain.")
