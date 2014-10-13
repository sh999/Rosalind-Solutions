def deleteNewlines(myString):
	myString = myString.replace("\n", "")
	myString = myString.replace(" ", "")
	myString = list(myString)
	return myString




f = open("sampletext.txt")
f = f.readlines()
print f
for i in range(0, len(f)):
	f[i] = deleteNewlines(f[i])
	for j in range(0, len(f[i])):
		f[i][j] = int(f[i][j])
	
print f