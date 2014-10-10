inputData = open("sampletext.txt")
a = []
b = {}
for i, j in enumerate(inputData.readlines()): # Convert string data into list of lists
	a.append([])
	a[i].extend([int(j[0])])
	a[i].extend([int(j[2])])
b = {key:0 for key in range(1,a[0][0]+1)} # initialize empty dictionary with all keys based on known vertex numbers
for j, i in enumerate(a):
	if j < 1: continue # allows iteration of list but do nothing on first element (heading of graph data not part of calculation)
	b[i[0]] += 1
	b[i[1]] += 1
print b
c = b.values()
print c
# outputFile = open("output.txt", "w")
# outputFile.write(str(a))

