from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com/"

def get_category_links(section_url):
  html = urlopen(section_url).read()
  soup = BeautifulSoup(html, "lxml")
  boccat = soup.find("dl", "boccat")
  category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
  return category_links

def get_category_winner(category_url):
  html = urlopen(category_url).read()
  soup = BeautifulSoup(html, "lxml")
  category = soup.find("h1", "headline").string
  winner = [h2.string for h2 in soup.findAll("h2", "boc2")]
  return {"category": category,
          "category_url": category_url,
          "winner": winner,
          "runners_up": runners_up}


def make_soup(url):
  html = urlopen(url).read()
  return BeautifulSoup(html, "lxml")

soup = make_soup(url) # where url is the url we're passing into the original function