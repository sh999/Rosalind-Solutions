#!/usr/local/bin/python2.7-32
'''
Solution for "Speeding Up Motif Finding"
http://rosalind.info/problems/kmp/
8/3/14
'''
import cProfile

def PK(_position, _DNA):
	# iterate through DNA sequence
	DNA = _DNA
	position = _position
	start = -1
	end = position 
	# print DNA[start:end]
	queries = []
	prefixes = []
	for i in range(end-1, start, -1):
		# print "i = ",i, ". end",end,". end-i = ",end-i
		if i > 0:
			# print DNA[i:end],"and", DNA[0:end-i]
			queries.extend([DNA[i:end]])
			prefixes.extend([DNA[0:end-i]])
	longest = 0
	current = 0
	for i in range(0,len(queries)):
		# print queries[i], prefixes[i]
		if queries[i] == prefixes[i]:
			current = len(queries[i])
			if current > longest:
				longest = current

			# print "equal"
			# print "length = ", current
	return longest
		# print longest
	# print queries, prefixes

	# create a list of query substrings at each position p(k) arrays
	# create reference prefix string at that position (only 1 ref)
	# compare each query substring to reference prefix
'''
a = open("sampletext.txt")
b = a.readlines()[1:]
b = str(b)
b = b.translate(None,"[]',\\n ")'''

def main():
	source = open("rosalind_sampletext.txt")
	DNA = source.readlines()[1:]
	DNA = str(DNA)
	DNA = DNA.translate(None,"[]',\\n ")
	fail_array = []
	for i in range(1, len(DNA)+1):
		fail_array.extend([PK(i, DNA)])
	fail_array = str(fail_array)
	fail_array = fail_array.translate(None,"[],")
	print fail_array
	output = open("rosalind_output.txt","w")
	output.write(fail_array)

main()
cProfile.run('main()')





	
	

		
	
	
	

	
	
