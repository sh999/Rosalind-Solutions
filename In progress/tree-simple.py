'''
tree.simple
given two edge pairs, create dictionary of group id
'''

a = [[1, 5],[5, 3]]
d = {}
for i in range(len(a)): 
	if a[i][0] not in d or a[i][1] not in d:
		
		print 'lol'
	'''	
	for j in range(len(a[i])):
		print "\n"
		print "Iterating",a[i][j]
		if a[i][j] not in d: # if node doesn't belong in a group yet
			d[a[i][j]] = a[i][j] # assign node to a new group labeled its own value
			print "creating new group id",a[i][j]
		else:
			print "id already created"'''

print "d =",d


