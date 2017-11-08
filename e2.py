#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

url_va = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req_va = requests.get(url_va)
html_va = req_va.content
soup = bs(html_va,'html.parser') 
tags = soup.find_all('tr','election_item')

ELECTION_ID=[]
for t in tags:
    year = t.td.text
    year2 = t['id'][-5:]
    i=[year,year2]
    ELECTION_ID.append(i)

Year = [item[0] for item in ELECTION_ID]
ID = [item[1] for item in ELECTION_ID]
m = dict(zip(ID, Year))
m

for t in ID:
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    replace_url = base.format(t)
    response = requests.get(replace_url).text
    Year_data = "president_general_"+ m[t] +".csv"
    with open(Year_data, 'w') as output:
        output.write(response)
