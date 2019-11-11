import sys
import csv
elWords = []
elWordDic = {}
with open('els.csv',mode='r') as elfile:
	reader = csv.reader(elfile)
	els = {rows[1].lower().strip():int(rows[0]) for rows in reader}

words = open(sys.argv[1]).readlines()

def elsThatFit(word,usedEls):
	if word=="":
		elWords.append(usedEls)
	else:
		for e in els.keys():
			if e==word[0:len(e)] and e not in usedEls:
				newUsedEls=usedEls.copy()
				newUsedEls.append(e)
				elsThatFit(word[len(e):],newUsedEls)

for w in words:
	elsThatFit(w.lower().strip(),[])

for i in elWords:
	score=0
	for e in i:
		score+=els[e]
	elWordDic["".join(s.capitalize() for s in i)] = score*len(i)

from operator import itemgetter
sortedWords = sorted(elWordDic.items(), key=itemgetter(1))
for s in sortedWords[len(sortedWords)-20:]:
	print (s)

with open(sys.argv[2],'w') as f:
        w=csv.writer(f)
        for key,value in sorted(elWordDic.items(),key=lambda tup: tup[1],reverse=True):
                w.writerow([key,value])

print(len(sortedWords))

