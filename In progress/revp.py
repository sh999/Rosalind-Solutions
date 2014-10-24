'''
revp.py
Locating restriction sites
http://rosalind.info/problems/revp/
Pseudocode:
	Process fasta into one string
	Iterate through each position of string
		In each position, create substrings of length 4 to 12 (given restriction) - position (i.e. from position to end)
		Check if is each is a palindrome
Strategy:
	Can work on individual modules instead of trying to tackle all problem at once

Progres:
	Check for palindrome for one length

'''
def processFile(): # Takes FASTA file and extracts sequence
	return "TCAATGCATGCGGGTCTATATGCAT"
	
def goThroughString(sequence): # Iterates through sequence and creates subsequences
	minLength = 4 # Min and Max length are palindrome lengths to be checked
	maxLength = 12
	substrings = []
	substringLength = 12
	for i in range(0, len(sequence)-substringLength):
		substrings.append(sequence[i:i+substringLength])
	return substrings

def checkIfPalindrome(string):
	reverse = string[::-1] # Extended slice of form [begin:end:-1]; reverses string
	revComp = ""
	for i in range(0,len(reverse)):
		if reverse[i] == 'A':
			revComp += 'T'
		elif reverse[i] == 'C':
			revComp += 'G'
		elif reverse[i] == 'G':
			revComp += 'C'
		elif reverse[i] == 'T':
			revComp += 'A'
	print "revcomp.. =",revComp
	if revComp == string:
		return True
	return False

def main():
	# print "Substrings =",goThroughString(sequence)
	string = "CATATGS"
	checkIfPalindrome(string)
	print "Sequence =",string
	print "Is %s a palindrome? %s" %(string,checkIfPalindrome(string))
main()
