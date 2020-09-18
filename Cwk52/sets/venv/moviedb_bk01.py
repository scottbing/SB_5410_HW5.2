import requests
FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
CREDITS_LIST_PATH ="http://api.themoviedb.org/3/movie"
RELEASE_DATE = "1990-01-01"
BACON_ID = "4724"       # Kevin Bacon
PAUL_ID = "781"         # Paul
SCARLETT_ID = "1245"    # Scarlett Johansson
BRADLEY_ID = "51329"    # Bradley Cooper
JENNIFER_ID = "72129"   # Jennifer Lawrence
WHALB_ID = "13240"      # Mark Whalberg
Chris_ID = "16828"      # Chis Evans
TOM_ID = "31"           # Tom Hanks


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

    print("film_set: ", film_set)
    return film_set


#end def data_to_set(data):"

def get_cast_list(film_id):
    url = CREDITS_LIST_PATH + "/" + film_id + "/credits"
    params = {"api_key":API_KEY}
    r = requests.get(url=url, params=params)
    data = r.json()
    return data
#end def get_cast_list(film_id):

def main():
    bacon_data = get_film_list(BACON_ID)
    bacon_films = data_to_set(bacon_data)
    print("Kevin Bacon films since", RELEASE_DATE, ":", bacon_films)

    bradley_data = get_film_list(BRADLEY_ID)
    print("Bradley: ", bradley_data)
    bradley_films = data_to_set(bradley_data)
    print("Bradley Cooper films since", RELEASE_DATE, ":", bradley_films)

    lawrence_data = get_film_list(JENNIFER_ID)
    print("Bradley: ", lawrence_data)
    lawrence_films = data_to_set(lawrence_data)
    print("Jennifer Lawrence films since", RELEASE_DATE, ":", lawrence_films)

    # ### get credits data for a film id and take out cast
    # cast = get_cast_list("514593")['cast']
    # person = cast[0]
    # print(str(person["id"]) + " " + person["name"])

#end def main():

if __name__ == '__main__':
    main()
