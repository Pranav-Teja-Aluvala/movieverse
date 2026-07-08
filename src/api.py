"""
Handles all communication with the OMDb API.
Everything else in the app just calls search_movie() and gets a dict back.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"


class OMDbError(Exception):
    """Raised whenever something goes wrong talking to OMDb (bad key, no
    internet, movie not found, etc). Keeps the calling code from having
    to know about requests or JSON errors directly."""
    pass


def search_movie(title):
    """Look up a single movie by title and return the full OMDb response
    as a dict. Raises OMDbError if anything goes wrong."""

    if not API_KEY:
        raise OMDbError(
            "No OMDb API key found. Copy .env.example to .env and add your key."
        )

    params = {
        "apikey": API_KEY,
        "t": title,
        "plot": "full",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise OMDbError("Request timed out. Check your internet connection.")
    except requests.exceptions.RequestException as e:
        raise OMDbError(f"Couldn't reach OMDb: {e}")

    data = response.json()

    # OMDb doesn't use HTTP error codes for "movie not found", it just
    # sends Response: "False" with an Error message. Annoying but ok.
    if data.get("Response") == "False":
        raise OMDbError(data.get("Error", "Movie not found."))

    return data
