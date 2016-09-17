import re
import urllib.request

#toyotaModel = ["Yaris Hatchback", "Yaris Sedan", "Corolla", "Corolla iM", "Toyota 86", "Prius c", "Prius", "Prius v", "Camry", "Camry Hybrid", "Avalon", "Sienna", "RAV4", "Tacoma", "Tundra"]

type = input("Enter the Toyota model you're looking for: ")
url = "http://www.toyota.ca/toyota/en/build-price/" + type + "models-options"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#print(data1)

m = re.search('div id="summary_tables_panel"', data1)
print(m)
start = m.end()

end = start + 100
newString = data1[start:end]
#print(newString)

m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
#print("The price of the " + type + "is" + final)#
