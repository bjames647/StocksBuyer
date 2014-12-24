from bs4 import BeautifulSoup as BS
import urllib.request
import time
from pdb import set_trace as debug

def doRequest(request):
	result = urllib.request.urlopen(request).read()
	soup = BS(result, from_encoding='UTF-8')
	return soup

def getRequest():
	#request = input('Website: ')
	soup = 'http://www.allpennystocks.com/aps_us/hot_nasdaq_stocks.asp'
	return soup

def mineN(soup):
	data = []
	soup = soup.findAll("td", {"width":"10%"})

	for blarg in soup:
		data.append(str(blarg.contents))
	
	counter = 0
	for d in data:
		stringData = data[counter]
		stringData = stringData[2:-2]
		stringData = stringData.replace(',','')
		data[counter] = int(stringData)
		counter = counter + 1
		#print(stringData)
	return data

#def mineSD(soup):

#def mineN(soup):

#def mineXBar(soup):

#def getPValue():

def main():
	while True:
		request = getRequest()
		soup = doRequest(request)
		population = mineN(soup)
		
		inputVar = input('To run again enter Y. Selection: ')
		if inputVar != 'y' and inputVar != 'Y':
			break

main()
