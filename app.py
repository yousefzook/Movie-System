import os
import json
from user import User
from movie import Movie
def menu():
    userName = input("Please Enter your name: ")
    fileName = "{}.txt".format(userName)
    if fileExists(fileName):
        with open(fileName, "r") as f:
            jsonData = json.load(f)
        user = User.fromJson(jsonData)
        print("Hello {}".format(userName))
    else:
        user = User(userName)

    op = 'a'
    while op != 'q':
        op = input("Enter 'a' to add movie, 's' to see movies,"
                   " 'w' to set a movie as watched, 'd' to delete a movie,"
                   " 'l' to see the list of watched movies or 'q' to save and quit: ")
        if op == 'a':
            movieName = input("enter movie name: ")
            movieGenre = input("enter movie genre: ")
            user.addMovie(movieName,movieGenre)
        elif op == 's':
            for movie in user.movies:
                print("Name:{} , Genre:{} , Watched:{}".format(movie.name,movie.genre,movie.watched))
        elif op == 'w':
            movieName = input("Enter the movie name to set watched: ")
            user.setWatched(movieName)
        elif op == 'd':
            movieName = input("Enter the movie name to delete: ")
            user.deleteMovie(movieName)
        elif op == 'l':
            for movie in user.watchedMovies():
                print("Name:{} , Genre:{} , Watched:{}".format(movie.name, movie.genre, movie.watched))
        elif op == 'q':
            with open(fileName, 'w') as f:
                json.dump(user.json(),f)



def fileExists(fileName):
    return os.path.isfile(fileName)

menu()