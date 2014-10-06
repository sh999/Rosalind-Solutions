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
intAmt = 100
intBound = 100000
randInts = random.sample(xrange(-intBound,intBound), intAmt)
randInts.sort()
key = [43,10]
positionList = []
for i in key:
	positionList.append(findKey(randInts, i))
print positionList
	

	

