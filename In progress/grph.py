from Fasta_extract_test import *
seqId = titleList()
DNAseq = seqList()
k = 3
adj = []
for i in range(0,len(DNAseq)):
	for j in range(0, len(DNAseq)):
		if j != i:
			if DNAseq[i][-3:] == DNAseq[j][0:k]: #Compare last character of item1 with first character of item2
				adj.append([seqId[i],seqId[j]])
output = adj
for i in range(0, len(output)):
	output[i] = " ".join(output[i])
	print output[i]

