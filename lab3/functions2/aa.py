# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_highly_rated_by_name(movie_name):
    for movie in movies:
        if movie["name"] == movie_name:
            return movie["imdb"] > 5.5
    return False 


print(is_highly_rated_by_name("Hitman"))  
print(is_highly_rated_by_name("AlphaJet"))

def highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


high_rated = highly_rated_movies(movies)
print(high_rated)

def movies_by_category(category_name):
    return [movie for movie in movies if movie["category"] == category_name]


romance_movies = movies_by_category("Romance")
print(romance_movies)


def average_imdb_score(movies):
    if not movies:  # Check if the list is empty
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)


average_score = average_imdb_score(movies)
print(average_score)


def average_imdb_by_category(category_name):
    category_movies = [movie for movie in movies if movie["category"] == category_name]
    
    if not category_movies:
        return 0
    
    total_score = sum(movie["imdb"] for movie in category_movies)
    return total_score / len(category_movies)

average_romance_score = average_imdb_by_category("Romance")
print(average_romance_score)
