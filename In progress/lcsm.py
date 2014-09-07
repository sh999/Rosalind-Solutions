'''
http://rosalind.info/problems/lcsm/
9/7:
Can get basic algorithm of finding longest match.
Work on getting breaking out of the loop after finding match (use functions instead of breaks)
Then generalize into functions to take arbitrary # of sequences
'''
from FASTA_extract import *
# seqList = seqList("sampletext.txt")
# for i in seqList:
a = 'ATTA'
aL = []
b = 'ATTC'
bL = []
print "aL and bL = "
for window in range(1, len(a)+1):
	aL.append([])
	for i in range(0, len(a)-window+1):
		aL[len(aL)-1].append(a[i:i+window])
print aL
for window in range(1, len(b)+1):
	bL.append([])
	for i in range(0, len(b)-window+1):
		bL[len(bL)-1].append(b[i:i+window])
print bL
print "aL iterated backwards = "
for i in range(len(aL)-1, -1, -1):
	print aL[i]
print "bL iterated backwards = "
for i in range(len(bL)-1, -1, -1):
	print bL[i]

for i in range(len(aL)-1, -1, -1):
	for j, val in enumerate(aL[i]):
		print val, bL[i]
		if val in bL[i]:
			keepLooping = false
			break
			print 'match'

	
	

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


