'''
<<<<<<< HEAD
Attempt if can process example, no parsing from file yet
'''
=======
bins.py
Binary Search
http://rosalind.info/problems/bins/
'''
import random

def parseFile():
	pass

def printStatus():
	print "Random integers = ", randInts
	print "key = ", key	
	print "lower pivot = ", lowerBoundPivot
	print "upper pivot = ", upperBoundPivot
	print "pivotPos = ", pivotPos
	print "randInt[pivotPos] = ", randInts[pivotPos]

>>>>>>> 5554f34772c54f840202c4f015830ecd5e732ffa
def findKey(randInts, key):
	upperBoundPivot = len(randInts)
	lowerBoundPivot = 0
	pivotPos = (upperBoundPivot - lowerBoundPivot)/2 + lowerBoundPivot
	terminate = False
	counter = 0 #Safeguard for infinite loops
	while terminate == False:
		if key > randInts[pivotPos]:
			# print 'larger'
			lowerBoundPivot = pivotPos
		elif key < randInts[pivotPos]:
			# print 'smaller'
			upperBoundPivot = pivotPos
		elif key == randInts[pivotPos]:
			print 'equal'
			terminate = True
		pivotPos = (upperBoundPivot - lowerBoundPivot)/2 + lowerBoundPivot
		counter += 1
		if counter > 100:
			return -1
			terminate = True
	
	print "position = ",pivotPos
<<<<<<< HEAD
	return pivotPos + 1

# a = ['5\n', '6\n', '10 20 30 40 50\n', '40 10 35 15 40 20']
# print a
a = open("sampletext.txt").readlines()
print a
n = int(a[0]) # Number of integers to be searched against
m = int(a[1]) # Number of keys to be searched for
positionList = [] 
intList = a[2].split() # Convert string of ints to list of ints
intList = [int(intList[i]) for i in range(0, len(intList))]
keyList = a[3].split()
keyList = [int(keyList[i]) for i in range(0, len(keyList))]

for i in keyList:
	positionList.append(findKey(intList, i)) # findKey returns position of key in the random list

positionList = str(positionList)
positionList = positionList.translate(None,"[],")
print positionList
=======
	return pivotPos

inputFile = open("sampletext.txt")
print inputFile.readlines()
intAmt = 100 # number of integers in list
intBound = 100000 # -intBound to +intBound is the range of random integers
randInts = random.sample(xrange(-intBound,intBound), intAmt) # Create random integers in bound with specific amt
randInts.sort()
key = [43,10] # numbers to find in the sorted random list
positionList = []
for i in key:
	positionList.append(findKey(randInts, i)) # findKey returns position of key in the random list
print positionList
	

	

>>>>>>> 5554f34772c54f840202c4f015830ecd5e732ffa
