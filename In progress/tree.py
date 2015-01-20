'''
tree.py
The tree of life
http://rosalind.info/problems/tree/

Notes:
-Draw tree of example file, and you can see that it results in 3 independent graph
-For every independent graph, that is how many minimum edges are needed
to the graph to produce one graph, which is the answer
-Note that input file may have missing nodes 
-Strategy:
	Iterate through edge pair
	Check if any node in the pair has a group idassociated with it
		In first edge pair, none will have group, so create group 1, representing an independent graph
	If one node in the edge pair has no group id, but the other one has, copy the other's group id to that first node
		e.g. if in "2 3" the group id is "1 None" then turn this to "1 1", meaning node 3 will belong to group 1
	After iterating, each node will have a group id associated
	The number of groups will be the solution of the puzzle
-Todo:

'''

def processFile(filename):
	f = open(filename)
	f = f.readlines() # Splits file into processable strings: f = [...,'Node1 Node2\n',...]
	for i in range(0, len(f)):
		f[i] = f[i].split() 
		for j in range(0, len(f[i])):
			f[i][j] = int(f[i][j]) # Results in the form of [[a,b],...] (2d list)
	return f # See above for what the list looks like

def assignGroups(inputList):
	print 'assigning..'
	groupIDs = {}
	for i in range(1, len(inputList)):
		print '\npair#',i
		for j in range(0, len(inputList[i])):
			print "node = ",inputList[i][j]
			checkForID(node)
	pass

def checkForID(node):
	pass

def outputResult():
	pass

def main():
	# processFile("sampletext.txt")
	inputList = processFile("sampletext.txt")
	assignGroups(inputList)
	print inputList
	
main()
