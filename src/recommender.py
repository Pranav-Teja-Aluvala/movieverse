"""
Recommendation system - no ML, just a lookup table I put together myself.
Checks the exact title first, then tries to match on language (so a
Telugu movie recommends other Telugu movies instead of random English
ones), and falls back to genre if neither of those hit.
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
    "rrr": ["Baahubali: The Beginning", "Pushpa: The Rise", "KGF: Chapter 1", "Kalki 2898 AD"],
    "pushpa: the rise": ["RRR", "KGF: Chapter 1", "Baahubali: The Beginning", "Salaar: Part 1 – Ceasefire"],
    "baahubali: the beginning": ["RRR", "KGF: Chapter 1", "Pushpa: The Rise", "Kalki 2898 AD"],
    "kgf: chapter 1": ["Baahubali: The Beginning", "RRR", "Kantara", "Pushpa: The Rise"],
    "3 idiots": ["Zindagi Na Milegi Dobara", "Dangal", "Queen", "Taare Zameen Par"],
    "dangal": ["3 Idiots", "Bhaag Milkha Bhaag", "Sultan", "Chak De! India"],
    "kantara": ["KGF: Chapter 1", "Ugramm", "Lucia", "Tumbbad"],
}

# curated by industry, used when a title isn't in the dict above but we
# at least know what language it's in
LANGUAGE_RECOMMENDATIONS = {
    "hindi": ["3 Idiots", "Dangal", "Zindagi Na Milegi Dobara", "Queen", "Andhadhun", "Gully Boy"],
    "telugu": ["Baahubali: The Beginning", "RRR", "Pushpa: The Rise", "Kalki 2898 AD", "Eega", "Ala Vaikunthapurramuloo"],
    "tamil": ["Vikram", "Master", "96", "Super Deluxe", "Asuran", "Jai Bhim"],
    "malayalam": ["Drishyam", "Kumbalangi Nights", "Premam", "The Great Indian Kitchen", "Ayyappanum Koshiyum"],
    "kannada": ["KGF: Chapter 1", "KGF: Chapter 2", "Kantara", "Ugramm", "Lucia"],
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
    the movie's language, then falls back to matching on genre."""

    title = movie_data.get("Title", "").lower()
    if title in MOVIE_RECOMMENDATIONS:
        return MOVIE_RECOMMENDATIONS[title]

    language_string = movie_data.get("Language", "")
    languages = [l.strip().lower() for l in language_string.split(",") if l.strip()]

    for language in languages:
        if language in LANGUAGE_RECOMMENDATIONS:
            return LANGUAGE_RECOMMENDATIONS[language]

    genre_string = movie_data.get("Genre", "")
    genres = [g.strip().lower() for g in genre_string.split(",") if g.strip()]

    for genre in genres:
        if genre in GENRE_RECOMMENDATIONS:
            return GENRE_RECOMMENDATIONS[genre]

    return []
