"""Small helper functions used across the project. Nothing fancy."""

import os
import json


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_json(path, default):
    """Load a JSON file, or return `default` if it doesn't exist / is broken."""
    if not os.path.exists(path):
        return default

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(path, data):
    """Write data to a JSON file, creating the parent folder if needed."""
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
