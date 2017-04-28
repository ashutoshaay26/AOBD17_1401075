import json
from pprint import pprint

with open('Senior Network Engineer.txt') as data_file:
	data = json.load(data_file)
	with open("aa.txt", 'a') as out:
		out.write('ID'+','+'Skills'+'\n')
		for i in range(len(data)):
			out.write(data[i]["CandidateID"] +','+data[i]["Skills"] +'\n')
			#pprint(data[i]["Skills"])