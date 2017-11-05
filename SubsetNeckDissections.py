import re

data = open("surgicalCasesWComplicationsIsDifficult2.csv", 'r')
data2 = open("surgicalCasesWComplicationsIsDifficult3.csv", 'w')

output = open("subsetNeckDissection.csv", 'w')

lineCount = 0

relevantCodes = ["4040", "4041", "4042"]

for line in data:
    lineCount += 1
    written = 0
    
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
                output.write(line)
                written = 1
                #print codes

    if(written == 0):
        data2.write(line)
    else:
        data2.write(line.strip() + ",Difficult\n")

        

data2.close()
data.close()
output.close()
