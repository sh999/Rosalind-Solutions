'''
mrna.py
Inferring mRNA from protein
http://rosalind.info/problems/mrna/
Notes:
	If a mod n = b mod n, a and b are congruent modulo 
	This is written as a === b (mod n)
	Properties of being congruent:
		if a === b (mod n) 
		it follows that
			a + c === b + d (mod n) 
			a X c === b X d (mod n) 
			example:
			given a = 29, b = 73, c = 10, d = 32, n = 11
			a + c = 39
			b + d = 105
			a + c (mod n) = 39 mod 11 = 6
			b + d (mod n) = 105 mod 11 = 6
		Pitfall:  Congruent notation is similar to regular modular arithmetic
		a === b (mod n) does NOT mean a === b mod n if b mod n is an expression
Naive algorithm:
	Have a table with key as AA residue and value as # of possible codons
	Given a list of protein string, look up above table and make a list of # possible codons
	Multiply each element one after another
Better algorithm?:
	Use modular congruency property
'''

