from bs4 import BeautifulSoup
import requests

#with open : file object
with open('simple.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

#prettify is method to see whole html data intended
print(soup.prettify())
