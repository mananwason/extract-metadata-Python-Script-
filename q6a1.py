from operator import itemgetter
from collections import Counter
rows = []
abc = []
countA = []
countB = {}
result = []
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
countB = sorted(countA.items(), key=itemgetter(0))
y=c=j=z=m=n=0
fin = [int(i[1]) for i in countB]
name = [(x[0]) for x in countB]
total = sum(fin)
print ""
print ("REQUIRED RELATIONS : ")
print ""
for key in countB:
	
	i = fin[j]	
	n+= fin[j]	
	result = [a + " " + b for a, b in zip(third_elements, second_elements)]
	print(name[z]),
	print( "(" ),
	print ', '.join(result[m:n]),
	print(")")
	print ""
	m=n
	j+=1
	z+=1
c += 1
