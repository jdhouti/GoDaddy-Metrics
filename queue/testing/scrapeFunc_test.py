from bs4 import BeautifulSoup
import urllib.request
import datetime

def scrape():
	url = "http://reporting.int.godaddy.com/wallboard/ccqueues-international.aspx?UTCOffset=1&Skilltargets=5007|10176"
	page = urllib.request.urlopen(url)

	# parse the page with beautifulsoup
	soup = BeautifulSoup(page, 'html.parser')

	# Get the values from the html tab
	name_box = [my_tag.text for my_tag in soup.find_all('td', attrs={'class': 'statWhite'})]

	return (name_box[0], name_box[2])
	