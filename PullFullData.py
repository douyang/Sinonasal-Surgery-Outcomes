import io
import re

Questions = open("NasalCancer.ASC", 'r')
newQuestions = open("fullNasalCancer.ASC", 'w')

needToNormalize = []
needYears = []
comorbs = {}

for line in Questions:
    if ((int(line[0:4]) <= 1997) & (int(line[0:4]) >= 1993)):
        needToNormalize.append(line[5:18])
        comorbs[line[5:18]] = line
        needYears.append(line[0:4])
        #print(line[6:20])
    else:
        newQuestions.write(line)
        

for IDs in needToNormalize:
    print IDs

for year in range(1993,1998):

    yearFile = open("E:\\Inpatient Database Studies\\NIS_" + str(year) + "\\Data\\NIS" + str(year % 1900) + "_A.ASC", 'r')

    for line in yearFile:
        for ID in needToNormalize:
            if(line.__contains__(ID)):
                newQuestions.write(str(year) + "_" + line + "_" + comorbs[ID])
                print("Normalized!" + ID)
            
                      
    print year

    yearFile.close()
