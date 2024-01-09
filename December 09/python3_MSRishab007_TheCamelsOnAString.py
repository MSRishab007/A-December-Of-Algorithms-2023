def wordCount(word):
    if not word:
        return 0
    count=1
    for i in range(0,len(word)):
        if ord(word[i])>=56 and ord(word[i])<=91:
            count=count+1
    return count
inputWord=str(input("Input: "))
outputCount=wordCount(inputWord)
print("Output: ",outputCount)
