from bs4 import BeautifulSoup
import urllib.request
import time

def doRequest(request):
	result = urllib.request.urlopen(request).read()
	soup = BeautifulSoup(request, from_encoding='utf8')
	return soup

def getRequest():
	request = input('Website: ')
	data = {}
	#request = urllib.Request(request)
	soup = doRequest(request)
	return soup



def main():
	while True:
		soup = getRequest()
		print(soup)
		inputVar = input('To run again enter Y. Selection: ')
		if inputVar != 'y' and inputVar != 'Y':
			break

main()