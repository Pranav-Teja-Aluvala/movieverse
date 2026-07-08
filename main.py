"""
MovieVerse - a terminal movie explorer built around the OMDb API.

Run this after setting up your .env file with an OMDB_API_KEY.
"""

import random

from src import api, ui
from src.history import HistoryManager
from src.recommender import get_recommendations

# pool of movies for the "random pick" feature - just some favorites
RANDOM_MOVIE_POOL = [
    "The Shawshank Redemption", "Inception", "Interstellar", "The Dark Knight",
    "Parasite", "Whiplash", "The Matrix", "Gladiator", "Fight Club",
    "The Prestige", "Se7en", "Coco", "Spirited Away", "La La Land",
    "Get Out", "Mad Max: Fury Road", "Titanic", "Forrest Gump",
]


def search_movie_flow(history_manager):
    title = ui.console.input("[bold]Enter a movie title:[/bold] ").strip()
    if not title:
        ui.error_message("You didn't type anything.")
        return

    try:
        movie = api.search_movie(title)
    except api.OMDbError as e:
        ui.error_message(str(e))
        return

    ui.display_movie(movie)
    history_manager.add_search(movie)
    ui.show_recommendations(get_recommendations(movie))

    choice = ui.console.input("\nAdd to favorites? (y/n): ").strip().lower()
    if choice == "y":
        added = history_manager.add_favorite(movie)
        if added:
            ui.success_message("Added to favorites!")
        else:
            ui.console.print("[dim]Already in your favorites.[/dim]")


def random_movie_flow(history_manager):
    title = random.choice(RANDOM_MOVIE_POOL)

    try:
        movie = api.search_movie(title)
    except api.OMDbError as e:
        ui.error_message(str(e))
        return

    ui.display_movie(movie)
    history_manager.add_search(movie)
    ui.show_recommendations(get_recommendations(movie))


def main():
    history_manager = HistoryManager()
    ui.show_banner()

    while True:
        choice = ui.show_menu()

        if choice == "1":
            search_movie_flow(history_manager)
        elif choice == "2":
            ui.show_favorites_table(history_manager.get_favorites())
        elif choice == "3":
            ui.show_history_table(history_manager.get_all())
        elif choice == "4":
            ui.show_history_table(history_manager.get_recent(), title="Recently Viewed")
        elif choice == "5":
            random_movie_flow(history_manager)
        elif choice == "6":
            ui.console.print("\n[bold cyan]Thanks for using MovieVerse. See ya![/bold cyan]")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting MovieVerse.")
