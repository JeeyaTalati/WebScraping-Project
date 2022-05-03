from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
import time
Starting_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page=requests.get(Starting_url)
soup=BeautifulSoup(page.text,"html.parser")
starTable=soup.find("table")
tempList=[]
tableRows=starTable.find_all("tr")
for tr in tableRows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    tempList.append(row)
starNames=[]
starDistance=[]
starRadius=[]
starMass=[]
for i in range(1,len(tempList)):
    starNames.append(tempList[i][1])
    starDistance.append(tempList[i][3])
    starRadius.append(tempList[i][6])
    starMass.append(tempList[i][5])
df=pd.DataFrame(list(zip(starNames,starDistance,starMass,starRadius)),columns=['name','distance','mass','radius'])
df.to_csv("StarsTable.csv")

