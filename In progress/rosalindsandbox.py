'''
2/16/15:  working on lia.py to deal with two genes/alleles
'''

def createGametes(individual):
	gametes = []
	gene1 = individual[0:2]
	gene2 = individual[2:4]
	for allele1 in gene1:
		for allele2 in gene2:
			gametes.append(allele1 + allele2)
	return gametes

def createOffsprings(p1, p2):
	offsprings = []
	# print "p1 = ", p1
	for i in p1:
		for j in p2:
			offsprings.append([i,j])
	return offsprings

def convertToGenotype(alleleList):
	genotype = alleleList[0][0] + alleleList[1][0] + alleleList[0][1] + alleleList[1][1]
	
	# print 'genotype = ', genotype
	if genotype[0].islower():
		genotype = genotype[1] + genotype[0] + genotype[2:4]
	if genotype[2].islower():
		genotype = genotype[0:2] + genotype[3] + genotype[2]
	return genotype

def countHets(genotypes): 
	a = 0
	for child in genotypes:
		
		if child[0].isupper() and child[1].islower() and child[2].isupper() and child[3].islower():
			a += 1
	return a
	

def main():
	parent1 = createGametes("AaBb")
	print "gametes = ", parent1
	offsprings = createOffsprings(parent1, parent1)
	# print "offsprings = ", offsprings
	offspringGenotypes = []
	for child in offsprings:
		# print 'child = ', child
		offspringGenotypes.append(convertToGenotype(child))
	print 'offspring genotypes = ', offspringGenotypes
	hetAmt = countHets(offspringGenotypes)
	print 'het amt = ', hetAmt
main()
