'''
mprt.py
Finding a Protein Motif 
http://rosalind.info/problems/mprt/
Algorithm:
	Process file, put sequence id into list
	For each sequence id:
		Get/scrape sequence from Uniprot, put sequence in list
	Iterate through sequence; at each sequence check if motif present (terminate sequence iteration if at any point there's mismatch)
	If motif match is found, note the index
'''
