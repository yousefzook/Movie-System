from movie import  Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def watchedMovies(self):
        watchedList = list(filter(lambda movie: movie.watched, self.movies))
        return watchedList

    def addMovie(self, name, genre):
        newMovie = Movie(name, genre, False)
        self.movies.append(newMovie)

    def deleteMovie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))


    def json(self):
        return {
            'name' : self.name,
            'movies' : [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def fromJson(cls, jsonData):
        user = User(jsonData['name'])
        for movie in jsonData['movies']:
            user.movies.append(Movie.fromJson(movie))
        return user

    def setWatched(self,name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True
                break