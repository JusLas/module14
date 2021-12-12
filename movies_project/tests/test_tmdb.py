from unittest.mock import Mock
import tmdb_client
import json
import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    with open(
        os.path.join(CURR_DIR, 'data', 'movie.json'), "r") as f:
        MOVIE = json.load(f)
except FileNotFoundError:
    MOVIE = None

try:
    with open(
        os.path.join(CURR_DIR, 'data', 'credits.json'), "r") as f:
        CREDITS = json.load(f)
except FileNotFoundError:
    CREDITS = None

def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def some_function_to_mock():
    raise Exception("Original was called")


def test_mocking(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = 2
    monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
    result = some_function_to_mock()
    assert result == 2


def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_call_tmdb_api(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.call_tmdb_api("movie/popular")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    api_mock = Mock(return_value=MOVIE)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    movie = tmdb_client.get_single_movie(550)

    assert api_mock.call_args == (('movie/550',),)

    assert movie == MOVIE


def test_get_movie_info():
    movie_info = tmdb_client.get_movie_info(MOVIE)

    assert MOVIE["id"] == movie_info["id"]
    assert MOVIE["title"] == movie_info["title"]
    assert MOVIE["poster_path"] == movie_info["poster_path"]

    assert len(movie_info.keys()) == 3


def test_get_single_movie_cast(monkeypatch):
    
    api_mock = Mock(return_value=CREDITS)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    cast = tmdb_client.get_single_movie_cast(550)

    assert api_mock.call_args == (('movie/550/credits',),)

    assert len(cast) == 4

    for c in cast:
        assert c.get("profile_path", None) is not None