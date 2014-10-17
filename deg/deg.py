def getInputList(filename): # based on deg-multidig parser.py
	f = open(filename)
	f = f.readlines()
	for i in range(0, len(f)):
		f[i] = deleteNewLines(f[i])
		for j in range(0, len(f[i])):
			f[i][j] = int(f[i][j]) # Causes the form of [[a,b],...] (2d list)
	return f

def deleteNewLines(myString): # called by getInputList()
	myString = myString.split()
	myString = list(myString) # needed?
	return myString

def getDict(a):
	b = {} # Dict of vertex:degree value
	b = {key:0 for key in range(1,a[0][0]+1)} # initialize empty dictionary with all keys based on known vertex numbers
	
	for j, i in enumerate(a):
		if j < 1: continue # allows iteration of list but do nothing on first element (heading of graph data not part of calculation)
		b[i[0]] += 1
		b[i[1]] += 1
	return b

def getResult(b):
	result = b.values()
	result = str(result)
	result = result.translate(None, "[],")
	return result

a = getInputList("sampletext.txt") # converts raw text file to list
b = getDict(a) # converts above list to a dictionary
result = getResult(b) # ensures appropriate output format
