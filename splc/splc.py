'''
splc.py
RNA splicing
http://rosalind.info/problems/splc/
Pseudocode:
	Process input fasta file:  Store first string as gene.  Store subsequent as introns
	Iterate through each intron
		Find where intron is in gene string.  Splice the intron out of the gene
	Translate gene string
'''
from Translate import *
def seqList(file):
	a = open(file)
	a = a.readlines()
	b = []
	for i in a:
		if i[0] == '>':
			b.append('')
		else:
			b[-1] = b[-1] + i.replace("\n","")
	return b
def titleList(file):
	a = open(file)
	a = a.readlines()
	b = []
	for i in a:
		if i[0] == '>':
			b.append(i.replace("\n","").replace(">",""))
	return b

def processFile(file):
	sequences = seqList(file)
	return sequences

def spliceOutIntrons(gene, introns):
	for i in introns:
		gene = gene.replace(i, '')
	return gene
	
def main():
	sequences = processFile("rosalind_splc.txt")
	gene = sequences[0]
	introns = sequences[1:]
	splicedGene = spliceOutIntrons(gene, introns)
	print translate(splicedGene)
main()



