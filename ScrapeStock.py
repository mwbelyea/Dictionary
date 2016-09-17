import re
import urllib.request

#https://www.google.ca/finance?q=
url = "https://www.google.ca/finance?q="

stock = input("Enter your stock: ")
url = url + stock #Concatenation of strings
print(url)

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)

m = re.search('meta itemprop="price"', data1)
print(m)

start = m.start()
end = start + 50 

newString = data1[start:end]
print(newString)

m = re.search('content="', newString)
start = m.end()

newString1 = newString[start:]
print(newString1)

m = re.search("/", newString1)
end = m.end()-3

final = newString1[0:end]
print(final)

print("The value of " + stock + " is " + final)