#!/usr/bin/env python3
import re
import csv

def normalize_space(s):
    return ' '.join(s.split())

absolute_path = open(r'output_files/ALU.map.rpt', 'r')
contents = absolute_path.read()

res = re.search('\;\s+Analysis & Synthesis Resource Usage(.*\s[0-9.]*)\;\s+Average fan-out\s+\;\s+[0-9.]*\s+\;$',
                    contents,flags = re.S | re.M).group(0)
my_list = res.split(";")

my_list[0:6] = ''

remove_space = [x.strip(' ') for x in my_list]
remove_space = [x.strip('\n') for x in my_list]
newlist = [ele for ele in my_list if ele.strip()]
special_char = "--"
out_list = [''.join(x for x in string if not x in special_char) for string in newlist]

replaced_list = [normalize_space(i) for i in out_list]
#print(replaced_list)

#partitioning list to number and text
row = []
column = []
for i in replaced_list:
    if(i.isdigit() or isinstance(i,float)):
       column.append(i)
    elif (i == "op[0]"):
        column.append(i)
    else:
       row.append(i) 
del row[4]
del row[9]

#print(row)
#print(column)

filename = "new.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(row)
    csvwriter.writerow(column)
absolute_path.close()
