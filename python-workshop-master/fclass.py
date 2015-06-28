class Movies():
    def __init__(self):
        self.movie_names = []
        self.ratings = []

    def populate_movie_names(self, movie_dict):
        for movie, rating in movie_dict.items():
            self.movie_names.append(movie)

    def populate_rating(self, movie_dict):
        for movie, rating in movie_dict.items():
            self.ratings.append(rating)

    def is_movie_name(self, name):
        return name in self.movie_names

    def update_movie(self, movie_dict, update_movie_dict):
        movie_dict.update(update_movie_dict)

        for movie, rating in update_movie_dict.items():
            self.movie_names.append(movie)
            self.ratings.append(rating)

        return movie_dict
        
def print_message(msg):
    return '/------ %s -------/' % msg

movieobj = Movies()
print print_message("After Intialization")
print movieobj.movie_names
print movieobj.ratings

fobj = open("movies.txt")

movie_dict = {}
for x in fobj:
    movie, rating = x.strip().rsplit(' ', 1)
    movie_dict[movie] = rating

movieobj.populate_movie_names(movie_dict)
movieobj.populate_rating(movie_dict)

print print_message("After Populating")

print movieobj.movie_names
print movieobj.ratings

print movieobj.is_movie_name('Fight Club') 

movie_dict = movieobj.update_movie(movie_dict, {'Gangs of Wasseypur': '8.6'})
print print_message("After Updating Movie")

print "Movie Dict", movie_dict
print "movie name list", movieobj.movie_names
print "movie rating list", movieobj.ratings


try:
    memento = movie_dict['memento']
except NameError:
    print 'In NameError'
    memento = 0
except KeyError:
    print 'In KeyError'
    memento = 0
print memento
