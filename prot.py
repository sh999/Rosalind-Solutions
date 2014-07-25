# Translate DNA program
# 11/11/13
# Take a string of DNA, and return with protein sequence

# For each amino acid, define what the codons are
Ala = ["Ala", "A", "GCT", "GCC", "GCA", "GCG"]
Arg = ["Arg", "R", "CGT", "CGC", "CGA", "CGG", "AGA", "AGG"]
Asn = ["Asn", "N", "AAT", "AAC"]
Asp = ["Asp", "D", "GAT", "GAC"]
Cys = ["Cys", "C", "TGT", "TGC"]
Gln = ["Gln", "Q", "CAA", "CAG"]
Glu = ["Glu", "E", "GAA", "GAG"]
Gly = ["Gly", "G", "GGT", "GGC", "GGA", "GGG"]
His = ["His", "H", "CAT", "CAC"]
Ile = ["Ile", "I", "ATT", "ATC", "ATA"]
Leu = ["Leu", "L", "TTA", "TTG", "CTT", "CTC", "CTA", "CTG"]
Lys = ["Lys", "K", "AAA", "AAG"]
Met = ["Met", "M", "ATG"]
Phe = ["Phe", "F", "TTT", "TTC"]
Pro = ["Pro", "P", "CCT", "CCC", "CCA", "CCG"]
Ser = ["Ser", "S", "TCT", "TCC", "TCA", "TCG", "AGT", "AGC"]
Thr = ["Thr", "T", "ACT", "ACC", "ACA", "ACG"]
Trp = ["Trp", "W", "TGG"]
Tyr = ["Tyr", "Y", "TAT", "TAC"]
Val = ["Val", "V", "GTT", "GTC", "GTA", "GTG"]
Stop = ["Stop", "*", "TAA", "TGA", "TAG"]

#Let user enter the sequence of DNA to be translated
AminoAcids = [Ala, Arg, Asn, Asp, Cys, Gln, Glu, Gly, His, Ile, Leu, Lys, 
			   Met, Phe, Pro, Ser, Thr, Trp, Tyr, Val, Stop]
sourcefile = open("rosalind_prot.txt")
RNASequence = sourcefile.read()
DNASequence = RNASequence.replace('U','T')
Codons = []
AminoAcidSequence = []
'''
#Iterate over every 3 letters of the DNA sequence.
#In reality, you iterate i++ but do an arithmetic function to simulate this
#e.g.
#Sequence:  c  a  g  c  a  g  c  a  g  
Index:      0  1  2  3  4  5  6  7  8  
size = 12
elements = 0 to 11
iterate range = 0 to 9 or 0 to end range - 3
for i in range(0, 3) 
...i = 0
...take letters from index 0,1,2 or i,i+1,i+2
...i = 1
...take letters from index 3,4,5 or i*3, and the next, and the next
...i = 2
...take letters from index 6,7,8 or i*3, and the next, and the next
'''
#Create codons sequence, where total DNA sequence is grouped by 3
for i in range(0,len(DNASequence)/3):
	Codons.append(DNASequence[i*3]+DNASequence[i*3+1]+DNASequence[i*3+2])
'''Iterate over every amino acid and see if it equals DNA sequence'''
#iterate over each amino acid residue
#i = Ala, Arg, Asn...
match = False
for k in Codons:
	match = False
	if match == False:
		for i in AminoAcids:
		#Within each AA, iterate over each 3 letter code of that residue
		#j = GCT, GCC....
			if match == False:
				for j in i:
				#For each code, iterate over Codon to see if they match
				#k = codon1, codon2...
					if j == k or j == k.upper():
						AminoAcidSequence.append(i[1])
						match = True

print Codons
print "".join(AminoAcidSequence)







    #print AA[i]

        #if AA[i] == "GCA": print "lo"
#myList = [k for k, v in dict.iteritems() if v > 1]
#print dict.items()
#print dict