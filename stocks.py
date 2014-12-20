from bs4 import BeautifulSoup
import urllib.request
import time

def doRequest(request):
	result = urllib.request.urlopen(request)
	soup = BeautifulSoup(request, from_encoding='utf8')
	return soup

def getRequest():
	request = input('Website: ')
	request = urllib.request.Request(request)
	soup = doRequest(request)
	return soup



def main():
	while True:
		getRequest()
		inputVar = input('To run again enter Y. Selection: ')
		if inputVar != 'y' and inputVar != 'Y':
			break

main()