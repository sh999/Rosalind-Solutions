prev = 0
current = 1
n = 24
if n == 0:
	print 0
elif n ==1:
	print 1
else:
	for i in range(0, n-1):
		next = prev + current
		prev = current
		current = next
		print next
