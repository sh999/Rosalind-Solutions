def mate(l, a, counter):
	double = a * 2
	triple = a * 3
	children = [double, triple]
	l.append(children)
	# print children
	if(counter > 0):
		for i in children:
			mate(l, i, counter-1)
	return l

# print(mate([], 4, 2))
print mate([], 4, 2)