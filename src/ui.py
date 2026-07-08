"""All terminal UI components for MovieVerse."""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.box import ROUNDED

console = Console()

PRIMARY = "gold3"
SECONDARY = "grey70"
TITLE = "bold white"
HEADER = "bold gold3"
TABLE_HEADER = "bold gold3"
SUCCESS = "green3"
ERROR = "red3"
BORDER = "gold3"


def show_banner():
    console.print()
    console.print(
        Panel.fit(
            f"[{TITLE}]MOVIEVERSE[/]\n"
            f"[{SECONDARY}]Terminal Movie Explorer[/]",
            border_style=BORDER,
            padding=(1, 4),
        )
    )


def show_menu():
    console.print()

    console.print(f"[bold {PRIMARY}]1[/]  Search Movie")
    console.print(f"[bold {PRIMARY}]2[/]  Favorites")
    console.print(f"[bold {PRIMARY}]3[/]  Search History")
    console.print(f"[bold {PRIMARY}]4[/]  Recently Viewed")
    console.print(f"[bold {PRIMARY}]5[/]  Random Movie")
    console.print(f"[bold {PRIMARY}]6[/]  Exit")

    console.print()

    return Prompt.ask(
        "Choose an option",
        choices=["1", "2", "3", "4", "5", "6"],
    )


def display_movie(movie):
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
    )

    table.add_column(style=TABLE_HEADER, no_wrap=True)
    table.add_column(style="white")

    fields = [
        ("Year", movie.get("Year")),
        ("Genre", movie.get("Genre")),
        ("Runtime", movie.get("Runtime")),
        ("IMDb Rating", movie.get("imdbRating")),
        ("Director", movie.get("Director")),
        ("Actors", movie.get("Actors")),
        ("Language", movie.get("Language")),
        ("Country", movie.get("Country")),
        ("Awards", movie.get("Awards")),
        ("Plot", movie.get("Plot")),
    ]

    for label, value in fields:
        table.add_row(label, value or "N/A")

    console.print(
        Panel(
            table,
            title=f"[bold white]{movie.get('Title', 'Unknown')}[/]",
            border_style=BORDER,
            box=ROUNDED,
            padding=(1, 2),
        )
    )


def show_recommendations(recommendations):
    if not recommendations:
        console.print(f"[{SECONDARY}]No recommendations available.[/]")
        return

    console.print()
    console.print(f"[{HEADER}]Recommendations[/]\n")

    for movie in recommendations:
        console.print(f"  • {movie}")


def show_history_table(history, title="Search History"):
    if not history:
        console.print(f"[{SECONDARY}]Nothing here yet.[/]")
        return

    table = Table(
        title=f"[{HEADER}]{title}[/]",
        box=ROUNDED,
        header_style=TABLE_HEADER,
    )

    table.add_column("Title", style="white")
    table.add_column("Year")
    table.add_column("Genre")
    table.add_column("IMDb Rating")

    for entry in history:
        table.add_row(
            entry["title"],
            entry["year"],
            entry["genre"],
            entry["imdb_rating"],
        )

    console.print(table)


def show_favorites_table(favorites):
    if not favorites:
        console.print(f"[{SECONDARY}]No favorites saved yet.[/]")
        return

    table = Table(
        title=f"[{HEADER}]Your Favorites[/]",
        box=ROUNDED,
        header_style=TABLE_HEADER,
    )

    table.add_column("Title", style="white")
    table.add_column("Year")
    table.add_column("Genre")
    table.add_column("IMDb Rating")

    for entry in favorites:
        table.add_row(
            entry["title"],
            entry["year"],
            entry["genre"],
            entry["imdb_rating"],
        )

    console.print(table)


def error_message(message):
    console.print(f"[bold {ERROR}]Error:[/] {message}")


def success_message(message):
    console.print(f"[bold {SUCCESS}]{message}[/]")