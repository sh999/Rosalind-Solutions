'''
FASTAextract.py
8/29/14
'''
class sequences:
	def __init__(self, sourceFile):
		self.parseFile(sourceFile)
	def parseFile(self, sourceFile):
		self.file = open(sourceFile)
		rawList = self.file.readlines()
		titleList = []
		seqList = []

		# Replace unecessay characters
		for i in range(0,len(rawList),2):
			rawList[i] = rawList[i].replace("\n","")
			rawList[i] = rawList[i].replace(">","")
			titleList.extend([rawList[i]])
			rawList[i+1] = rawList[i+1].replace("\n","")
			seqList.extend([rawList[i+1]])
			
		print titleList
		print seqList

class element:
	def __init__(self, title, seq):
		self.title = title
		



