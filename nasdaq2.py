import csv
import re
import pandas as pd
import os
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import itertools 
import datetime
import sys


def replaceBlank(x):
  if x == '':
    return 0
  else:
    return x

if __name__ == "__main__":
	ticker = sys.argv[1]
	print(ticker)
	Calls = []
	LastCalls =  []
	ChgCalls = []
	BidCalls = []
	AskCalls = []
	VolCalls = []
	OpenIntCalls = []
	Root = []
	Strike = []
	Puts = []
	LastPuts = []
	ChgPuts = []
	BidPuts = []
	AskPuts = []
	VolPuts = []
	OpenIntPuts = []
	d = {'CallsKey': Calls, 'LastCallKey': LastCalls, 'ChgCallKey': ChgCalls, 'BidCallKey': BidCalls, 'AskCallKey': AskCalls, 'VolCalls': VolCalls, 'OpenIntCalls': OpenIntCalls, 'Root': Root, 'Strike': Strike, 'PutsKey': Puts, 'LastPutKey': LastPuts, 'ChgPutKey': ChgPuts, 'BidPutKey': BidPuts, 'AskPutKey': AskPuts, 'VolPuts': VolPuts, 'OpenIntPuts': OpenIntPuts}

	for i in range(1, 14):
		uClient = uReq('https://www.nasdaq.com/symbol/{}/option-chain?dateindex={}'.format(str(ticker), i))
		page_html = uClient.read()
		uClient.close()
		page_soup = soup(page_html, 'html.parser')
		attributes = page_soup.findAll('div', {'class': 'OptionsChain-chart'})
		attribute = attributes[0]
		tables = attribute.find_all('table')
		table = tables[0]
		rows = table.find_all('tr')
		iterrows = iter(rows)
		next(iterrows)
		for row in iterrows:
			columns = row.find_all('td')
			Calls.append(replaceBlank(columns[0].text))
			LastCalls.append(replaceBlank(columns[1].text))
			ChgCalls.append(replaceBlank(columns[2].text))
			BidCalls.append(replaceBlank(columns[3].text))
			AskCalls.append(replaceBlank(columns[4].text))
			VolCalls.append(replaceBlank(columns[5].text))
			OpenIntCalls.append(replaceBlank(columns[6].text))
			Root.append(replaceBlank(columns[7].text))
			Strike.append(replaceBlank(columns[8].text))
			Puts.append(replaceBlank(columns[9].text))
			LastPuts.append(replaceBlank(columns[10].text))
			ChgPuts.append(replaceBlank(columns[11].text))
			BidPuts.append(replaceBlank(columns[12].text))
			AskPuts.append(replaceBlank(columns[13].text))
			VolPuts.append(replaceBlank(columns[14].text))
			OpenIntPuts.append(replaceBlank(columns[15].text))

		print(d)
	now = datetime.datetime.now()
	file1 = str(ticker) + str(now) + '.csv'
	file2 = str(ticker) + str(now) + '2.csv'
	outfile1 = open(file1, "w") 
	writer = csv.writer(outfile1)
	writer.writerow(d.keys())
	writer.writerows(zip(*d.values()))
	outfile1.close()

	inFile2 = open(file1,'r')

	outFile2 = open(file2,'w')

	listLines = []

	for line in inFile2:

	    if line in listLines:
	        continue

	    else:
	        outFile2.write(line)
	        listLines.append(line)

	outFile2.close()

	inFile2.close()