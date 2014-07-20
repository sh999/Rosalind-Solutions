#http://rosalind.info/problems/hamm/
#6/5/14
sourceFile = open("rosalind_hamm.txt", "r")
sequences = []
mutations = 0
for line in sourceFile:
	line = line.replace("\n","")
	sequences.extend([line])
for i in range(0, len(sequences[0])):
	if sequences[0][i] != sequences[1][i]:
		mutations += 1
print sequences
print mutations


