import re
dir(re)

string = "Hi! My name is Mike. I'm learning how to build a search function with Python."

re.search("Mike", string)

m = re.search("Mike", string)

print(m)

start = m.start()
end = start + 4

print(start)
print(end)

print(string[start:end])

#I don't understand why the name "Mike" doesn't print out when you run the code. It works in the terminal.