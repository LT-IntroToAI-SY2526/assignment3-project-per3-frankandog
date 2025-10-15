from main import f1driverdb
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "movie" (a tuple)
def get_title(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]


def get_director(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_actors(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]



def title_by_year(matches: List[str]) -> List[str]:

    year = int(matches[0])
    result = []
    for movie in f1driverdb:
        if get_year(movie) == year:
            result.append(get_title(movie))
    return result

def title_by_year_range(matches: List[str]) -> List[str]:

    start_year = int(matches[0])
    end_year = int(matches[1])
    result = []
    for movie in f1driverdb:
        if start_year <= get_year(movie) <= end_year:
            result.append(get_title(movie))
    return result



def title_before_year(matches: List[str]) -> List[str]:
    
    year = int(matches[0])
    result = []
    for movie in f1driverdb:
        if get_year(movie) < year:
            result.append(get_title(movie))
    return result


def title_after_year(matches: List[str]) -> List[str]:

    year = int(matches[0])
    result = []
    for movie in f1driverdb:
        if get_year(movie) > year:
            result.append(get_title(movie))
    return result


def director_by_title(matches: List[str]) -> List[str]:

    title = matches[0]
    result = []
    for movie in f1driverdb:
        if get_title(movie) == title:
            result.append(get_director(movie))
    return result


def title_by_director(matches: List[str]) -> List[str]:

    result = []
    director = matches[0]

    for movie in f1driverdb:
        if get_director(movie) == director:
            result.append(get_title(movie))
    return result


def actors_by_title(matches: List[str]) -> List[str]:

    result = []
    title = matches[0]
    for movie in f1driverdb:
        if get_title(movie) == title:
            result = get_actors(movie)
    return result


def year_by_title(matches: List[str]) -> List[int]:

    result = []
    title = matches[0]
    for movie in f1driverdb:
        if get_title(movie) == title:
            result.append(get_year (movie))
    return result


def title_by_actor(matches: List[str]) -> List[str]:
    
    actor = matches[0]
    result = []
    for movie in f1driverdb:
        if actor in get_actors(movie):
            result.append(get_title(movie))
    return result

def actor_by_director(matches:List[str]) -> List[str]:
    director = matches[0]
    result = []
    for movie in f1driverdb:
        if director in get_director(movie):
            result.append(get_actors(movie))
    return result


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt



pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what movies were made in _"), title_by_year),
    (str.split("what movies were made between _ and _"), title_by_year_range),
    (str.split("what movies were made before _"), title_before_year),
    (str.split("what movies were made after _"), title_after_year),

    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what movies did % appear"), title_by_actor),
    (str.split("in what year was % made"), year_by_title),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:

    for pat, act, in pa_list:
        print(f"pattern: {pat}, source: {src}, action: {act}")
        mat = match(pat, src)
        print(f"match: {mat}")

        if mat is not None:
            ans = act(mat)
            print(f"answer: {ans}")
            return ans if ans else ["No ansers"]
    return("I don't understand")

def query_loop() -> None:

    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


if __name__ == "__main__":
    assert isinstance(title_by_year(["1974"]), list), "title_by_year not returning a list"
    assert sorted(title_by_year(["1974"])) == sorted(
        ["amarcord", "chinatown"]
    ), "failed title_by_year test"
    assert isinstance(title_by_year_range(["1970", "1972"]), list), "title_by_year_range not returning a list"
    assert sorted(title_by_year_range(["1970", "1972"])) == sorted(
        ["the godfather", "johnny got his gun"]
    ), "failed title_by_year_range test"
    assert isinstance(title_before_year(["1950"]), list), "title_before_year not returning a list"
    assert sorted(title_before_year(["1950"])) == sorted(
        ["casablanca", "citizen kane", "gone with the wind", "metropolis"]
    ), "failed title_before_year test"
    assert isinstance(title_after_year(["1990"]), list), "title_after_year not returning a list"
    assert sorted(title_after_year(["1990"])) == sorted(
        ["boyz n the hood", "dead again", "the crying game", "flirting", "malcolm x"]
    ), "failed title_after_year test"
    assert isinstance(director_by_title(["jaws"]), list), "director_by_title not returning a list"
    assert sorted(director_by_title(["jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed director_by_title test"
    assert isinstance(title_by_director(["steven spielberg"]), list), "title_by_director not returning a list"
    assert sorted(title_by_director(["steven spielberg"])) == sorted(
        ["jaws"]
    ), "failed title_by_director test"
    assert isinstance(actors_by_title(["jaws"]), list), "actors_by_title not returning a list"
    assert sorted(actors_by_title(["jaws"])) == sorted(
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ]
    ), "failed actors_by_title test"
    assert sorted(actors_by_title(["movie not in database"])) == [], "failed actors_by_title not in database test"
    assert isinstance(year_by_title(["jaws"]), list), "year_by_title not returning a list"
    assert sorted(year_by_title(["jaws"])) == sorted(
        [1975]
    ), "failed year_by_title test"
    assert isinstance(title_by_actor(["orson welles"]), list), "title_by_actor not returning a list"
    assert sorted(title_by_actor(["orson welles"])) == sorted(
        ["citizen kane", "othello"]
    ), "failed title_by_actor test"
    
    
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["who", "directed", "jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "movies", "were", "made", "in", "2020"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"

    print("All tests passed!")