import click
from models.team import Team
from models.player import Player

@click.group()
def cli():
    pass

@cli.command()
def main_menu():
    while True:
        click.echo("1. Manage Teams")
        click.echo("2. Manage Players")
        click.echo("3. Exit")
        choice = click.prompt("Select an option", type=int)
        if choice == 1:
            manage_teams()
        elif choice == 2:
            manage_players()
        elif choice == 3:
            break

if __name__ == "__main__":
    cli()
