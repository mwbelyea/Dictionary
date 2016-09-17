import requests 
from bs4 import BeautifulSoup


url = "http://www.yellowpages.ca/search/si/1/coffee/Montreal%2C%20QC"
r = requests.get(url)

soup = BeautifulSoup(r.content)


links = soup.find_all("a")

for link in links:
  print “<a href=‘%s’>%s</a>” %(link.get(“href”), link.text)


g_data = soup.find_all("div", {"class": "listing__right article hasIcon"}) #note only one class can be used. Choose either listing__right, article, or hasIcon
print g_data

for item in g_data:
  print item.text

for item in g_data:
  print item.contents[1].text
  print item.contents[3].text

