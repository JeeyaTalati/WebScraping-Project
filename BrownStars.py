from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
import time 

Starting_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(Starting_url)
soup=BeautifulSoup(page.text,"html.parser")
starTable=soup.find("table",attrs={"class":"wikitable sortable jquery-tablesorter"})
tempList=[]
print(starTable)
tableRows=starTable[6].find_all("tr")
for tr in tableRows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    tempList.append(row)
starNames=[]
starDistance=[]
starRadius=[]
starMass=[]
for i in range(1,len(tempList)):
    starNames.append(tempList[i][0])
    starDistance.append(tempList[i][5])
    starRadius.append(tempList[i][8])
    starMass.append(tempList[i][7])
df=pd.DataFrame(list(zip(starNames,starDistance,starRadius,starMass)),columns=['name','distance','radius','mass'])
df.to_csv("BrownStarsTable.csv")
