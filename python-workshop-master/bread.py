fobj = open('movies.txt')
print 'After exectuing read()'
print fobj.read()
fobj.close()
fobj = open('movies.txt')
print 'After executing read() again'
print fobj.read()
