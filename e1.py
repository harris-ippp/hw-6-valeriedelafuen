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
    i=[year, year2]
    ELECTION_ID.append(i)
    print(year, year2)

with open('ELECTION_ID','w') as ELECTION_ID_file:
    for line in ELECTION_ID:
        ELECTION_ID_file.write(line[0] + ' ' + line[1])
        print(line[0],line[1])
