#!usr/local/bin/python2.7-5
'''
http://rosalind.info/problems/subs/
Finding a motif in DNA
Rosalind problem
'''
source = open("rosalind_subs.txt")
source = source.readlines()
reference = source[0].replace("\n","")
query = source[1].replace("\n","")
print reference
print query
scanLocation = 0
scanUntil = len(reference) - len(query) + 1
temp = ''
matches = 0
matchLocations = []
for loc in range(0, scanUntil):	
	for j in range(loc, loc+len(query)):
		temp = temp + reference[j]
	if temp == query:
		matches += 1
		matchLocations.extend([loc+1])
	temp = ''
print matches
print matchLocations


