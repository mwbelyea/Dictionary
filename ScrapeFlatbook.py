# #taken from altitudelabs.com

# #import libraries
# import urllib2
# from bs4 import BeautifulSoup

# #specify the url
# quote_page = 'https://www.flatbook.co/'

# #Then, make use of the Python urllib2 to get the HTML page of the url declared.
# #query the website and return the html to the variable 'page'
# page = urllib2.urlopen(quote_page)

# #parse the html using beautiful soup and store in variable 'soup'
# soup = BeautifulSoup(page, 'html.parser')

# #now we have a variable soup containing the HTML of the page. Here's where we can start extracting the data. 

# name_box = soup.find('section', {'class': 'section-featured-cities'})

# #After we have the tag, we can get the data by getting its text:

# name = name_box.text.strip()
# #strip() is used to remove starting and trailing print name

sen = "Hello %s, you're invited to my birthday."
  print(sen%("Kira"))
