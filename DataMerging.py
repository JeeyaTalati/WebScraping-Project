import csv 
import pandas
rows1=[]
rows2=[]
with open("StarsTable.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        rows1.append(row)
with open("data2.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        rows2.append(row)
headers=rows1[0]
del headers[0]
headers.append("gravity")

data1=rows1[1:]
data2=rows2[1:]

temp1=rows1[1:]
for stars in temp1:
    try:
        stars[2]=float(stars[2])
        stars[3]=float(stars[3])
        stars[4]=float(stars[4])
        del stars[0]
    except:
        data1.remove(stars)

temp2=rows2[1:]
for stars in temp2:
    try:
        stars[2]=float(stars[2])
        stars[3]=float(stars[3])*0.000954588
        stars[4]=float(stars[4])*0.102763
        del stars[0]
    except:
        data2.remove(stars)

data=data1+data2
for stars in data:
    mass=stars[2]*1.989e+30
    radius=stars[3]*6.957e+8
    g=(6.674e-11*mass)/(radius**2)
    stars.append(g)

with open('FinalStarsData.csv','a+') as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)



