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

def doMining(soup):
	data = []
	#
	i = 0
	soup = soup.findAll("td", {"width":"10%"})
	for blarg in soup:
		data.append(str(blarg.contents))
		
		#print(i)
	#debug()
	counter = 0
	for d in data:
		print(i)
		balls = data[counter]
		#print(balls)
		i = i + balls
		counter = counter + 1
	#print(data[0])

def main():
	while True:
		request = getRequest()
		soup = doRequest(request)
		#debug()
		doMining(soup)
		#print(soup)
		inputVar = input('To run again enter Y. Selection: ')
		if inputVar != 'y' and inputVar != 'Y':
			break

main()
