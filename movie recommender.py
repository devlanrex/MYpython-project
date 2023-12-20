# movies={}
# def add ():
#     title = input('enter title')
#     cat = input('enter category')
#     year = input('enter year')
#     movies = {'title':title,'cat':cat,'year':year}
#     movies [len(movies)+1] = movies
#     print('successful')


movies = {"Movie1": {
        "Title": "The Shawshank Redemption",
        "Director": "Frank Darabont",
        "Year": 1994,
        "Genre": ["Drama", "Crime"],
        "IMDb Rating": 9.3,
    },
    "Movie2": {
        "Title": "The Godfather",
        "Director": "Francis Ford Coppola",
        "Year": 1972,
        "Genre": ["Drama", "Crime"],
        "IMDb Rating": 9.2,
    },
    "Movie3": {
        "Title": "The Dark Knight",
        "Director": "Christopher Nolan",
        "Year": 2008,
        "Genre": ["Action", "Crime", "Drama"],
        "IMDb Rating": 9.0,
    },
    "Movie4": {
        "Title": "Pulp Fiction",
        "Director": "Quentin Tarantino",
        "Year": 1994,
        "Genre": ["Crime", "Drama"],
        "IMDb Rating": 8.9,
    },
    "Movie5": {
        "Title": "Schindler's List",
        "Director": "Steven Spielberg",
        "Year": 1993,
        "Genre": ["Biography", "Drama", "History"],
        "IMDb Rating": 8.9,
    },
    "Movie6": {
        "Title": "Forrest Gump",
        "Director": "Robert Zemeckis",
        "Year": 1994,
        "Genre": ["Drama", "Romance"],
        "IMDb Rating": 8.8,
    },
    "Movie7": {
        "Title": "The Matrix",
        "Director": "The Wachowskis",
        "Year": 1999,
        "Genre": ["Action", "Sci-Fi"],
        "IMDb Rating": 8.7,
    },
    "Movie8": {
        "Title": "The Silence of the Lambs",
        "Director": "Jonathan Demme",
        "Year": 1991,
        "Genre": ["Crime", "Drama", "Thriller"],
        "IMDb Rating": 8.6,
    },
    "Movie9": {
        "Title": "Fight Club",
        "Director": "David Fincher",
        "Year": 1999,
        "Genre": ["Drama"],
        "IMDb Rating": 8.8,
    },
    "Movie10": {
        "Title": "Gladiator",
        "Director": "Ridley Scott",
        "Year": 2000,
        "Genre": ["Action", "Adventure", "Drama"],
        "IMDb Rating": 8.5,
    },
    "Movie11": {
        "Title": "The Grand Budapest Hotel",
        "Director": "Wes Anderson",
        "Year": 2014,
        "Genre": ["Adventure", "Comedy", "Crime"],
        "IMDb Rating": 8.1,
    },
    "Movie12": {
        "Title": "The Revenant",
        "Director": "Alejandro González Iñárritu",
        "Year": 2015,
        "Genre": ["Adventure", "Drama", "Thriller"],
        "IMDb Rating": 8.0,
    },
    "Movie13": {
        "Title": "Interstellar",
        "Director": "Christopher Nolan",
        "Year": 2014,
        "Genre": ["Adventure", "Drama", "Sci-Fi"],
        "IMDb Rating": 8.6,
    },
    "Movie14": {
        "Title": "The Departed",
        "Director": "Martin Scorsese",
        "Year": 2006,
        "Genre": ["Crime", "Drama", "Thriller"],
        "IMDb Rating": 8.5,
    },
    "Movie15": {
        "Title": "The Social Network",
        "Director": "David Fincher",
        "Year": 2010,
        "Genre": ["Biography", "Drama"],
        "IMDb Rating": 7.7,
    },
    "Movie16": {
        "Title": "The Prestige",
        "Director": "Christopher Nolan",
        "Year": 2006,
        "Genre": ["Drama", "Mystery", "Sci-Fi"],
        "IMDb Rating": 8.5,
    },
    "Movie17": {
        "Title": "Eternal Sunshine of the Spotless Mind",
        "Director": "Michel Gondry",
        "Year": 2004,
        "Genre": ["Drama", "Romance", "Sci-Fi"],
        "IMDb Rating": 8.3,
    },
    "Movie18": {
        "Title": "No Country for Old Men",
        "Director": "Joel Coen, Ethan Coen",
        "Year": 2007,
        "Genre": ["Crime", "Drama", "Thriller"],
        "IMDb Rating": 8.1,
    },
    "Movie19": {
        "Title": "The Green Mile",
        "Director": "Frank Darabont",
        "Year": 1999,
        "Genre": ["Crime", "Drama", "Fantasy"],
        "IMDb Rating": 8.6,
    },
    "Movie20": {
        "Title": "The Sixth Sense",
        "Director": "M. Night Shyamalan",
        "Year": 1999,
        "Genre": ["Drama", "Mystery", "Thriller"],
        "IMDb Rating": 8.1,
    },
    "Movie21": {
        "Title": "The Avengers",
        "Director": "Joss Whedon",
        "Year": 2012,
        "Genre": ["Action", "Adventure", "Sci-Fi"],
        "IMDb Rating": 8.0,
    },
    "Movie22": {
        "Title": "The Lion King",
        "Director": "Roger Allers, Rob Minkoff",
        "Year": 1994,
        "Genre": ["Animation", "Adventure", "Drama"],
        "IMDb Rating": 8.5,
    },
    "Movie23": {
        "Title": "Inglourious Basterds",
        "Director": "Quentin Tarantino",
        "Year": 2009,
        "Genre": ["Adventure", "Drama", "War"],
        "IMDb Rating": 8.3,
    },
    "Movie24": {
        "Title": "The Wolf of Wall Street",
        "Director": "Martin Scorsese",
        "Year": 2013,
        "Genre": ["Biography", "Comedy", "Crime"],
        "IMDb Rating": 8.2,
    },
    "Movie25": {
        "Title": "Goodfellas",
        "Director": "Martin Scorsese",
        "Year": 1990,
        "Genre": ["Biography", "Crime", "Drama"],
        "IMDb Rating": 8.7,
    },
    "Movie26": {
        "Title": "For a Few Dollars More",
        "Director": "Sergio Leone",
        "Year": 1965,
        "Genre": ["Western"],
        "IMDb Rating": 8.3,
    },
    "Movie27": {
        "Title": "The Terminator",
        "Director": "James Cameron",
        "Year": 1984,
        "Genre": ["Action", "Sci-Fi"],
        "IMDb Rating": 8.0,
    },
    "Movie28": {
        "Title": "The Shining",
        "Director": "Stanley Kubrick",
        "Year": 1980,
        "Genre": ["Drama", "Horror"],
        "IMDb Rating": 8.4,
    },
    "Movie29": {
        "Title": "Avatar",
        "Director": "James Cameron",
        "Year": 2009,
        "Genre": ["Action", "Adventure", "Fantasy"],
        "IMDb Rating": 7.8,
    },
    "Movie30": {
        "Title": "Jurassic Park",
        "Director": "Steven Spielberg",
        "Year": 1993,
        "Genre": ["Adventure", "Sci-Fi"],
        "IMDb Rating": 8.1,
    },
}


def recommender(pres):
    movie = []
    for per in pres:
        for key in movie:
            if movie[key]['Genre'].__contains__(per):
                movie.append(movies[key])
    return movies

Exit = False
pres = []

while not Exit:
    pres = input("Enter preference: ")
    pres.append(pres)
    e = input("Have you got your preference [y/n]: ")

    if e == "y":
        Exit = True
    