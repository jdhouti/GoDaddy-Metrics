# Metrique
### The Queue Project
Every day at GoDaddy, hundreds of customers are calling in to resolve issues on their site, to request certain features, or even to ask for some advice on their business. Throughout the day, the queue goes up and down in numbers but there is no tool to graph the historical levels throughout the day. <b>The Queue Project</b> is a web application that I built in Python that scrapes data from our queues every 4 seconds and then graphs the results live within your browser. Additionally, at the end of each day, a daily report is automatically generated.

![Live Queue Graph](https://github.com/jdhouti/Metrique/blob/master/images/demo.png)

---
### The Metrics Project
As a consultant at GoDaddy, we are constantly tracked on a dozen of metrics, including our customer availability (our percentage of availability on the phone), our sales (new revenue and renewed revenue), our survey scores etc. Although they allow us to obtain this data so that we can track our performance, we are not provided with any analytical tools so the data is rendered meaningless for us agents. We have no way of visualizing our performance.

A few months ago, I started recording this data on a spreadsheet that I would take home and look over. Even though I wasn't provided with any graph tools, I saw no reason to not make any myself, so I got to work with jupyter notebooks. 

Unfortunately after reaching out to my supervisor, I was told that I could not upload any of my real data so I had to
generate random data so that I could at least upload my notebooks to Github, even if the data is meaningless.

After a few hours, I was able to create this following pipeline layout:
![Pipeline Flow Chart](https://github.com/jdhouti/Metrique/blob/master/images/flowchart.jpg)

One of the questions that is probably on your mind is why does my `random_data_generation.ipynb` notebook purposely create non-clean data? I wanted to demonstrate my `data_cleaning.ipynb` notebook but since it contained real data *(which I cannot upload)*, I had to create a new identical notebook called `random_data_cleaning.ipynb` where I would pass my "non-clean" random data.

The end result is not yet available in `visualize.ipynb` because Github does not allow iframes to render in Jupyter notebooks
yet.
