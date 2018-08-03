from bs4 import BeautifulSoup
import urllib.request
import time
import datetime

data_filename = 'french_queue_data_' + str(datetime.datetime.now().date()) + '.csv'
url = "http://reporting.int.godaddy.com/wallboard/ccqueues-international.aspx?UTCOffset=1&Skilltargets=5007|10176"
time_limit = datetime.time(13, 30, 0, 0)
refresh_rate = 15 #seconds

print('info : current time is ' + str(datetime.datetime.now()))
print('info : file name is ' + data_filename)

while datetime.datetime.time(datetime.datetime.now()) < time_limit:
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print('error: url could not be reached')
        break

    # parse the page with beautifulsoup
    soup = BeautifulSoup(page, 'html.parser')

    # Get the values from the html tab
    name_box = [my_tag.text for my_tag in soup.find_all('td', attrs={'class': 'statWhite'})]

    # Let's write to the file
    temporary_string = (str(name_box[2]) + ',' + str(name_box[3]) + ',' +
                        str(datetime.datetime.now()))

    file = open(data_filename, 'a')
    file.write(temporary_string + '\n')
    print('info : ' + temporary_string)
    file.close()
    
    time.sleep(refresh_rate)

# close the file
print('info : time limit exceeded')
print('info : open graph.py to generate report')

input()