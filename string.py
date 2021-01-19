stirng = "     Hello     "
# remove the whitespace
print(stirng.startswith("H"))
# find endswith return bool
print(stirng.endswith(" "))
print(stirng.strip())
# find the word index
print(stirng.find('l'))
# if no result then -1
print(stirng.find('dd'))
print(stirng.count("l"))
print(stirng.replace("H", "Trol"))
stringtry = "how are you"
# to split and take each word and then the parameter is the delimiter
thelist = stringtry.split(" ")
# to join all the element inside a string
newstring = " ".join(thelist)
print(newstring)
print(thelist)
# other example
alist = ['a'] * 6
astring = " ".join(alist)
print(astring)
