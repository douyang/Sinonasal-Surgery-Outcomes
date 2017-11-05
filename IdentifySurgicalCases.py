import re

unweightedData = open("unweightedNasalCancerWithDiagsAndProcsAll.csv", 'r')
primarySinonasal = open("primary160.csv", 'w')
surgicalCases = open("surgicalCases.csv", 'w')


relevantDiags = ["1600", "1601", "1602", "1603", "1604", "1605", "1606", "1607", "1608", "1609"]
relevantProcs = ["2262", "2263", "0214", "2211", "7639", "4041", "2131", "215", "2264", "2261", "0159", "1651", "2122", "2239", "2242", "2242", "2231", "2212", "7644", "2183", "7645", "2132", "0124", "2732", "2260", "2252", "4042", "1692", "0762", "0864", "0125", "222", "2912", "0981", "2721", "2169", "2241", "7631", "1609", "2742", "4011", "2130", "2186", "2219", "2749", "8663", "7611", "0206", "229", "4040", "2199", "1623", "0204", "2185", "1602", "1652"]

lineCount = 0

for line in unweightedData:

    lineCount = lineCount + 1

    if(lineCount == 1):
        surgicalCases.write(line)
        primarySinonasal.write(line)
        
    data = line.strip().split(',')
    primaryDiag = data[15]
    primaryProc = data[30]

    good = bool(0)

    if(primaryDiag in relevantDiags):

        primarySinonasal.write(line)
        
        if(primaryProc  in relevantProcs):
            good = bool(1)

    if(primaryProc == "    "):
        good = bool(0)
        
    if(good):
        #print primaryDiag, primaryProc, len(primaryDiag), len(primaryProc)
        surgicalCases.write(line)

unweightedData.close()
primarySinonasal.close()
surgicalCases.close()
