#!/usr/local/bin/python2.7-32
'''
study of fibonacci mortal
to do:
count # of adults and create offspring
'''
import copy 

ageLimit = 9
a = [x for x in range(ageLimit)]
b = []
for i in a:
	b.append([i, 0])
b[0] = [0, 1]
oldestAge = 3
#b = [[0, 1],[1, 2],[2,2],[3,0],[4,0],[5,0]] #before breed list
c = copy.deepcopy(b) #holds after breed list
adults = 0
total = 0

for gen in range(1, 5):
	print "\ngeneration = ", gen
	print "Original b      = ", b

	# Shift elements to the right
	for i in range(oldestAge, -1, -1):
		c[i+1][1] = c[i][1]
	print "(c) After shift = ", c

	# Breed 
	for i in range(1, oldestAge+1):
		adults = adults + b[i][1]
	c[0][1] = adults
	b = copy.deepcopy(c)
	print "b after process = ", b
	total = 0
	for i in range(0, len(b)):
		#print b[i][1]
		total = total + b[i][1]
	print "total = ", total


print "\nc After breed = ", c


	
	

		
	
	
	

	
	
