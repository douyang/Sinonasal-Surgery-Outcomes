import io
import re

Questions = open("fullNasalCancerCertainYears.ASC", 'r')
unweightedData = open("unweightedNasalCancerWithDiagsAndProcs.csv", 'w')


unweightedData.write('weight,year,age,died,pay1,pay2,sex,hospital,los,race,charges,zip,atype,disp,,diagnoses\n') #,IDENTIFIER


relevantDiags = []

relevantDiags.append("1600")
relevantDiags.append("1602")
relevantDiags.append("1603")
relevantDiags.append("1604")
relevantDiags.append("1605")
relevantDiags.append("1608")
relevantDiags.append("1609")

for line in Questions:
    year = line[0:4]
    restOfLine = line[5:len(line)]

    #if(int(year)>1997):
    #    restOfLine = " " + restOfLine[0:len(restOfLine)]

    #if(int(year)<1993):
    #    restOfLine = restOfLine[1:len(restOfLine)]
    
    #if(str(year) in range(1993,1998)):
    #    restOfLine = line[5:len(line)]
    #else:
    #    restOfLine = line[6:len(line)]
        ###weird formatting error from PullAllYearsFromTLEandEpilepsy such that years 1993 - 1997 has only one space after year

    fileFormat = open("E:\\Inpatient Database Studies\\Format" + str(year) + ".csv")

    ageStart = 0
    ageEnd = 0
    diedStart = 0
    diedEnd = 0
    pay1Start = 0
    pay1End = 0
    pay2Start = 0
    pay2End = 0
    femaleStart = 0
    femaleEnd = 0
    hospitalStart = 0
    hospitalEnd = 0
    weightStart = 0
    weightEnd = 0
    losStart = 0
    losEnd = 0
    raceStart = 0
    raceEnd = 0
    chargesStart = 0
    chargesEnd = 0
    zipIncStart = 0
    zipIncEnd = 0
    atypeStart = 0
    atypeEnd = 0
    dispStart = 0
    dispEnd = 0
    diagStart = 0
    diagEnd = 0
    procStart = 0
    procEnd = 0

    
    for Fline in fileFormat:
        items = Fline.strip().split(',')
        if(items[0] == "AGE"):
            ageStart = int(items[1]) - 1
            ageEnd = int(items[2])
            
        if(items[0] == "DIED"):
            diedStart = int(items[1])- 1
            diedEnd = int(items[2])

        if(items[0] == "PAY1"):
            pay1Start = int(items[1])- 1
            pay1End = int(items[2])

        if(items[0] == "PAY2"):
            pay2Start = int(items[1])- 1
            pay2End = int(items[2])

        if((items[0] == "SEX") | (items[0] == "FEMALE")):
            femaleStart = int(items[1])- 1
            femaleEnd = int(items[2])

        if(items[0] == "HOSPID"):
            hospitalStart = int(items[1])- 1
            hospitalEnd = int(items[2])

        if((items[0] == "DISCWT") | (items[0] == "DISCWT_U")):
            weightStart = int(items[1])- 1
            weightEnd = int(items[2])

        if(items[0] == "LOS"):
            losStart = int(items[1])- 1
            losEnd = int(items[2])

        if((items[0] == "ZIPINC_QRTL") | (items[0] == "ZIPINC4") | (items[0] == "ZIPINC")):
            zipIncStart = int(items[1])- 1
            zipIncEnd = int(items[2])    


        if(items[0] == "RACE"):
            raceStart = int(items[1])- 1
            raceEnd = int(items[2])

        if(items[0] == "TOTCHG"):
            chargesStart = int(items[1])- 1
            chargesEnd = int(items[2])


        if(items[0] == "ATYPE"):
            atypeStart = int(items[1])- 1
            atypeEnd = int(items[2])

        if((items[0] == "DISP") | (items[0] == "DISPUNIFORM")):
            dispStart = int(items[1])- 1
            dispEnd = int(items[2])

        if(int(year) <= 1992 or int(year) >= 1998):
            if(items[0] == "DX1"):
                diagStart = int(items[1])- 1
            if(items[0] == "DX15"):
                diagEnd = int(items[2])
            if(items[0] == "PR1"):
                procStart = int(items[1])- 1
            if(items[0] == "PR15"):
                procEnd = int(items[2])

            


    ### Hopefully this is not needed
    #if(int(year) > 1997):
    #    ageStart -= 14
    #    ageEnd -= 14
    #    diedStart -= 14
    #    diedEnd -= 15
    #    pay1Start -= 15
    #    pay1End -= 15
    #    pay2Start -= 15
    #    pay2End -= 15
    #    femaleStart -= 15
    #    femaleEnd -= 15
    #    hospitalStart -= 15
    #    hospitalEnd -= 15
    #    weightStart -= 15
    #    weightEnd -= 15
    #    losStart -= 15
    #    losEnd -= 15
    #    raceStart -= 15
    #    raceEnd -= 15
    #    chargesStart -= 15
    #    chargesEnd -= 15
        
    age = restOfLine[ageStart:ageEnd]
    died = restOfLine[diedStart:diedEnd]
    pay1 = restOfLine[pay1Start:pay1End]
    pay2 = restOfLine[pay2Start:pay2End]
    female = restOfLine[femaleStart:femaleEnd]
    disp = restOfLine[dispStart:dispEnd]

    ### Inconsistency between FEMALE and SEX
    if(int(year) < 1998):
        female = " "+ str((int(female) - 1))
    
    hospital = restOfLine[hospitalStart:hospitalEnd]
    weight = restOfLine[weightStart:weightEnd]
    los = restOfLine[losStart:losEnd]
    race = restOfLine[raceStart:raceEnd]
    charges = restOfLine[chargesStart:chargesEnd]
    zipInc = restOfLine[zipIncStart:zipIncEnd]
    atype = restOfLine[atypeStart:atypeEnd]
    diagnoses = restOfLine[diagStart:diagEnd]
    procedures = restOfLine[procStart:procEnd]
    #print procedures

    diags = ""
    procs = ""

    for i in range(0,15):
        diags = diags + "," + diagnoses[(i*5):(i*5+5)]
        procs = procs + "," + procedures[(i*4):(i*4+4)]

    #print diags    
    #print procs
    
    #identifier = restOfLine.split("COMORBS: ")[1].split(",D ,")[0]
    
    summary =  year + "," + age+ "," +died+ "," +pay1+ "," +pay2+ "," +female + "," + hospital + "," + los + "," + race + "," + charges + "," + zipInc + "," + atype + "," + disp + "," + diags + procs #+ "," + identifier

    #if(year == "1998"):
    #    weight = "A 3"

    isRelevant = bool(0)

    for this in relevantDiags:
        if this in diags:
            isRelevant = bool(1)

    if(isRelevant):        
        unweightedData.write(weight + "," + summary + "\n")
    #write it based on the number of times it appears, rounded to nearest .01 of weight

    fileFormat.close()
Questions.close()
unweightedData.close()
