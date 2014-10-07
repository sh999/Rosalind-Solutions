'''
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
	

	

