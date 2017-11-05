import io
import re

### import all the labels

comorbs = open("E:\\Inpatient Database Studies\\Sinonasal Surgery\\Comorbidities.ASC", 'r')

diags = {}
procs = {}

for line in comorbs:
        parse = line.strip().split(',D,')
        ID = parse[0]
        theseDiags, theseProcs = parse[1].split(',P,')

        #print theseDiags, theseProcs

        for diag in theseDiags.split(','):
                diag = diag.replace("'","").strip()
                if(len(diag)>2):
                        if(diag in diags):
                                diags[diag] += 1
                        else:
                                diags[diag] = 1


        for proc in theseProcs.split(','):
                proc = proc.replace("'","").strip()
                if(len(proc)>2):
                        if(proc in procs):
                                procs[proc] += 1
                        else:
                                procs[proc] = 1


print diags
print procs

tableDiag = open("E:\\Inpatient Database Studies\\Sinonasal Surgery\\tableDiagnosesNasalCancer.csv", 'w')
tableDiag.write("Diagnosis,Number\n")
tableProc = open("E:\\Inpatient Database Studies\\Sinonasal Surgery\\tableProceduresNasalCancer.csv", 'w')
tableProc.write("Procedure,Number\n")

for aCode, aCount in diags.iteritems():
	tableDiag.write(str(aCode) + "," + str(aCount) + "\n")
	
for aCode, aCount in procs.iteritems():
	tableProc.write(str(aCode) + "," + str(aCount) + "\n")

tableDiag.close()
tableProc.close()
comorbs.close()
