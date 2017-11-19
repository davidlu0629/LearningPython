import numpy as np
import pandas as pd 
import csv 
import math

#read file
##file address
query_table="/home/ryuu/ir/hw1/query_list.txt"
##read file from row 1
with open(query_table, 'r') as doc:
	reader= csv.reader(doc)
	qlist= [[str(s) for s in row] for i, row in enumerate(reader) if i >=0]
  

#open new file and write
##open
file= open("/home/ryuu/ir/hw1/"+"submission.txt",'a')
##write
file.write("Query,RetrievedDocuments\n")
