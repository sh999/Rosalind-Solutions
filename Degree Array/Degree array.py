def delete_newlines(myString):
	myString = myString.replace("\n", "")
	myString = myString.replace(" ", "")
	myString = list(myString)
	return myString


def process_textfile(myFile):
	heading = []
	vertex_edge_list = []
	for line_number, line in enumerate(myFile):
		if line_number == 0:
			heading = line
			heading = delete_newlines(heading)
		else:
			vertex_edge_list.append(line)
			#for i in range(0, len(vertex_edge_list)):
				#vertex_edge_list[i] = delete_newlines(vertex_edge_list[i])
	#vertex_edge_list[0] = delete_newlines(vertex_edge_list[0])
	print vertex_edge_list



myFile = open("sampletext.txt", "r")
process_textfile(myFile)






myFile.close()