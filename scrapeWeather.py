import re
import urllib.request

#url = http://www.weather-forecast.com/locations/Montreal/forecasts/latest

city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#print(data1)

m = re.search('span class="phrase">', data1) #The > just removes the same symbol that is at the beggining of the sentence for some reason when we print it out. 

start = m.end()

end = start + 300

newString = data1[start:end]
print(newString)

m = re.search("/span", newString)

end = m.start() -1

final = newString[0:end]

print(final)