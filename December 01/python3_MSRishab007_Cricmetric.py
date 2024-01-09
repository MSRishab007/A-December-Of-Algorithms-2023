print("Input:")
numberOfBatters=int(input())
scoreList=list(map(int,input().strip().split()))[:numberOfBatters]
print("\n")
print("Output:")
maxScoreIndex=0
totalScore=0
for i in range(0,numberOfBatters):
    totalScore=totalScore+scoreList[i]
    if scoreList[i]>scoreList[maxScoreIndex]:
        maxScoreIndex=i
print(totalScore)
print(maxScoreIndex)