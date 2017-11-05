import io
import re

# For years 1993 - 1997 , the files are split among two lines, they need to be jointed into one line.

thisFile = open("surgicalCases.csv", 'r')
newFile = open("surgicalCasesWComplications.csv", 'w')

complications = ["41071", "42611", "4279", "4254", "4264", "4280", "42731",
                 "4018", "42789", "9971", "42769", "4275", "2768", 
                 "2761", "2767", "2752", "2760", "2769", "3526",
                 "37854", "37853", "37852", "37851", "36960", "3688",
                 "3698", "37851", "3699", "36900", "3693", "36840",
                 "5990", "486", "6820", "4610", "37601", "9985",
                 "51881","5180","5185","5119","9973","99702"]
lineCount = 0
isComplicated = bool(0)

for line in thisFile:

    isComplicated = bool(0)
    
    lineCount = lineCount + 1

    if(lineCount == 1):
        newFile.write(line.strip() + ",complications\n")
    else:
        data = (line.strip()).split(',')

        if(data[3] == "1"):
            isComplicated = bool(1)

        for i in range(15,31):
            if(data[i] in complications):
                isComplicated = bool(1)
        
        newFile.write(line.strip() + "," + str(isComplicated) + "\n")
    

thisFile.close()
newFile.close()
