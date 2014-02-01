import urllib.request as ur
from html.parser import HTMLParser
import os
import dataMake as dm

url = "http://songspk.name/indian-mp3-songs/gunday-2013-mp3-songs.html"
filename = 'songs.html'
movName = 'gunday.txt'

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if (';' not in data and data.strip() != ''):
            g.write(data + '\n')

parser = MyHTMLParser()

if not (os.path.isfile("/home/minima/Desktop/musicBrainz/songs.html")):
	f = open(filename,'wb')
	with ur.urlopen(url) as alpha:
		f.write(alpha.read())
	f.close()

g = open(movName, 'w')

with open(filename, 'r') as f:
		line = f.readline()
		while not line == '' :
			parser.feed(line)
			line = f.readline()
g.close()
f = open('gunday.txt', 'r')
line = f.readlines()
f.close()

a = dm.actualData(dm.listing(line))
print (a)
#os.remove("alpha.html")
