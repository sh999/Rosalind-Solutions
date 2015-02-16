'''
Given a multiline fasta sequence, seqList() will return 
a list of all the sequences in the same order.  titleList()
returns the sequence ID's in the same order
'''

def seqList(file):
	a = open(file)
	a = a.readlines()
	b = []
	for i in a:
		if i[0] == '>':
			b.append('')
		else:
			b[-1] = b[-1] + i.replace("\n","")
	return b
def titleList(file):
	a = open(file)
	a = a.readlines()
	b = []
	for i in a:
		if i[0] == '>':
			b.append(i.replace("\n","").replace(">",""))
	return b

def testRun():
	file = "sampletext.txt"
	print seqList(file)
	print titleList(file)
	


