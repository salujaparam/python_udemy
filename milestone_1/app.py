movies = []

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to exit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command- please try again!!')
        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to exit: ")

def add_movie():
    name = input('\nEnter the movie name: ')
    director = input('Enter the movie director: ')
    year = input('Enter the movie release year: ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })

def show_movies(movies_list):
    for movie in movies_list:
        print_movies(movie)
def print_movies(movie):
    print(f"\nName: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def find_movie():
    find_by = input('What property of the movie are you looking for?')
    looking_for = input('What are you looking for?')

    found_movies = search_by_attr(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)

def search_by_attr(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found
menu()