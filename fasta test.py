'''
I'm m aking FASTAextract, which is a module that can take a text
file of FASTA sequences and parses them into individual sequences
with id numbers.  This program will test that module
'''
# from FASTAextract import sequences
# a = sequences("sampletext.txt")


a = sequences('')
print a.length() # 5
print a[1].title # >Rosalind_2391
print a[1].seq # AAATTTT