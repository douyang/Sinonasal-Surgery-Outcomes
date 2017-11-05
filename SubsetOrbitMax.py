import re

data = open("surgicalCasesWComplications.csv", 'r')
data2 = open("surgicalCasesWComplicationsIsDifficult.csv", 'w')

output = open("subsetOrbitMax.csv", 'w')

lineCount = 0

relevantCodes = ["1652",  "1651"]

for line in data:
    writeThisTime = 0
    lineCount += 1

    codes = ""
    
    if lineCount == 1:
        output.write(line)
    else:
        if(line.find("low") > 0):
            codes = line[line.find("low"):len(line)]
        if(line.find("medium") > 0):
            codes = line[line.find("medium"):len(line)]
        if(line.find("high") > 0):
            codes = line[line.find("high"):len(line)]

        for code in relevantCodes:
            if(code in codes):
                writeThisTime = 1
                output.write(line)
                #print codes
    if(writeThisTime == 1):    
        data2.write(line.strip() + ",Difficult\n")
    else:
        data2.write(line)
        

data2.close()
data.close()
output.close()
