# Translate DNA program
# Based on prot.py
# Take a string of DNA, and return with protein sequence
# For each amino acid, define what the codons are

def translate(DNASequence):
	Codons = []
	AminoAcidSequence = []
	#Create codons sequence, where total DNA sequence is grouped by 3
	for i in range(0,len(DNASequence)/3):
		Codons.append(DNASequence[i*3]+DNASequence[i*3+1]+DNASequence[i*3+2])
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
	# print Codons
	translatedSeq = "".join(AminoAcidSequence)
	return translatedSeq

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
Stop = ["Stop", "", "TAA", "TGA", "TAG"]
#Let user enter the sequence of DNA to be translated
AminoAcids = [Ala, Arg, Asn, Asp, Cys, Gln, Glu, Gly, His, Ile, Leu, Lys, 
			   Met, Phe, Pro, Ser, Thr, Trp, Tyr, Val, Stop]
# DNASequence = RNASequence.replace('U','T')




