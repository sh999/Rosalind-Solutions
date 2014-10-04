'''
Goal: Test recursion to simulate mating between two organisms
in rosalind/lia, var1 would be parent 1 (whatever individual) 
and var2 would be heterozygote parent 2 (background individual)
Program should accept >=1 generations of mating.  In each mating cycle,

Input: 
var1 = 1
var 2 = 2
In one round of mating/generation, will generate offspring list that 
contains four individuals: 1x2-1, 1x2-2, 1x2-3, 1x2-4 (Indicates parentpair-offspring id)
In the second round of mating, each of the above offsprings will mate with individual '2'
resulting in e.g. for offspring of 1x2-1:  1x2-1x2-1,1x2-1x2-2,1x2-1-3,1x2-1-4 and so on.
After 1 round, 4 offpsrings.
After second round, 8 offpsrings.
'''

def mateOneGeneration(parent1,parent2):
	combined = parent1 + 'x' + parent2 + '-'
	offsprings = []
	for i in range(0,4):
		offsprings.append(combined+str(i+1))
	return offsprings

def mateXGenerations(parent1,parent2,offsprings,generations):
	if(generations > 0):
		# combined = str(parent1) + 'x' + str(parent2) + '-'
		combined = '3'
		# offsprings.append('1')
		print "offsprings = ",offsprings
		for i in range(0,4):
			# offsprings.append([combined+str(i+1)])
			offsprings.append(i)
		# for j in offsprings:
		for j in offsprings:
			print "j = ",j
			mateXGenerations(j,parent2,offsprings,generations-1)
		# mateXGenerations(parent1,parent2,offsprings,generations-1)

			
	# print offsprings
	return offsprings 

def main():
	parent1 = '1'
	parent2 = '2'
	# print "Offspring from 1 generation = ", mateOneGeneration(parent1,parent2)
	# print "Offspring from 2 generations = ", mateXGenerations(parent1,parent2,[],1)
	print "total offspring = ",mateXGenerations(parent1, parent2, [], 2)
	# print 'lol'
main()
