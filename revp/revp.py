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

Progress:
	Check for palindrome for one length
	1/30: work on palindromeLocations, figure out strategy on communicating location with substrings (list consisting of position+string?)
'''
from FASTA_extract import *

def processFile(): # Takes FASTA file and extracts sequence
	return seqList("sampletext.txt")[0]
	
def goThroughString(sequence): # Iterates through sequence and creates subsequences
	minLength = 4 # Min and Max length are palindrome lengths to be checked
	maxLength = 12
	substrings = []
	for j in range(minLength, maxLength+1):
		for i in range(0, len(sequence)-j+1):
			# print "appending ",sequence[i:i+j]
			substring = sequence[i:i+j]
			substringLocation = i+1
			substrings.append([substring, substringLocation, len(substring)]) 
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
	# print "revcomp.. = ",revComp
	
	palindromeLocations = []
	palindromeLength = []
	if revComp == string:
		return True
	return False

def palindromeLocations(): # Gives value of location, length of palindromes
	outputFile = open("output.txt", "w")
	substrings = goThroughString(processFile())
	print substrings
	for i in substrings:
		if checkIfPalindrome(i[0]):
			outputFile.write("%s %s\n"%(i[1],i[2])) # Formatting is compliant of puzzle
			print i[1],i[2]
	outputFile.close()


def test():
	# print "Substrings =",goThroughString(sequence)
	string = "CATATGS"
	checkIfPalindrome(string)
	print "Sequence =",string
	print "Is %s a palindrome? %s" %(string,checkIfPalindrome(string))

def main():
	'''
	substrings = goThroughString(processFile())
	for i in substrings:
		print(checkIfPalindrome(i))'''
	palindromeLocations()

	
main()
