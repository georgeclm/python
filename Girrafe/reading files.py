# "r" to read files "w" to write files and "a" to add new indo "r+" read and more
the_file = open("blabla.txt", "r")
print(the_file.readable())
for file in the_file.readlines():
    print(file)
# readlines to read all text and put it in array each line and can take index
# print(the_file.readlines()[1])
# readline to read 1 line
print(the_file.readline())
print(the_file.readline())
print(the_file.readline())

the_file.close()