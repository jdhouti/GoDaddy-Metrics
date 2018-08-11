from bs4 import BeautifulSoup
import urllib.request
import datetime

def scrape():
	data_filename = 'queue_data_' + str(datetime.datetime.now().date()) + '.csv'
	url = "http://reporting.int.godaddy.com/wallboard/ccqueues-international.aspx?UTCOffset=1&Skilltargets=5007|10176"
	page = urllib.request.urlopen(url)

	# parse the page with beautifulsoup
	soup = BeautifulSoup(page, 'html.parser')

	# Get the values from the html tab and record them as well
	file = open(data_filename, 'a')
	name_box = [my_tag.text for my_tag in soup.find_all('td', attrs={'class': 'statWhite'})]
	temporary_string = (str(name_box[0]) + ',' + str(name_box[1]) + ',' +
                        str(name_box[2]) + ',' + str(datetime.datetime.now()))
	file.write(temporary_string + '\n')
	file.close()

	return (name_box[0], name_box[2])
	