import requests
import csv

API_KEY = "da7ce042"  # Replace with your working API key
BASE_URL = "http://www.omdbapi.com/"

def get_movie_titles():
    titles = input("Enter movie/series names (comma-separated): ")
    return [title.strip() for title in titles.split(",") if title.strip()]

def fetch_movie_data(title):
    params = {
        "t": title,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return {
                "Title": data.get("Title", "N/A"),
                "Year": data.get("Year", "N/A"),
                "Genre": data.get("Genre", "N/A"),
                "Director": data.get("Director", "N/A"),
                "Actors": data.get("Actors", "N/A"),
                "Plot": data.get("Plot", "N/A"),
                "IMDB Rating": data.get("imdbRating", "N/A")
            }
        else:
            print(f"Not found: {title}")
    else:
        print(f"Error for {title}: Status code {response.status_code}")
    return None

def save_to_csv(movies, filename="movies.csv"):
    if not movies:
        print("No data to save.")
        return

    keys = movies[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(movies)

    print(f"All movie data saved to {filename}")

def main():
    titles = get_movie_titles()
    movie_data = []

    for title in titles:
        data = fetch_movie_data(title)
        if data:
            movie_data.append(data)
            print(f"🎬 {data['Title']} ({data['Year']})")

    save_to_csv(movie_data)

if __name__ == "__main__":
    main()
