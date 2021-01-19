mydict = {"name": "max", "age": 26, "city": "new york"}
print(mydict)
mydict2 = dict(name="mary", age=34, city="Indonesia")
print(mydict2)
try:
    print(mydict["lastname"])
except:
    print("error")
for key, value in mydict.items():
    print(key, value)
# update object value
mydict.update(mydict2)
print(mydict)

mytuple = (8, 7)
thedict = {mytuple: 15}
print(thedict)
