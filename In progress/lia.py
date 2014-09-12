'''
http://rosalind.info/problems/lia/

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
	print "Offsprings after mating func= ",offsprings
	print "\n\n"
	return offsprings

parent1 = genotype("Aa")
print "parent 1 = ", parent1 
parent2 = genotype("Aa")
# for i in range(0, len(offsprings)):
	# offsprings[i] = genotype(offsprings[i])
offsprings = mate(parent1, parent2) # Return a list of offsprings
print "initial length of offpsrings = ",len(offsprings)
for i in range(0, len(offsprings)):
	print "Iterating offspring[i] = ",offsprings[i]
	
	offsprings = mate(offsprings[i], parent2) # Return a list of offsprings
	print "offpsrings after iterating for",offsprings
print offsprings




