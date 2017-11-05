import io
import re

comorb = open("Comorbidities.ASC", 'r')
norm = open("morbidity.csv", 'w')

norm.write("key,code\n")

for line in comorb:
    #print(line)
    
    codes = line.split(',')
    key = codes[0]

    for i in range(1,len(codes)):
        newCode = codes[i].replace( '\'', '').strip()
        newdiag = key + "," + newCode + '\n'
        norm.write(newdiag)
        #print(newdiag)

norm.close()

