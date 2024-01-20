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

# 1 answer
def low_imdb(movie):
    if movie["imdb"] < 5.5:
        return True
    else: return False
    
# 2 answer
def low_list():
    answer = []
    for movie in movies:
        if low_imdb(movie):
            answer.append(movie)
    return answer

# 3 answer
def cat_finder(cat):
    answer = []
    for movie in movies:
        if movie["category"] == cat:
            answer.append(movie)
    return answer

# 4 answer 
def ave_rating(films):
    rate = 0
    for movie in films:
        rate += movie["imdb"]
    return rate/len(films)

# 5 answer
def ave_cat_rating_v1(cat):
    rate = 0
    num = 0
    for movie in movies:
        if movie["category"] == cat:
            rate += movie["imdb"]
            num += 1
    return rate/num

def ave_cat_rating_v2(cat):
    return ave_rating(cat_finder(cat))

print(low_list())

print(ave_cat_rating_v2("Romance"))