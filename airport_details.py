import operator
import sys

file = open(r"C:\Users\Mani Kandan\Downloads\airlines.csv",'r')
data = file.readline()
results = dict()
while(True):
    line = file.readline()
    if not line:
        break
    values = line.split(',')
    airport_name = values[1]+values[2]
    if airport_name not in results:
        results[airport_name]=1
    else:
        results[airport_name]+=1

airport_details = dict(sorted(results.items(), key=operator.itemgetter(0)))
 
max_value =0
airport_name_max =""
min_value = sys.maxsize
airport_name_min=""

for key,value in airport_details.items():
    if(value>max_value):
        max_value = value
        airport_name_max = key
    if(value<min_value):
        min_value = value
        airport_name_min = key
print("Output 1")
print(airport_details)
print()
print("Output 2")
print(airport_name_max, max_value)
print()
print("Output 3")
print(airport_name_min, min_value)
