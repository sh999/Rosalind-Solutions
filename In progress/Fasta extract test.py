def seqList():
	a = open("sampletext.txt")
	a = a.readlines()
	b = []
	for i in a:
		if i[0] == '>':
			b.append('')
		else:
			
			b[-1] = b[-1] + i.replace("\n","")
	print b
	return b
def titleList():
	a = open("sampletext.txt")
	a = a.readlines()
	b = []
	for i in a:
		if i[0] == '>':
			b.append(i.replace("\n",""))
	print b
seqList()
titleList()
