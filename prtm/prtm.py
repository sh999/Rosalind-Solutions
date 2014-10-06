#!/usr/local/bin/python2.7-32
'''
http://rosalind.info/problems/prtm/
rosalind
Calculating Protein Mass
'''
myFile = open("monoisotopic mass table.txt")
data = []
sequence = open("rosalind_prtm.txt")
sequence = sequence.readlines()
sequence = list(sequence[0])
for lines in myFile:	
	data.extend([lines.split()])
mass = 0
for residue in sequence:
	for j in data:
		if j[0] == residue:			
			mass = mass + float(j[1])
print sequence
print mass




	
	

		
	
	
	

	
	
