import requests
from bs4 import BeautifulSoup
import json
import re
import os
import time
#from GoogleNews import GoogleNews

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
base_link='https://finance.yahoo.com/quote/CIIC?ltr=1'

def findAllMergedCompany(url):
	links = [];
	req = requests.get(url, headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	searched_word = "merge"
	results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)

	print ('Found the word "{0}" {1} times\n'.format(searched_word, len(results)))

	for content in results:
		words = content.split()
		for index, word in enumerate(words):
			# If the content contains the search word twice or more this will fire for each occurence
			if word == searched_word:
				#print ('Whole content: "{0}"'.format(content))
				before = None
				after = None
				# Check if it's a first word
				if index != 0:
					before = words[index-1]
				# Check if it's a last word
				if index != len(words)-1:
					after = words[index+1]
				print ('\tWord before: "{0}", word after: "{1}"'.format(before, after))

	return len(results)
	

def notify(text):
    os.system("osascript -e 'display notification \"{0}\"'".format(text))

"""
googlenews = GoogleNews()
googlenews = GoogleNews(lang='en')
googlenews = GoogleNews(period='7d')
googlenews = GoogleNews(encode='utf-8')
googlenews.get_news('Yahoo finance merge')
googlenews.search('Yahoo finance merge')

googlenews.results()
googlenews.get_texts()

"""

while True:
	print("\nStart searching...\n")
	output = findAllMergedCompany(base_link);
	if output > 0:
		notify(text = 'found {0} result. '.format(output))	
	time.sleep(10);
