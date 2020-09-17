import requests
FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
RELEASE_DATE = "2016-01-01"
BACON_ID = "4724"
PAUL_ID = "781"
WHALB_ID = "13240"
API_KEY = "380c3a8372deba596a494c0912183d65"

def get_film_list(actor_id):
    params = {"api_key":API_KEY, "with_people":actor_id,
              "primary_release_date.gte": RELEASE_DATE}

    print(FILM_LIST_PATH + "?api_key=" +API_KEY + "&with_people="+ actor_id +
          "&primary_release_date.gte=" + RELEASE_DATE)
    r = requests.get(url = FILM_LIST_PATH, params = params)

    data = r.json()
    return data
#end def get_film_list(actor_id):

def main():
    bacon_films = get_film_list(BACON_ID)
    print(bacon_films)
#end def main():

if __name__ == '__main__':
    main()
