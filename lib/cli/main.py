import click
from models.team import Team
from models.player import Player
from utils.db import create_tables

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    create_tables()
    click.echo("Initialized the database.")

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

def manage_teams():
    while True:
        click.echo("1. Create Team")
        click.echo("2. View All Teams")
        click.echo("3. Delete Team")
        click.echo("4. Back to Main Menu")
        choice = click.prompt("Select an option", type=int)
        if choice == 1:
            name = click.prompt("Enter team name")
            Team.create(name)
            click.echo(f"Created team: {name}")
        elif choice == 2:
            teams = Team.get_all()
            for team in teams:
                click.echo(team)
        elif choice == 3:
            team_id = click.prompt("Enter team ID to delete", type=int)
            Team.delete(team_id)
            click.echo(f"Deleted team with ID: {team_id}")
        elif choice == 4:
            break

def manage_players():
    while True:
        click.echo("1. Add Player")
        click.echo("2. View All Players")
        click.echo("3. Delete Player")
        click.echo("4. Back to Main Menu")
        choice = click.prompt("Select an option", type=int)
        if choice == 1:
            name = click.prompt("Enter player name")
            team_id = click.prompt("Enter team ID", type=int)
            Player.create(name, team_id)
            click.echo(f"Added player: {name}")
        elif choice == 2:
            players = Player.get_all()
            for player in players:
                click.echo(player)
        elif choice == 3:
            player_id = click.prompt("Enter player ID to delete", type=int)
            Player.delete(player_id)
            click.echo(f"Deleted player with ID: {player_id}")
        elif choice == 4:
            break

if __name__ == "__main__":
    cli.add_command(main_menu)
    cli()
