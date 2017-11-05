import io
import re

Questions = open("NasalCancerAndSurgery.ASC", 'r')
newQuestions = open("fullNasalCancerAndSurgery.ASC", 'w')

needToNormalize = []
needYears = []

for line in Questions:
    if ((int(line[0:4]) <= 1997) & (int(line[0:4]) >= 1993)):
        needToNormalize.append(line[5:18])
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
                newQuestions.write(str(year) + " " + line)
                print("Normalized!" + ID)
            
                      
    print year

    yearFile.close()
