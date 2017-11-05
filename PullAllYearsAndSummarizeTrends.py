import io
import re

### import all the labels

codes = open("E:\\Inpatient Database Studies\\I9_Formats.txt", 'r')

pattern = re.compile("\"\\w[\\d ]*\" = \"\\w[\\d ]*:.*\"")
code = re.compile("\"\\w[\\d ]*\"")

#boundedString = re.compile("'[...!']*'")
boundedString = re.compile("'[\w\s+-.\\\\\[\]]*'")

counts = {}
counts["nasalcancer"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

counts["yearSum"] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

header = "code"

relevantDiags = []
relevantDiags.append("1600")
relevantDiags.append("1602")
relevantDiags.append("1603")
relevantDiags.append("1604")
relevantDiags.append("1605")
relevantDiags.append("1608")
relevantDiags.append("1609")
relevantDiags.append("1470")
relevantDiags.append("1471")
relevantDiags.append("1472")
relevantDiags.append("1473")
relevantDiags.append("1478")
relevantDiags.append("1479")

relevantProcs = []
relevantProcs.append("31231")
relevantProcs.append("31233")
relevantProcs.append("31235")
relevantProcs.append("31237")
relevantProcs.append("31238")
relevantProcs.append("31239")
relevantProcs.append("31240")
relevantProcs.append("31254")
relevantProcs.append("31256")
relevantProcs.append("31267")
relevantProcs.append("31276")
relevantProcs.append("31287")
relevantProcs.append("31288")
relevantProcs.append("31290")
relevantProcs.append("31291")
relevantProcs.append("31292")
relevantProcs.append("31293")
relevantProcs.append("31294")
relevantProcs.append("61795")

relevantProcs.append("31000")
relevantProcs.append("31030")
relevantProcs.append("31032")
relevantProcs.append("31040")
relevantProcs.append("31050")
relevantProcs.append("31051")
relevantProcs.append("31070")
relevantProcs.append("31075")
relevantProcs.append("31084")
relevantProcs.append("31085")
relevantProcs.append("31086")
relevantProcs.append("31087")
relevantProcs.append("31205")
relevantProcs.append("31090")

relevantProcs.append("30130")
relevantProcs.append("30140")
relevantProcs.append("30801")
relevantProcs.append("30802")
relevantProcs.append("30930")

relevantProcs.append("30117")
relevantProcs.append("30118")
relevantProcs.append("30120")
relevantProcs.append("30150")
relevantProcs.append("30160")
relevantProcs.append("30300")
relevantProcs.append("30310")
relevantProcs.append("30320")
relevantProcs.append("30400")
relevantProcs.append("30410")
relevantProcs.append("30420")
relevantProcs.append("30430")
relevantProcs.append("30435")
relevantProcs.append("30450")
relevantProcs.append("30520")
relevantProcs.append("30540")
relevantProcs.append("30545")
relevantProcs.append("30620")
relevantProcs.append("30630")
relevantProcs.append("31225")
relevantProcs.append("31230")

### form dictionary of all the labels

for line in codes:

	#print(line)
	
	codeLine = pattern.findall(line)

	#print(len(codeLine))
	
	if(len(codeLine) > 0):
		#print(codeLine)
		
		THIScode = code.findall(codeLine[0])[0].strip("\"\' ")
		#if(len(THIScode) > 0):
		#    if(THIScode[0] == '0'):
		#            THIScode = THIScode[1:len(THIScode)]
		#print THIScode
		counts[THIScode] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


### load year file
### loop through all the diagnoses and procedures

#print counts

print "dict made"




#### Make File to pull demographics

Question = open("NasalCancer.ASC", 'w')
BadLines = open("BadLines.ASC", 'w')
comorb = open("Comorbidities.ASC", 'w')

for i in range(0,5):

	year = 1988 + i

	print year

	header = header + "," + str(year)

	FormatFileName = "E:\\Inpatient Database Studies\\Format" + str(year) + ".csv"
	fileFormat = open(FormatFileName, 'r')

	DXstart = 0
	DXend = 0
	PRstart = 0
	PRend = 0
	WTstart = 0
	WTend = 0
	keyStart = 0
	keyEnd = 0
	hospIDStart = 0
	hospIDEnd = 0
	
	for line in fileFormat:
		items = line.strip().split(',')
		if(items[0] == "DX1"):
			DXstart = int(items[1]) - 1
		if(items[0] == "DX15"):
			DXend = int(items[2])
		if(items[0] == "PR1"):
			PRstart = int(items[1]) - 1
		if(items[0] == "PR15"): 
			PRend = int(items[2])
		if(items[0] == "DISCWT_U"):
			WTstart = int(items[1]) - 1
			WTend = int(items[2])
		if(items[0] == "HOSPID"):
			hospIDStart = int(items[1]) - 1
			hospIDEnd = int(items[2])
		if(items[0].__contains__("KEY") | items[0].__contains__("SEQ") ):
			keyStart = int(items[1]) - 1
			keyEnd = int(items[2])

	fileFormat.close()
	
	#print DXstart, DXend, PRstart, PRend, (DXend-DXstart)/15, (PRend-PRstart)/15, WTstart, WTend
		
	yearFileName = "E:\\Inpatient Database Studies\\NIS_1988-1992\\" + str(year) + "\\Data\\NIS" + str(year%1900) + "weighted.asc"
	yearFile = open(yearFileName, "r")

	lineCount = 0
	
	for line in yearFile:
		lineCount += 1

		#print line
		#print len(line)
		
		diag = line[DXstart:DXend]
		proc = line[PRstart:PRend]
		key = line[keyStart:keyEnd]

		#print "D:" + diag
		#print "P:" + proc
		#print "W:" + line[WTstart:WTend]

		counts["yearSum"][i]  = counts["yearSum"][i] + float(line[WTstart:WTend])
		
		#print line[WTstart:WTend]
		
		allCodes = {}
		allDiags = {}
		allProcs = {}
		
		for fifteen in range(0,15):
			thisDiag = diag[(fifteen*5):(fifteen*5+5)].strip("\"\' ")
			thisProc = proc[(fifteen*4):(fifteen*4+4)].strip("\"\' ")

			allCodes[thisDiag] = 1
			allCodes[thisProc] = 1

			allDiags[thisDiag] = 1
			allProcs[thisProc] = 1
			
		   #print thisDiag,thisProc, diag, proc

			if thisDiag in counts:
				counts[thisDiag][i] = counts[thisDiag][i] + float(line[WTstart:WTend])
			else:
				BadLines.write("D" + " " + thisDiag + " " + diag + ":" + line)
				counts[thisDiag] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				counts[thisDiag][i] = counts[thisDiag][i] + float(line[WTstart:WTend])

			if thisProc in counts:
				counts[thisProc][i] = counts[thisProc][i] + float(line[WTstart:WTend])
			else:
				BadLines.write("P" + " " + thisProc + " " + proc + ":" + line)
				counts[thisProc] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				counts[thisProc][i] = counts[thisProc][i] + float(line[WTstart:WTend])


		hasCancer = bool(0)
		hasSurgery = bool(0)

		for diagnosis in relevantDiags:
			if diagnosis in allCodes:
				hasCancer = bool(1)
		for procedure in relevantProcs:
			if procedure in allCodes:
				hasSurgery = bool(1)

			
			
		if((hasCancer)):
			#print("BINGO")
			counts["nasalcancer"][i] = counts["nasalcancer"][i] + float(line[WTstart:WTend])
			Question.write(str(year) + " " + line)
			comorb.write(key + ",D," + str(allDiags.keys()).strip("[] ") + ",P," + str(allProcs.keys()).strip("[] ") + "\n")
			#print("yes")




	print counts["yearSum"][i]
	print counts["nasalcancer"]
	


################# 1993 - 1998 ####################

nokeycount = 0

for i in range(5,10):
	

	year = 1988 + i

	print(year)

	header = header + "," + str(year)
		
	yearFileName = "E:\\Inpatient Database Studies\\Unnormalized" + str(year) + ".asc"
	yearFile = open(yearFileName, "r")

	for line in yearFile:

		
		importantStuff = re.findall(boundedString, line)

		if(len(importantStuff) == 3):
			#print importantStuff

			diag = importantStuff[0].strip('\'\" ')
			proc = importantStuff[1].strip('\'\" ')
			weight = float((importantStuff[2]).strip('\'\" '))

		
			counts["yearSum"][i]  = counts["yearSum"][i] + weight
			
			allCodes = {}
			allDiags = {}
			allProcs = {}
			
			for ii in range(0,len(diag)/5):
				thisDiag = diag[(ii*5):(ii*5+5)].strip("\"\' ")
				allCodes[thisDiag] = 1
				allDiags[thisDiag] = 1

				if thisDiag in counts:
					counts[thisDiag][i] = counts[thisDiag][i] + weight
				else:
					BadLines.write("D" + " " + thisDiag + "     " + line)
					counts[thisDiag] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
					counts[thisDiag][i] = counts[thisDiag][i] + weight



			for ii in range(0,len(proc)/4):    
				thisProc = proc[(ii*4):(ii*4+4)].strip("\"\' ")          
				allCodes[thisProc] = 1
				allProcs[thisProc] = 1
				
				if thisProc in counts:
					counts[thisProc][i] = counts[thisProc][i] + weight
				else:
					BadLines.write("P" + " " + thisProc + "     " + line)
					counts[thisProc] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
					counts[thisProc][i] = counts[thisProc][i] + weight


			hasCancer = bool(0)
			hasSurgery = bool(0)

			for diagnosis in relevantDiags:
				if diagnosis in allCodes:
					hasCancer = bool(1)
			for procedure in relevantProcs:
				if procedure in allCodes:
					hasSurgery = bool(1)

				
				
			if((hasCancer)):
				counts["nasalcancer"][i] = counts["nasalcancer"][i] + weight
				Question.write(str(year) + " " + line)
				comorb.write(key + ",D," + str(allDiags.keys()).strip("[] ") + ",P," + str(allProcs.keys()).strip("[] ") + "\n")
				#print("yes")




	print counts["yearSum"][i]
	print counts["nasalcancer"]
	

############### 1998 - 2009 #############


for i in range(10,22):


	year = 1988 + i

	print year

	header = header + "," + str(year)

	FormatFileName = "E:\\Inpatient Database Studies\\Format" + str(year) + ".csv"
	fileFormat = open(FormatFileName, 'r')

	DXstart = 0
	DXend = 0
	PRstart = 0
	PRend = 0
	WTstart = 0
	WTend = 0
	keyStart = 0
	keyEnd = 0
	
	for line in fileFormat:
		items = line.strip().split(',')
		if(items[0] == "DX1"):
			DXstart = int(items[1]) - 1
		if(items[0] == "DX15"):
			DXend = int(items[2]) - 0
		if(items[0] == "PR1"):
			PRstart = int(items[1]) - 1
		if(items[0] == "PR15"): 
			PRend = int(items[2]) - 0
		if(items[0] == "DISCWT"):
			WTstart = int(items[1]) - 1
			WTend = int(items[2])
		if(items[0].__contains__("KEY") | items[0].__contains__("SEQ") ):
			keyStart = int(items[1]) - 1
			keyEnd = int(items[2])


	fileFormat.close()
	
	#print DXstart, DXend, PRstart, PRend, (DXend-DXstart)/15, (PRend-PRstart)/15, WTstart, WTend
		
	yearFileName = "E:\\Inpatient Database Studies\\NIS_" + str(year) + "\\Data\\NIS_" + str(year) + "_CORE.asc"
	yearFile = open(yearFileName, "r")

	lineCount = 0
	
	for line in yearFile:
		lineCount += 1

		#print line
		#print len(line)
		
		diag = line[DXstart:DXend]
		proc = line[PRstart:PRend]
		
		key = line[keyStart:keyEnd]

		#print "D:" + diag
		#print "P:" + proc
		#print "W:" + line[WTstart:WTend]

		counts["yearSum"][i]  = counts["yearSum"][i] + float(line[WTstart:WTend])
		
		#print line[WTstart:WTend]
		
		allCodes = {}
		allDiags = {}
		allProcs = {}
		
		for fifteen in range(0,15):
			thisDiag = diag[(fifteen*5):(fifteen*5+5)].strip("\"\' ")
			thisProc = proc[(fifteen*4):(fifteen*4+4)].strip("\"\' ")

			allCodes[thisDiag] = 1
			allCodes[thisProc] = 1

			allDiags[thisDiag] = 1
			allProcs[thisProc] = 1
			
		   #print thisDiag,thisProc, diag, proc

			if thisDiag in counts:
				counts[thisDiag][i] = counts[thisDiag][i] + float(line[WTstart:WTend])
			else:
				BadLines.write("D" + " " + thisDiag + "     " + line)
				counts[thisDiag] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				counts[thisDiag][i] = counts[thisDiag][i] + float(line[WTstart:WTend])

			if thisProc in counts:
				counts[thisProc][i] = counts[thisProc][i] + float(line[WTstart:WTend])
			else:
				BadLines.write("D" + " " + thisProc + "     " + line)
				counts[thisProc] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				counts[thisProc][i] = counts[thisProc][i] + float(line[WTstart:WTend])

		hasCancer = bool(0)
		hasSurgery = bool(0)

		for diagnosis in relevantDiags:
			if diagnosis in allCodes:
				hasCancer = bool(1)
		for procedure in relevantProcs:
			if procedure in allCodes:
				hasSurgery = bool(1)

			
			
		if((hasCancer)):
			#print("BINGO")
			counts["nasalcancer"][i] = counts["nasalcancer"][i] + float(line[WTstart:WTend])
			Question.write(str(year) + " " + line)
			comorb.write(key + ",D," + str(allDiags.keys()).strip("[] ") + ",P," + str(allProcs.keys()).strip("[] ") + "\n")
			#print("yes")




	print counts["yearSum"][i]
	print counts["nasalcancer"]



BadLines.close()
Question.close()
comorb.close()

#"I:\Inpatient Database Studies\NIS_" + str(year) + "\Data\NIS_" + str(year) + "_CORE.asc"
print counts["nasalcancer"]

		
### print the dictionary

writeSummary = open("AllSummaryWeightsPrior.csv", 'w')

writeSummary.write(header + "\n")


for aCode, aCount in counts.iteritems():
	writeSummary.write(aCode + "," + str(aCount).strip("[]") + "\n")

writeSummary.close()
