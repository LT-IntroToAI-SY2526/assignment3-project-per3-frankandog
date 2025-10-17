from main import f1driverdb
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "movie" (a tuple)
def get_driver(main: Tuple[str, str, List[str]]) -> str:
    return main[0]


def get_country(main: Tuple[str, str, List[str]]) -> str:
    return main[1]


def get_sponsors(main: Tuple[str, str, List[str]]) -> List[str]:
    return main[2]



def driver_by_country(matches: List[str]) -> List[str]:

    country = matches[0]
    result = []
    for driver in f1driverdb:
        if get_country(driver) == country:
            result.append(get_driver(driver))
    return result


def country_by_driver(matches: List[str]) -> List[str]:

    driver = matches[1]
    result = []
    for country in f1driverdb:
        if get_driver(country) == driver:
            result.append(get_country(country))
    return result


def sponsors_by_driver(matches: List[str]) -> List[str]:

    driver = matches[0]
    result = []
    for sponsors in f1driverdb:
        if get_driver(sponsors) == driver:
            result = get_sponsors(sponsors)
    return result


def sponsor_by_country(matches: List[str]) -> List[str]:

    country = matches[0]
    result = []
    for sponsor in f1driverdb:
        if get_country(sponsor) == country:
            result.append(get_sponsors(sponsor))
    return result

def driver_by_sponsor(matches: List[str]) -> List[str]:

    sponsor = matches[0]
    result = []
    for driver in f1driverdb:
        if get_sponsors(driver) == sponsor:
            result.append(get_driver(driver))
    return result

def country_by_sponsor(matches: List[str]) -> List[str]:

    sponsor = matches[0]
    result = []
    for country in f1driverdb:
        if get_sponsors(country) == sponsor:
            result.append(get_country(country))
    return result


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt



pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what drivers race for _"), driver_by_country),
    (str.split("what country has _ driven for"), country_by_driver),
    (str.split("What sponsors has _ had"), sponsors_by_driver),
    (str.split("What sponsors has the nation _ had"), sponsor_by_country),
    (str.split("who drove with these _"), driver_by_sponsor),
    (str.split("What sponsors supported _"), country_by_sponsor),

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

    print("Welcome to the F1 Driver database!\n")
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