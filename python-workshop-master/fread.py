fobj = open('movies.txt')
contents = fobj.read()
print contents
fobj.close()


fobj = open('movies.txt')
contents = fobj.read()
print "After First Read", contents
contents = fobj.read()
print "After Second Read", contents // return ''
fobj.close()


fobj = open('movies.txt')
print fobj.readline()
print fobj.readline()
fobj.close()

fobj = open('movies.txt')
print fobj.readlines()
fobj.close()


fobj = open('movies.txt')
contents = fobj.readlines()
for content in contents:
    print content
fobj.close()

fobj = open("movies.txt")
for x in fobj:
    print x
fobj.close()
