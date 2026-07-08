"""All the terminal output lives here, built with Rich. Keeping this
separate from main.py so the actual app logic doesn't get buried in
print statements."""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]CINESCOPE[/bold cyan]\n[dim]terminal movie explorer[/dim]",
            border_style="cyan",
        )
    )


def show_menu():
    console.print("\n[bold]1[/bold]  Search Movie")
    console.print("[bold]2[/bold]  Favorites")
    console.print("[bold]3[/bold]  Search History")
    console.print("[bold]4[/bold]  Recently Viewed")
    console.print("[bold]5[/bold]  Random Movie")
    console.print("[bold]6[/bold]  Exit\n")
    return Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6"])


def display_movie(movie):
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(style="bold cyan", no_wrap=True)
    table.add_column()

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
        table.add_row(label, value if value else "N/A")

    console.print(
        Panel(table, title=f"[bold green]{movie.get('Title', 'Unknown')}[/bold green]", border_style="green")
    )


def show_recommendations(recommendations):
    if not recommendations:
        console.print("[dim]Couldn't find any recommendations for this one.[/dim]")
        return

    console.print("\n[bold yellow]You might also like:[/bold yellow]")
    for movie in recommendations:
        console.print(f"  • {movie}")


def show_history_table(history, title="Search History"):
    if not history:
        console.print("[dim]Nothing here yet.[/dim]")
        return

    table = Table(title=title)
    table.add_column("Title", style="cyan")
    table.add_column("Year")
    table.add_column("Genre")
    table.add_column("IMDb Rating")

    for entry in history:
        table.add_row(entry["title"], entry["year"], entry["genre"], entry["imdb_rating"])

    console.print(table)


def show_favorites_table(favorites):
    if not favorites:
        console.print("[dim]No favorites saved yet.[/dim]")
        return

    table = Table(title="Your Favorites")
    table.add_column("Title", style="magenta")
    table.add_column("Year")
    table.add_column("Genre")
    table.add_column("IMDb Rating")

    for entry in favorites:
        table.add_row(entry["title"], entry["year"], entry["genre"], entry["imdb_rating"])

    console.print(table)


def error_message(message):
    console.print(f"[bold red]Error:[/bold red] {message}")


def success_message(message):
    console.print(f"[bold green]{message}[/bold green]")
