from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import plotly
import queue_graph as qg

# specify the url
url = "http://reporting.int.godaddy.com/wallboard/ccqueues-international.aspx?UTCOffset=1&Skilltargets=5007|10176"
time_limit = datetime.time(17, 26, 0, 0) # the time at which the script stops
script_name = 'queue_data_' + str(datetime.datetime.now().date()) + '.csv'
refresh_rate = 5 #seconds

while datetime.datetime.time(datetime.datetime.now()) < time_limit:
    file = open(script_name, 'a')

    # query the website
    page = urllib.request.urlopen(url)

    # parse the page with beautifulsoup
    soup = BeautifulSoup(page, 'html.parser')

    # Get the values from the html tab
    name_box = [my_tag.text for my_tag in soup.find_all('td', attrs={'class': 'statWhite'})]

    # Let's write to the file
    temporary_string = (str(name_box[0]) + ',' + str(name_box[1]) + ',' +
                        str(name_box[2]) + ',' + str(datetime.datetime.now()))
    file.write(temporary_string + '\n')
    print('written: ' + temporary_string)
    file.close()

    time.sleep(refresh_rate)

#create the graph
final_graph = qg.create_graph(script_name)

# plot the graph and save the graph
image_name = str(datetime.datetime.now().date()) + '_report'
plotly.offline.plot(final_graph, filename=(image_name + '.html'))