'''
http://rosalind.info/problems/lia/
'''
import string
def testMate(parent1, parent2, generations):
	tempOffsprings = []
	if generations >= 0:
		for i in parent1:
			for j in parent2:
				tempOffsprings.append([i,j])
	else:
		return 
def testRecursion(a,c):
	if c >= 0:
		b = [a*2,a*3]
		print b
		for i in b:
			testRecursion(i,c-1)
	else:
		return
def testRecursion2(l, c):
	if c >= 0:
		l.append('1')
		print "appending ...",l

		testRecursion2(l,c-1)
	else:
		print "last l = ",l
		return l
	# return 7

def f(a):
	if a > 10:
		return 1
	else:
		return 0


def mate(parent1, parent2):
	offsprings = []
	# Create offsprings
	for i in parent1:
		for j in parent2:
			offsprings.append([i,j])
	return offsprings

def countHets(genotypes):
	hetFreq = 0.0
	for i in genotypes:
		if (i[0] == 'A' and i[1] == 'a') or (i[0] == 'a' and i[1] == 'A'):
			hetFreq += 1
	hetFreq = hetFreq/len(genotypes)
	return hetFreq
parent1 = ['A','a']
parent2 = ['A','a']
offsprings = mate(parent1, parent2) # Return a list of offsprings
subOffsprings = []
for i in range(0, len(offsprings)):
	subOffsprings = mate(offsprings[i], parent2) # Return a list of offsprings
	offsprings.extend(subOffsprings)
print countHets(offsprings)

# print(testRecursion2([],4))
print(testRecursion2([],2))
print (f(-1))



