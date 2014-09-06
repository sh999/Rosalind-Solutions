'''
http://rosalind.info/problems/lia/
9/2/14- Start
Do single mating scenario.  Print frequency of children
9/4 (Done)- Check case to count homozygous/heterozygous/etc 
9/5 Work on recursion function 
'''
import string
def genotype(genString): # Returns a list form of a parent's genotype
    genList = []
    for allele in genString:
    	genList.extend(allele)
    return genList
def mate(parent1, parent2):
	print parent1, "mates with", parent2
	offsprings = []
	# Create offsprings
	for i in parent1:
		for j in parent2:
			offsprings.append([i,j])
	print 'Offsprings = ', offsprings
	# Count offspring frequencies
	dominant = 0
	heterozygous = 0
	recessive = 0
	for i, alleles  in enumerate(offsprings):
		print "Offspring",i," = " , alleles
		if alleles[0] == 'A' and alleles[1] == 'A':
			print "homozygous dominant"
			dominant += 1
		elif alleles[0] == 'a' and alleles[1] == 'a':
			print "homozygous recessive"
			recessive += 1
		elif (alleles[0] == 'A' and alleles[1] == 'a') or (alleles[0] == 'a' and alleles[1] == 'A'):
			print "heterozygous"
			heterozygous += 1
	print "Homozygous dominant = ",dominant
	print "heterozygous= ",heterozygous
	print "Homozygous recessive = ",recessive
parent1 = genotype("Aa")
parent2 = genotype("Aa")
mate(parent1, parent2)




