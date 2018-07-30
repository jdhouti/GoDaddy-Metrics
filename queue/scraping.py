from bs4 import BeautifulSoup
import urllib.request
import time
import datetime

# specify the url
url = "http://reporting.int.godaddy.com/wallboard/ccqueues-international.aspx?UTCOffset=1&Skilltargets=5007|10176"

while True:
    file = open('queue_data.csv', 'a')

    # query the website
    page = urllib.request.urlopen(url)
	
    # parse the page with beautifulsoup
    soup = BeautifulSoup(page, 'html.parser')

    # Get the values from the html tab
    name_box = [my_tag.text for my_tag in soup.find_all('td', attrs={'class': 'statWhite'})]
	
    # Let's write to the file
    temporary_string = str(name_box[0]) + ', ' + str(name_box[1]) + ', ' + str(datetime.datetime.now())
    file.write(temporary_string + '\n')
    print('written: ' + temporary_string)
    file.close()

    time.sleep(30)