"""Keeps track of search history and favorited movies, both saved as JSON
so they persist between runs."""

from src.utils import load_json, save_json

HISTORY_FILE = "data/history.json"
FAVORITES_FILE = "data/favorites.json"


class HistoryManager:
    def __init__(self):
        self.history = load_json(HISTORY_FILE, [])
        self.favorites = load_json(FAVORITES_FILE, [])

    def add_search(self, movie_data):
        entry = {
            "title": movie_data.get("Title", "Unknown"),
            "year": movie_data.get("Year", "N/A"),
            "genre": movie_data.get("Genre", "N/A"),
            "imdb_rating": movie_data.get("imdbRating", "N/A"),
        }

        # don't log the exact same movie twice in a row (happens if someone
        # searches, then just hits search again by mistake)
        if self.history and self.history[-1]["title"] == entry["title"]:
            return

        self.history.append(entry)
        save_json(HISTORY_FILE, self.history)

    def get_recent(self, count=5):
        return list(reversed(self.history[-count:]))

    def get_all(self):
        return self.history

    def add_favorite(self, movie_data):
        title = movie_data.get("Title", "Unknown")

        already_saved = any(fav["title"] == title for fav in self.favorites)
        if already_saved:
            return False

        entry = {
            "title": title,
            "year": movie_data.get("Year", "N/A"),
            "genre": movie_data.get("Genre", "N/A"),
            "imdb_rating": movie_data.get("imdbRating", "N/A"),
        }
        self.favorites.append(entry)
        save_json(FAVORITES_FILE, self.favorites)
        return True

    def get_favorites(self):
        return self.favorites
