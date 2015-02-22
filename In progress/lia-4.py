'''
2/16/15:  working on lia.py to deal with two genes/alleles
I can do two generations; program yet unable to do x number of generations
I must understand the mathematics before going ahead
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

def genotypeFormat(offsprings):
	offspringGenotypes = []

	for child in offsprings: # converts ['AB', 'AB'] to 'AABB'
		genotype = child[0][0] + child[1][0] + child[0][1] + child[1][1]
		if genotype[0].islower():
			genotype = genotype[1] + genotype[0] + genotype[2:4]
		if genotype[2].islower():
			genotype = genotype[0:2] + genotype[3] + genotype[2]
		offspringGenotypes.append(genotype)
		# print "genotype = ", genotype
		# print "list = ", offspringGenotypes
	return offspringGenotypes

def countHets(genotypes): 
	a = 0
	for child in genotypes:
		if child[0].isupper() and child[1].islower() and child[2].isupper() and child[3].islower():
			a += 1
	return a
	
def main():
	parent1 = createGametes("AaBb")
	hetMate = "AaBb"
	hetMateGametes = createGametes(hetMate)
	# print "gametes = ", parent1
	offsprings = createOffsprings(parent1, hetMateGametes)
	# print "offsprings = ", offsprings
	offspringGenotypes = genotypeFormat(offsprings)
	# print 'Offspring genotypes after = ', offspringGenotypes
	hetAmt = countHets(offspringGenotypes)
	# print 'het amt after 1st generation = ', hetAmt
	hetAmtList = []
	for i in offspringGenotypes:
		tempOffspringList = genotypeFormat(createOffsprings(createGametes(i), hetMateGametes))
		print i, "x", hetMate, " = ", tempOffspringList
		hetAmtList.append(countHets(tempOffspringList))
	print hetAmt
	print hetAmtList

main()
