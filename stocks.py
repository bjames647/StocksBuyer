from bs4 import BeautifulSoup
import urllib.request
import time
#from pdb import set_trace as debug

def doRequest(request):
	result = urllib.request.urlopen(request).read()
	soup = BeautifulSoup(result).prettify().encode('UTF-8')
	return soup

def getRequest():
	#request = input('Website: ')
	soup = doRequest('http://www.allpennystocks.com/aps_us/hot_nasdaq_stocks.asp')
	return soup



def main():
	while True:
		soup = getRequest()
		
		print(soup)
		inputVar = input('To run again enter Y. Selection: ')
		if inputVar != 'y' and inputVar != 'Y':
			break

main()
#debug()