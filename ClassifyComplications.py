import io
import re

# For years 1993 - 1997 , the files are split among two lines, they need to be jointed into one line.

thisFile = open("surgicalCases.csv", 'r')
newFile = open("ComplicationsOverTime.csv", 'w')

cardiopulm = ["41071", "42611", "4279", "4279", "4254", "4264", "4280",
                 "42731", "4108", "42789", "9971", "42769", "4275",
              "51881", "5180", "5185", "5119", "9973"]

electrolyte = ["2768", "2761", "2767", "2752", "2760", "2769"]
neuro = ["3526", "37854", "37853", "37852", "37851"]
eye = ["36960", "3688", "3698", "37851", "3699", "36900", "3693", "36840"]

infectious = ["5990", "486", "6820", "4610", "37601", "9985"]

other = ["99702", "99811"]

lineCount = 0
isComplicated = bool(0)

for line in thisFile:

    isComplicated = bool(0)
    
    lineCount = lineCount + 1
    compType = ""

    if(lineCount == 1):
        newFile.write(line.strip() + ",complications,compType\n")
    else:
        data = (line.strip()).split(',')

        if(data[3] == "1"):
            isComplicated = bool(1)
            compType = "death"
            newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")

        for i in range(15,31):
            if(data[i] in cardiopulm):
                isComplicated = bool(1)
                compType = "Cardiopulm"
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")
            if(data[i] in electrolyte):
                isComplicated = bool(1)
                compType = "Electrolyte"
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")
            if(data[i] in neuro):
                isComplicated = bool(1)
                compType = "neuro"
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")
            if(data[i] in eye):
                isComplicated = bool(1)
                compType = "eye"
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")
            if(data[i] in infectious):
                isComplicated = bool(1)
                compType = "infectious"
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")
            if(data[i] in other):
                isComplicated = bool(1)
                compType = "other"
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")


            if(not(isComplicated)):
                newFile.write(line.strip() + "," + str(isComplicated) + "," + compType + "\n")
                
    

thisFile.close()
newFile.close()
