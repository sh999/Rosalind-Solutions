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
	print "\nRunning mate.."
	print parent1, "mates with", parent2
	offsprings = createOffsprings(parent1, parent2)
	print 'Offsprings = ', offsprings
	countFrequencies(offsprings)
	print "\n..End mate()"
	return offsprings

def createOffsprings(p1, p2):
	# Create offsprings by combining alleles
	print "\nRunning createOffsprings().."
	offsprings = []
	for i in p1:
		for j in p2:
			offsprings.append([i,j])
	print "\n..End createOffsprings"
	return offsprings

def countFrequencies(offsprings):
	# Count offspring frequencies
	print "\nRunning countFrequencies()..."
	dominant = 0
	heterozygous = 0
	recessive = 0
	for i, alleles  in enumerate(offsprings):
		print "\tOffspring",i," = " , alleles,
		if alleles[0] == 'A' and alleles[1] == 'A':
			print "homozygous dominant"
			dominant += 1
		elif alleles[0] == 'a' and alleles[1] == 'a':
			print "homozygous recessive"
			recessive += 1
		elif (alleles[0] == 'A' and alleles[1] == 'a') or (alleles[0] == 'a' and alleles[1] == 'A'):
			print "heterozygous"
			heterozygous += 1
	print "Total:"
	print "\tHomozygous dominant = ",dominant
	print "\theterozygous= ",heterozygous
	print "\tHomozygous recessive = ",recessive
	print "\tOffsprings after mating func= ",offsprings
	print "\n...End countFrequencies"

def countHets(genotypes):
	print "\nRunning countHets()..."
	hetFreq = 0.0
	for i in genotypes:
		print i,
		if (i[0] == 'A' and i[1] == 'a') or (i[0] == 'a' and i[1] == 'A'):
			hetFreq += 1
	hetFreq = hetFreq/len(genotypes)
	print "\nhet freq = ",hetFreq
	print "total indivs = ",len(genotypes)
	print "\n...End countHets"

print "Start:"
parent1 = genotype("Aa")
parent2 = genotype("Aa")
print "parent 1 = ", parent1, " will mate with parent 2 = ", parent2
# for i in range(0, len(offsprings)):
	# offsprings[i] = genotype(offsprings[i])
offsprings = mate(parent1, parent2) # Return a list of offsprings
subOffsprings = []
print "initial length of offsprings = ",len(offsprings)
print "all offsprings = ",offsprings
for i in range(0, len(offsprings)):
	print "Iterating offspring[",i,"] = ",offsprings[i]
	subOffsprings = mate(offsprings[i], parent2) # Return a list of offsprings
	print "offsprings after iterating for",subOffsprings
	offsprings.extend(subOffsprings)
print "All offsprings combined = ",offsprings
countHets(offsprings)



