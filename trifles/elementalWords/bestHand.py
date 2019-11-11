import sys
import csv
hand={}
with open(sys.argv[1],mode='r') as wordFile:
    reader = csv.reader(wordFile)
    wordDic={row[0]:int(row[1]) for row in reader}


