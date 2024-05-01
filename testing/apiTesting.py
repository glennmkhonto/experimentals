import requests

def api_testing():
    url = "https://swapi.dev/api/films/"

    try:
        response = requests.get(url)
        response_data = response.json()

        if response.status_code == 200:
            movie_count = len(response_data['results'])
            assert movie_count == 6, f"Expected 6 movies, but found {movie_count} movies."

            print("Movies count assertion successful.")
            third_movie_url = response_data['results'][2]['url']
            third_movie_response = requests.get(third_movie_url)
            third_movie_data = third_movie_response.json()
            director = third_movie_data['director']
            assert director == 'Richard Marquand', f"The director of the third movie is not 'Richard Marquand'. Director found: {director}"

            print("Director assertion successful.")
            fifth_movie_url = response_data['results'][4]['url']
            fifth_movie_response = requests.get(fifth_movie_url)
            fifth_movie_data = fifth_movie_response.json()

            producers = fifth_movie_data['producer']
            assert 'Gary Kurtz' not in producers and 'George Lucas' not in producers, f"Gary Kurtz and/or George Lucas found in producers: {producers}"
            print("done asserting for producers")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print("An error occurred:", e)

api_testing()