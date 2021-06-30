import csv
data1 = []
data2 = []
with open("data 129.csv",'r')as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1.append(row)
with open("data_129.csv",'r')as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)
header1 = data1[0]
planetdata1 = data1[1:]
header2 = data2[0]
planetdata2 = data2[1:]
headers = header1+header2
planet_data = []
for index, data_row in enumerate(planetdata1):
    planet_data.append(planetdata1[index]+planetdata2[index])
with open("final.csv",'a+')as f :
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(planet_data)
        