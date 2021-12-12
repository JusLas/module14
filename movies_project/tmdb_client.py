import requests

API_TOKEN = (
    "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2Njg2OWJiMDkzZTJiY2YyYzUzOGRlYWYxZjM3NjYz"
    "YiIsInN1YiI6IjYxYTI0ZjRmZGUxMWU1MDAyZDA2NWZmMiIsInNjb3BlcyI6WyJhcGlfcmVhZ"
    "CJdLCJ2ZXJzaW9uIjoxfQ.qQqehPsS3Tg7kO__7YFcEM3JnqTKZtXrOaVBlT8eW_0")

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_popular_movies():
    return call_tmdb_api("movie/popular")


def get_movie_info(movie):
    return {
        "id": movie["id"],
        "title": movie["title"],
        "poster_path": movie["poster_path"]
    }


def get_poster_url(path, size="w342"):
    return f"https://image.tmdb.org/t/p/{size}{path}"


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(
  movie_id, how_many=4, only_with_img=True, characters_only=True):
    cast =  call_tmdb_api(f"movie/{movie_id}/credits")["cast"]

    if only_with_img:
        cast = [c for c in cast if c.get("profile_path", None)]

    if characters_only:
        cast = [c for c in cast if "character" in c]
    
    return cast[:how_many]


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_movies(list_type="popular", how_many=8):
    data = get_movies_list(list_type)

    return data["results"][:how_many]


def get_available_list_types():
    return ["now_playing", "popular", "top_rated", "upcoming"]