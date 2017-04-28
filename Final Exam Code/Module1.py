import re
from collections import Counter
import fileinput

for line in fileinput.input("aa.txt", inplace=True):
	#remove digits
	result = ''.join(i for i in line if not i.isdigit())
	#remove dollar signs
	result = result.replace("$","")
	result = result.replace("+","")
	result = result.replace("(","")
	result = result.replace(")","")
	#some other regex, removes all y's
	#result = re.sub("[Yy]+", "", result)
	print (result)


with open('aa.txt') as f:
 	passage = f.read()
print(passage)
words = re.findall(r'\w+', passage)
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)
for i in word_counts:
 	print(i)