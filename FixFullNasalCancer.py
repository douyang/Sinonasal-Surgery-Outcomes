import io
import re

# For years 1993 - 1997 , the files are split among two lines, they need to be jointed into one line.

thisFile = open("fullNasalCancer.ASC", 'r')
newFile = open("fullNasalCancerFixed.ASC", 'w')

previousLine = ""
years = ["1993_", "1994_", "1995_", "1996_", "1997_"]

for line in thisFile:
    if (line[0:5] in years):
        previousLine = line.rstrip()
    else:
        newFile.write(previousLine + line)
        previousLine = ""
    

thisFile.close()
newFile.close()
