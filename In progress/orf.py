'''
orf.py
Open Reading Frames
http://rosalind.info/problems/orf/
Algorithm:
	Process FASTA file (put sequence into a string)
	Have codon table ready
	Iterate through each base position in sequence
		Look for every start and stop codon in sequence, note their positions
		Note which start/stop pairs are in frame with one another
		Build DNA sequences out of all the possible combinations of the start/stop codons that are in frame
	Reverse complement, do same process
'''
from FASTA_extract import *
print seqList("sampletext.txt")