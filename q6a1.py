from operator import itemgetter
from collections import Counter
rows = []
abc = []
countA = []
countB = {}
with open('q6a1metadata.txt') as fp:	
	for line in fp:
		items=[x.strip() for x in line.split(',')]
		abc.append(items)
sorted_a = sorted(abc, key=lambda tup: tup[4])
rows = sorted(sorted_a, key=lambda tup: tup[0])
first_elements = [x[0] for x in rows]
second_elements = [x[1] for x in rows]
third_elements = [x[2] for x in rows]
fourth_elements = [x[3] for x in rows]
fifth_elements = [x[4] for x in rows]

countA = Counter(elem[0] for elem in rows)
print countA
print dict((k, dict(v)) for k, v in countA.iteritems())
#print countB
c =0
for key in countA:
	print key
	i = countA[key]
	for x in range(0,i):
		#print(key + "(" +second_elements[c] )
		c += 1
		
	
"""
print (first_elements + "("+ )
print("########################")
print second_elements"""
""""
print("########################")
print third_elements
print("########################")
print fourth_elements
print("########################")
print fifth_elements"""