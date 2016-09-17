import re
import urllib.request


# url = http://www.dictionary.com/
word = input("Choose a word to look up:" )
url = "http://www.dictionary.com/browse/" + word +"?s=t"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#print(data1)

m = re.search('meta name="description" content="', data1)
#print(m)

start = m.end()

end = start + 300

newString = data1[start:end]
#print(newString)

m = re.search("See more.", newString)
end = m.start() - 1
#end = m.search 

final = newString[0:end]
print(final)
