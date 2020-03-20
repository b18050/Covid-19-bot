""" load used libraries"""
import requests
import json
import logging
import argparse
import pandas as pd
from bs4 import BeautifulSoup

""" load the website you will use""" 
URL = 'https://www.mohfw.gov.in/'

data = []  #global list for data

response = requests.get(URL).content  # call requests
soup = BeautifulSoup(response, 'html.parser') # use html parser
header = soup.tr.find_all('th')
all_rows = soup.find_all('tr')

for row in all_rows:
    col = row.find_all('td')
    data.append(col)
    
#COLUMNS = ['serial_number', 'State', 'In', 'Fr', 'Cd', 'Dt']

Sno = []
State = []
Indian = []
Foreigner = []
Cured = []
Death = []
for d in data[1:len(data)-2]:
    for j in range(6):
        d[j] = str(d[j])
        local = d[j][d[j].find('width')+11:-5]
        if(j == 1):
            State.append(local)
        else:
            local = int(local)
            if(j==0):
                Sno.append(local)
            elif(j==2):
                Indian.append(local)
            elif(j==3):
                Foreigner.append(local)
            elif(j==4):
                Cured.append(local)
            else:
                Death.append(local)
A = {}
A['Serial number'] = Sno
A['State'] = State
A['Indian'] = Indian
A['Foreigner'] = Foreigner
A['Cured'] = Cured
A['Death'] = Death
    
df = pd.DataFrame(A)          

            
            
