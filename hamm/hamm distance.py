source_file = open("sampletext.txt", "r")
line_list = []
for lines in source_file:
	line_list.extend([lines])
seq1 = line_list[0]
seq2 = line_list[1]
for i in range(len(seq1)):
	print seq1[i]
	seq1[i] = seq1[i].replace("A","X")
print seq1
print seq2

source_file.close()