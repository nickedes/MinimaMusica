import urllib.request as ur
from html.parser import HTMLParser
import os
import json
import dataMake as dm       # helps in getting data in the required format.

url = "http://songspk.name/indian-mp3-songs/gunday-2013-mp3-songs.html"
filename = 'Songs.html'
movName = 'Gunday.txt'
coverArt = 'Gunday.jpg'

# Parser class
img = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'src' and '.jpg' in attr[1] :
                img.append(attr[1])
    def handle_data(self, data):
        if (';' not in data and data.strip() != ''):
            g.write(data + '\n')

# Downloading HTML file if not already present.
if not (os.path.isfile("/home/minima/Desktop/musicBrainz/Songs.html")):
	f = open(filename, 'wb')
	with ur.urlopen(url) as alpha:
		f.write(alpha.read())
	f.close()

# parsing the HTML file for image link and song data
parser = MyHTMLParser()
g = open(movName, 'w')
with open(filename, 'r') as f:
		line = f.readline()
		while not line == '' :
			parser.feed(line)
			line = f.readline()
f.close()
g.close()

# making the data
f = open(movName, 'r')
line = f.readlines()
f.close()
os.remove(movName)

a = dm.actualData(dm.listing(line))
json.dump(a, open(movName, 'w'))
print (a)

# Cover Art 
f = open(coverArt, 'wb')
f.write(ur.urlopen(img[0]).read())
f.close()

os.remove("Songs.html")


