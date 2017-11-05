import re

data = open("surgicalCasesWComplicationsIsDifficult.csv", 'r')

data2 = open("surgicalCasesWComplicationsIsDifficult2.csv", 'w')

output = open("subsetNeurosurgery.csv", 'w')

lineCount = 0

relevantCodes = [ "159", "206", "151", "442", "118", "203", "124", "153", "131", "139", "204", "202", "212"]

stringent = ["1652", "1692", "1651", "2231", "2262", "1609", "1602", "2239"]

for line in data:
    lineCount += 1

    codes = ""
    written = 0
    
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
                if("2263" in codes):
                    for second in stringent:

                       
                        
                        if(second in codes and written == 0):
                            
                            written = 1
                            output.write(line)
                #print codes
        
    if(written == 1):    
        data2.write(line.strip() + ",Difficult\n")
    else:
        data2.write(line)
        

data2.close()
data.close()
output.close()
