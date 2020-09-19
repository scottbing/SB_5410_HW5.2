import requests

FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
CREDITS_LIST_PATH ="http://api.themoviedb.org/3/movie"
RELEASE_DATE = "2000-01-01"
BACON_ID = "4724"       # Kevin Bacon
PAUL_ID = "781"
BACON_ID = "4724"       # Kevin Bacon
PAUL_ID = "781"         #
SCARLETT_ID = "1245"    # Scarlett Johansson
BRADLEY_ID = "51329"    # Bradley Cooper
JENNIFER_ID = "72129"   # Jennifer Lawrence
WHALB_ID = "13240"      # Mark Whalberg
CHRIS_ID = "16828"      # Chis Evans
TOM_ID = "31"           # Tom Hanks
KATE_ID = "11661"       # Kate Hudson
MATTHEW_ID = "10297"    # "Matthew McConaughey
JOHNNY_ID = "85"        # Johnny Depp
ADAM_ID = "19292"       # Adam Sandler
SETH_ID = "19274"       # Seth Rogen
EMMA_ID = "53693"       # Emma Stone

ID2NAME = {
    "4724"  : "Kevin Bacon",
    "1245"  : "Scarlett Johansson",
    "51329" : "Bradley Cooper",
    "72129" : "Jennifer Lawrence",
    "13240" : "Mark Whalberg",
    "16828" : "Chis Evans",
    "31"    : "Tom Hanks",
    "11661" : "Kate Hudson",
    "10297" : "Matthew McConaughey",
    "85"    : "Johnny Depp",
    "19292" : "Adam Sandler",
    "19274" : "Seth Rogen",
    "53693" : "Emma Stone"
}

API_KEY = "380c3a8372deba596a494c0912183d65"

def get_film_list(actor_id):
    params = {"api_key":API_KEY, "with_people":actor_id,
              "primary_release_date.gte": RELEASE_DATE}

    # print(FILM_LIST_PATH + "?api_key=" +API_KEY + "&with_people="+ actor_id +
    #       "&primary_release_date.gte=" + RELEASE_DATE)
    r = requests.get(url = FILM_LIST_PATH, params = params)

    data = r.json()
    return data
#end def get_film_list(actor_id):

def data_to_set(data):
    film_set = set()

    for res in data['results']: #For each element in results array
        film_set.add(res['title'])

    #print("film_set: ", film_set)
    return film_set


#end def data_to_set(data):"

def get_cast_list(film_id):
    url = CREDITS_LIST_PATH + "/" + film_id + "/credits"
    params = {"api_key":API_KEY}
    r = requests.get(url=url, params=params)
    data = r.json()
    return data
#end def get_cast_list(film_id):

def getResults(left, right):
    left_data = get_film_list(left)
    left_films = data_to_set(left_data)

    right_data = get_film_list(right)
    right_films = data_to_set(right_data)

    return(left_films.intersection(right_films))

#end def main():

if __name__ == '__main__':
    main()
