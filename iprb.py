#!usr/local/bin/python2.7-5
import copy
def dictFunc(dictio, mod):
	x = dict(dictio)
	total = sum(a.values())
	prob1 = x[mod[0]]/total
	x[mod[0]] -= 1
	total -= 1
	prob2 = x[mod[1]]/total
	totalProb = prob1*prob2
	print totalProb
	return totalProb

a = {'dom':20.0, 'het':23.0, 'rec':28.0}
b = ('dom', 'dom')
c = ('dom', 'het')
d = ('dom', 'rec')
e = ('het', 'het')
f = ('het', 'rec')
total = dictFunc(a, b) + dictFunc(a, c)*2 + dictFunc(a, d)*2 + dictFunc(a, e)*0.75 + dictFunc(a, f)*0.5*2
print "total = ", total

