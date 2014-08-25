'''
Rosalind 
Calculated Expected offsprings
8/24/14
'''
def mate(parent1, parent2):
	allelesOfP1 = [x for x in parent1]
	allelesOfP2 = [x for x in parent2]
	offsprings = []
	for allele1 in allelesOfP1:
		for allele2 in allelesOfP2:
			offsprings.extend([allele1+allele2])
	return offsprings

def domPhenotypes(offsprings, numOfCouples):
	dom = 0
	for i in offsprings:
		if i[0] == 'A' or i[1] == 'A':
			dom += 1
	domFreq = dom/4.0
	expectedDom = numOfCouples * 2 * domFreq
	return expectedDom

def getDataSet():
	inputFile = open("rosalind_iev.txt")
	inputFile = inputFile.readlines()
	inputFile = "".join(inputFile)
	inputFile = inputFile.split()
	inputFile = map(int, inputFile)
	return [17275,16971, 19158, 19008, 19144, 19582]

dataset = getDataSet()
parentsList = {'AA-AA':0,'AA-Aa':0,'AA-aa':0,'Aa-Aa':0,'Aa-aa':0,'aa-aa':0,}
childrenList = {'AA-AA':0,'AA-Aa':0,'AA-aa':0,'Aa-Aa':0,'Aa-aa':0,'aa-aa':0,}
parentsList['AA-AA'] = dataset[0]
parentsList['AA-Aa'] = dataset[1]
parentsList['AA-aa'] = dataset[2]
parentsList['Aa-Aa'] = dataset[3]
parentsList['Aa-aa'] = dataset[4]
parentsList['aa-aa'] = dataset[5]

for couple in parentsList:
	childrenList[couple] = domPhenotypes(mate(couple[0:2],couple[3:5]),parentsList[couple])
tot = 0
for child in childrenList:
	tot = tot + childrenList[child]
print tot