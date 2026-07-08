"""
Recommendation system - no ML, just a lookup table I put together myself.
Some movies get specific recommendations (stuff I know is actually similar),
and everything else falls back to a genre match.
"""

MOVIE_RECOMMENDATIONS = {
    "interstellar": ["Arrival", "The Martian", "Gravity", "Inception"],
    "inception": ["Shutter Island", "The Prestige", "Tenet", "Memento"],
    "the dark knight": ["Joker", "Batman Begins", "The Prestige", "Se7en"],
    "the matrix": ["Blade Runner 2049", "Equilibrium", "Tron: Legacy", "Ghost in the Shell"],
    "titanic": ["The Notebook", "Pearl Harbor", "A Walk to Remember", "Romeo + Juliet"],
    "the shawshank redemption": ["The Green Mile", "Fight Club", "American History X", "Se7en"],
    "avengers: endgame": ["Avengers: Infinity War", "Guardians of the Galaxy", "Iron Man", "Thor: Ragnarok"],
    "parasite": ["Snowpiercer", "Burning", "The Handmaiden", "Memories of Murder"],
    "whiplash": ["Black Swan", "The Social Network", "La La Land", "Birdman"],
}

# fallback if the exact title isn't in the dict above
GENRE_RECOMMENDATIONS = {
    "sci-fi": ["Interstellar", "Arrival", "Blade Runner 2049", "Ex Machina"],
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "drama": ["Forrest Gump", "The Shawshank Redemption", "A Beautiful Mind", "Good Will Hunting"],
    "comedy": ["Superbad", "The Hangover", "Step Brothers", "Bridesmaids"],
    "horror": ["Hereditary", "Get Out", "A Quiet Place", "The Conjuring"],
    "romance": ["Titanic", "The Notebook", "La La Land", "Pride & Prejudice"],
    "animation": ["Spirited Away", "Coco", "Up", "Inside Out"],
    "thriller": ["Se7en", "Gone Girl", "Prisoners", "Shutter Island"],
    "crime": ["The Godfather", "Goodfellas", "Pulp Fiction", "The Departed"],
}


def get_recommendations(movie_data):
    """Return a short list of similar movies. Checks title first, then
    falls back to matching on genre."""

    title = movie_data.get("Title", "").lower()
    if title in MOVIE_RECOMMENDATIONS:
        return MOVIE_RECOMMENDATIONS[title]

    genre_string = movie_data.get("Genre", "")
    genres = [g.strip().lower() for g in genre_string.split(",") if g.strip()]

    for genre in genres:
        if genre in GENRE_RECOMMENDATIONS:
            return GENRE_RECOMMENDATIONS[genre]

    return []
