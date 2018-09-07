import urllib2
from bs4 import BeautifulSoup

url = "http://www.lolking.net/champions"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

imgs = soup.findAll("img", {"class":"champion-icon image-responsive"})
names = soup.findAll("div",{"class":"champion-name"})

print("returning images...")
for img in imgs:
        print img.a['href'].split("imgurl=")[1]
print("All Image URLs printed!")

print("returning names...")
for name in names:
	print(name)

print("All names printed!")
print("Done!")