# bcopy.py

fobj1 = open('movies.txt', 'r')
fobj2 = open('movies_copy.txt', 'w')

fobj2.write(fobj1.read())

print type(fobj1.read())

fobj1.close()
fobj2.close()

# read single line 
fobj1 = open('movies.txt', 'r')
content = fobj1.readline()
print content
fobj1.close()

# - every readline introduces line feed.
fobj1 = open('movies.txt', 'r')
print fobj1.readline()
print fobj1.readline()
print fobj1.readline()
fobj1.close()

# read all lines at once
fobj1 = open('movies.txt', 'r')
print fobj1.readlines()
fobj1.close()

# string operations
fobj1 = open('movies.txt', 'r')
contents = fobj1.readlines()
for content in contents:
	print content
    if content.startswith("The")
    	print content
fobj1.close()

fobj1 = open('movies.txt', 'r')
for x in fobj1:
	print x