#!/usr/local/bin/python2.7-32
# done 7/13/14
inputFile = open("rosalind_fibd.txt", 'r')
parsed = []
for lines in inputFile:
	parsed.extend(lines.split())
print parsed


aList = [0]
#ageOfDeath = int(parsed[1])
#months = int(parsed[0])
ageOfDeath = 17
months = 30
months = months + 1
for gen in range(1, months):
	#print "\ngeneration = ", gen	
	#print "list = ", aList
	#print "total = ", len(aList)
	childList = []
	nextGen = []
	trunc = 0
	for i in range(0, len(aList)):
		# if element is above age 0, create offspring
		if aList[i] > 0:
			childList.extend([0])
		# make element older
		aList[i] = aList[i]+1
	# essentially deletes elements that are 
	'''for i in range(0, len(aList)):
		if aList[i] == ageOfDeath:
			trunc = i

			#nextGen.extend([aList[i]])

	aList = nextGen '''
	# add offsprings into current list	
	aList.extend(childList)
print "total = ", len(aList)
inputFile.close()




	
	

		
	
	
	

	
	

