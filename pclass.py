"""
class ABC():
	def xyz(self):
		----

	def abc(self):
		----

"""

class Movies():
	def __init__(self):
		self.movie_names = []
		self.ratings = []

	def populate_movie_names(self, movie_dict):
		for movie, rating in movie_dict.items():
			self.movie_names.append(movie)

	def populate_ratings(self, movie_dict):
		for movie, rating in movie_dict.items():
			self.ratings.append(rating)

	def update_movie(self, movie_dict, update_movie_dict):
		
 

def print_message(msg):
		return '/-------- %s ---------/' % msg


fobj1 = open('movies.txt', 'r')

movie_dict = {}

for x in fobj1:
	movie, rating = x.strip().rsplit(' ', 1)
	movie_dict[movie] = rating



movieobj = Movies()
print print_message("Before populating:")
print movieobj.movie_names

print print_message("After populating:")
movieobj.populate_movie_names(movie_dict)
print movieobj.movie_names

print print_message("Movie Ratings")
movieobj.populate_ratings(movie_dict)
print movieobj.ratings
