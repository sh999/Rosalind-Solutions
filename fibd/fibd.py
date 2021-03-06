#!/usr/local/bin/python2.7-32
'''
Mortal Fibonacci
http://rosalind.info/problems/fibd
Solved 7/20/14
'''
import copy 

generations = 80 #May implement file parsing
oldestAge = 16
a = [x for x in range(oldestAge+2)]
b = []
for i in a:
	b.append([i, 0])
b[0] = [0, 1]

c = copy.deepcopy(b) #holds after breed list
adults = 0
total = 0

for gen in range(1, generations):
	adults = 0

	# Shift elements to the right
	for i in range(oldestAge, -1, -1):
		c[i+1][1] = c[i][1]
	c[0][1] = 0  # Age 0 bunny should be none (artifact of shift leaves nonzero value)

	# Breed 
	c[oldestAge][1] = 0
	for i in range(1, oldestAge+1):
		adults = adults + b[i][1]
	
	# Kill rabbits aged OldestAge
	c[0][1] = adults
	
	b = copy.deepcopy(c)
	total = 0
	for i in range(0, len(b)):
		total = total + b[i][1]
print "total = ", total



	
	

		
	
	
	

	
	
