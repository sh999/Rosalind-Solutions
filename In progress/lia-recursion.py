'''
Input: a list containing one number
Algorithm will generate two makeChildren
On the left = double of parent
Right = Triple of parent
A list will hold 
'''
class Master:
	def __init__(self, a, limit):
		self.topElement = a
		self.allElements = [self.topElement]
		self.limit = limit

	def makeChildren(self, parent, counter):
		if counter < self.limit:
			print "Parent = ",parent
			leftChild = 2 * parent
			rightChild = 3 * parent
			print "Left child = ",leftChild
			print "Right child = ",rightChild
			
			self.allElements.extend([leftChild])
			self.allElements.extend([rightChild])
			self.makeChildren(leftChild, counter+1)
			self.makeChildren(rightChild, counter+1)

a = Master(1, 3)
a.makeChildren(1, 0)
print a.allElements

