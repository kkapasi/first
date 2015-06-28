fobj1 = open('movies.txt', 'r')

for x in fobj1.readlines():
	print x.strip().rsplit(' ', 1)
# strip removes the additonal \n present in the file

fobj1.close()

fobj1 = open('movies.txt', 'r')

movie_dict = {}

for x in fobj1:
	movie, rating = x.strip().rsplit(' ', 1)
	movie_dict[movie] = rating


print movie_dict

for item in movie_dict.items():
	print item
	print type(item)
# the above output item is a tuple

# so to get individual values, we can do this.
for movie, rating in movie_dict.items():
	print 'Key', movie 
	print 'Value', rating

try:
	movie_dict['Memento']
	# other method for this is movie_dict.get('Memento')
except:
    Memento = 0

print Memento	

print "***Movies with rating 8.9***\n"
for movie, rating in movie_dict.items():
	if rating == "8.9":
		print movie



fobj1.close()
