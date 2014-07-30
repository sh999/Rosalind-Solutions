#!usr/local/bin/python2.7-5
import math

def calcProb(seq, gc):
	pg = gc/2
	pc = gc/2
	pa = (1-gc)/2
	pt = (1-gc)/2
	g = 0
	c = 0
	a = 0
	t = 0
	for i in seq:
		print i
		if i == 'A':
			a += 1
		elif i == 'C':
			c += 1
		elif i == 'T':
			t += 1
		elif i == 'G':
			g += 1
	print a, c, t, g
	prob = pa**a * pc**c * pg**g * pt**t
	return math.log(prob, 10)

f = open("sampletext.txt")
fileLines = f.readlines()
seq = ''
gcArray = ''
#Separate input file into DNA sequence and list of numbers
for i in range(len(fileLines)):
	if fileLines[i][0].isalpha():
		#Takes care of multiline sequences
		fileLines[i] = fileLines[i].replace("\n","")
		seq = seq + fileLines[i]
	elif fileLines[i][0].isdigit():
		gcArray = gcArray + fileLines[i]
#Convert gcArray from string to list of floats
gcArray = gcArray.split()
gcArray = [float(x) for x in gcArray]
#probArray corresponds to gc content
probArray = [0]*len(gcArray)

'''
a = 'ACGATACAA'
gc = 0.287	
g = gc/2
c = gc/2
a = (1-gc)/2
t = (1-gc)/2
prob = a*c*g*a*t*a*c*a*a'''

for i in range(len(gcArray)):
	probArray[i] = calcProb(seq, gcArray[i])
	probArray[i] = round(probArray[i], 3)


# Display correctly
for i in probArray:
	print i,





	

