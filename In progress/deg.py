def deleteNewlines(myString):
	myString = myString.replace("\n", "")
	myString = myString.replace(" ", "")
	myString = list(myString)
	return myString

def getInputList1(fileName):
	a = open(fileName)
	a = a.readlines()
	for i in range(0, len(a)):
		a[i] = deleteNewlines(a[i])
		for j in range(0, len(a[i])):
			a[i][j] = int(a[i][j])
	return a

def getInputList2(fileName):
	inputData = open(fileName)
	a = [] # List that takes in input file
	for i, j in enumerate(inputData.readlines()): # Convert string data into list of lists
		a.append([])
		a[i].extend([int(j[0])])
		a[i].extend([int(j[2])])
	return a
a = getInputList1("sampletext.txt")
b = {} # Dict of vertex:degree value

b = {key:0 for key in range(1,a[0][0]+1)} # initialize empty dictionary with all keys based on known vertex numbers
for j, i in enumerate(a):
	if j < 1: continue # allows iteration of list but do nothing on first element (heading of graph data not part of calculation)
	b[i[0]] += 1
	b[i[1]] += 1
print b
c = b.values()
print c
print 'a = ',a
# outputFile = open("output.txt", "w")
# outputFile.write(str(a))

