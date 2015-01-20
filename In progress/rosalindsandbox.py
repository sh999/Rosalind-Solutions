
def splice():

	a = 'ahaxxxsdf'
	b = 'xxx'
	for i in range(0, len(a)-len(b)+1):
		print a[i:i+3]
		if b == a[i:i+3]:
			print 'match'
		else:
			print 'no match'

def replaceChars():
	a = "asdfadfxxxasasdf"
	print a.replace("xxx","ooo")

def main():
	replaceChars()

main()
