#!/usr/local/bin/python2.7-32
'''
'''
myFile = open("monoisotopic mass table.txt")
data = []
sequence = list("EDVRHPYRLDRRRSGPCHCNHDCPRCIFRHLYMCFETFQFQPKYQEVDYDQEGHRISWCQHRRVTKVYHCLEYWAMRCQKRVIRSFTMQYLVQLTPGKGLIYYQGNPCIRIIRKMFHWNKQRAQHYHHRYYATCPYELVDHIFYQFSMCQILNCSVTYKDFDSLQAWAVTISDLLDMKQAMVAEIEMTILRVDNPQWTWECSHVEAWLNNQKIWYKVTQNGCDRYGTCASFCIWRSVKPSTMPALAWRIVVLDVYTAEIDQHIIKSNILLMHYTLPIPVEDQKLNFWHMTNVMHPFSIEEYFNLCPCILQPERRTIVSTTMWPQIRDSCPQTDGCQKMESFTQQAGGVPFPTDRRPWSQHGEQYRQYAPMAADTLQKDCRNNKARANNNGMILHPPHCTILGGFGKRCEWMCQHTFQHYGQEHLFRYFFIMMYDPYWCMQCPTMPWPFNRAMPPYMKTQNGGYHHDTSINKASPCSHYFHTMNTKESESIVNNLAVCAINTIYKIGVTTQNYLVERWLCCGVANITVRCRSHRWYIPRKYEVAIVWSCQPQGSLLHQDHCREHDDQSFHDLNWPYEGYHPQAGTYAIKSPMNVSFKGIYLEEHDLNNEHMYSNPCQSEICLALNCQHTGQVDYRGDIAIRAIIFHCHWSPEFAYDKTHLLSAPCSWPDIDLWCAQCGYAGNSLWVNLSMKTMRRRFMYKLHPHFIRCVLNYQKARSSDWPTYETNVWNLLPKHALHPWYIKMSPFSSMPWNVQMDPLVGWVAQWKGTHHPCTYMRESGCTFQRKDMVMLRQRYNCNSHRKHWVLSFVRKEDSMSDHATTSSCSLPDNSSY")
for lines in myFile:	
	data.extend([lines.split()])
mass = 0
for residue in sequence:
	for j in data:
		if j[0] == residue:
			print float(j[1]), "match"
			mass = mass + float(j[1])
print data
print sequence
print mass




	
	

		
	
	
	

	
	
