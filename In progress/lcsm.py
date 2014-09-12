'''
http://rosalind.info/problems/lcsm/
9/7:
Can get basic algorithm of finding longest match.
Work on getting breaking out of the loop after finding match (use functions instead of breaks)
Then generalize into functions to take arbitrary # of sequences (Done 8/9)
Make shortest function
	make it accept variable argument numbers
'''
from FASTA_extract import *


def substringList(s):
	substrings = []
	for window in range(1, len(s)+1):
		substrings.append([])
		for i in range(0, len(s)-window+1):
			substrings[len(substrings)-1].append(s[i:i+window])
	return substrings


def shortest(a, b, c):
	d = []
	d.extend([a,b,c])
	shortest = len(a)
	for i in d:
		if len(i) <= shortest:
			shortest = len(i)
	print shortest

a = 'GATTACA'
aL = substringList(a)
b = 'TAGACCA'
bL = substringList(b)
c = 'GAT'
cL = substringList(c)

# shortest = shortest(a, b, c)

# Backward iteration test
'''
print "aL and bL = "
print bL
print "aL iterated backwards = "
for i in range(len(aL)-1, -1, -1):
	print aL[i]
print "bL iterated backwards = "
for i in range(len(bL)-1, -1, -1):
	print bL[i]'''



i = len(aL)-1 # index of last element of aL
keepLooping = True
while keepLooping and i > -1:	
	for j, val in enumerate(aL[i]): # loop through each element of aL until it finds match in corresponding element in bL (each element has many entries)
		print "Checking if",val,"is in.. bL:", bL[i],"..and cL:", cL[i]
		if val in bL[i] and val in cL[i]:
			keepLooping = False
			
			match = val
			print 'match found =', match
			break
	i -= 1
			


	
	

'''
window = 3
for i in range(0, len(a)-window+1):
	# print a[i:i+window]
	aL.append(a[i:i+window])
print aL
'''

'''
for i in range(1,len(a)+1):
	aL.append(a[0:i])
print aL

for i in range(1,len(b)+1):
	bL.append(b[0:i])
print bL

for i in range(0, len(aL)):
	print aL[i], bL[i]'''


