import re
import urllib.request

arrayOfStocks = ["Dow Jones", "Nasdaq", "FB"]

url = "https://www.google.ca/finance?q="

stock = input("Enter your stock: ")

url = url + stock

data = urllib.request.urlopen(url).read()

data1 = data.decode("utf-8")
print(data1)

