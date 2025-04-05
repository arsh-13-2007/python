""" 5.	Store details of n movies in a dictionary by taking input from the user.
 Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
a)	print all movie details
b)	display name of movies released before 2015
c)	print movies that made a profit.
d)	print movies directed by a particular director."""
movies = {}
n = int(input("Enter the number of movies: "))
for i in range(n):
    name = input("Enter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    production_cost = float(input("Enter production cost: "))
    collection = float(input("Enter collection made (earnings): "))
    movies[name] = {
        'year': year,
        'director': director,
        'production_cost': production_cost,
        'collection': collection
    }
print("\nAll Movie Details:")
for movie, details in movies.items():
    print(f"{movie}: {details}")
print("\nMovies released before 2015:")
for movie, details in movies.items():
    if details['year'] < 2015:
        print(movie)
print("\nMovies that made a profit:")
for movie, details in movies.items():
    if details['collection'] > details['production_cost']:
        print(movie)

director_name = input("\nEnter the director's name to search for their movies: ")
print(f"\nMovies directed by {director_name}:")
for movie, details in movies.items():
    if details['director'].lower() == director_name.lower():
        print(movie)
