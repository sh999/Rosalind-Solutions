#!/usr/local/bin/python2.7-32
'''
http://rosalind.info/problems/cons/
Rosalind.info problem
Find consensus sequence and print out matrix of base content from each site
'''
f = open("rosalind_cons.txt")
sequenceCount = -1
DNAlist = []
for line in f:
	if line[0] == '>':
		sequenceCount = sequenceCount + 1
		DNAlist.append("")
	else:
		DNAlist[sequenceCount] = DNAlist[sequenceCount] + line
for i in range(len(DNAlist)):
	DNAlist[i] = DNAlist[i].replace("\r\n", "")
	DNAlist[i] = DNAlist[i].replace("\n", "")
a = [0]*len(DNAlist[0])
c = [0]*len(DNAlist[0])
t = [0]*len(DNAlist[0])
g = [0]*len(DNAlist[0])
for i in range(0, len(DNAlist[0])):
	for j in range(0, len(DNAlist)):
		if DNAlist[j][i] == 'A':
			a[i] += 1
		elif DNAlist[j][i] == 'C':
			c[i] += 1
		elif DNAlist[j][i] == 'T':
			t[i] += 1
		elif DNAlist[j][i] == 'G':
			g[i] += 1

consensus = [0]*len(DNAlist[0])
highest = [0]*len(DNAlist[0])
for i in range(0, len(consensus)):
	highest[i] = a[i]
	consensus[i] = 'A'
	if c[i] > highest[i]:
		highest[i] = c[i]
		consensus[i] = 'C'
	if t[i] > highest[i]:
		highest[i] = t[i]
		consensus[i] = 'T'
	if g[i] > highest[i]:
		highest[i] = g[i]
		consensus[i] = 'G'	
print "".join(consensus)
print 'A:', " ".join(map(str,a))
print 'C:', " ".join(map(str,c))
print 'G:', " ".join(map(str,g))
print 'T:', " ".join(map(str,t))






	






	
	

		
	
	
	

	
	
