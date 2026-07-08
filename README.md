# MovieVerse 🎬

A terminal-based movie explorer and recommendation system I built to get more
comfortable working with external APIs, JSON storage, and building an actual
usable CLI (instead of just print statements everywhere). It uses the OMDb
API for movie data and Rich for a cleaner-looking terminal.

## What it does

- **Search Movie** — look up any movie by title and see its year, genre,
  runtime, IMDb rating, director, cast, language, country, plot, and awards.

- **Recommendations** — after a search, get 4-5 similar movies based on a
  genre/title mapping I put together (no ML, just a lookup table).

- **Favorites** — bookmark movies you like, saved to `data/favorites.json`.

- **Search History** — every movie you look up gets logged to
  `data/history.json` so you can look back at it later.

- **Recently Viewed** — quick view of your last 5 searches.

- **Random Movie** — picks something from a small internal list and pulls
  its details, for when you don't know what to search.

## Project structure

```
movieverse/
├── assets/
├── data/
│   ├── history.json
│   └── favorites.json
├── src/
│   ├── api.py          # talks to the OMDb API
│   ├── history.py       # handles history + favorites (json read/write)
│   ├── recommender.py    # genre/title based recommendation lookup
│   ├── ui.py             # all the Rich terminal output
│   └── utils.py          # small json helper functions
├── main.py
├── requirements.txt
├── .gitignore
└── .env                 # contains the API key
```

## Tech used

- Python 3
- `requests` — for hitting the OMDb API
- `rich` — for the terminal tables/panels/menu
- `python-dotenv` — for loading the API key from `.env`
- JSON — for storing history and favorites locally, no database needed

## Notes / things I'd add later

- Right now the recommendation system is a hardcoded dictionary. It works
  fine for common movies but obviously doesn't scale — a genre-similarity
  score or hitting a second API for "similar titles" would be the next step.
- Favorites and history are stored per-machine (just local JSON files), so
  there's no multi-user support. Wasn't really the point of this project.
- Would be cool to add a "compare two movies" feature at some point.

## Why I built this

Wanted a project that actually used a real API instead of a toy dataset,
and forced me to think about structuring code into modules instead of
dumping everything into one script. Also just wanted an excuse to use
Rich properly.
