def movie_organizer(*movies_info):
    result = []
    movies_data = {}

    for movie_name, genre in movies_info:
        if genre not in movies_data:
            movies_data[genre] = []
        movies_data[genre].append(movie_name)

    for movie_genre, movies in sorted(movies_data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result.append(f"{movie_genre} - {len(movies)}")
        for movie in sorted(movies):
            result.append(f"* {movie}")

    return '\n'.join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
