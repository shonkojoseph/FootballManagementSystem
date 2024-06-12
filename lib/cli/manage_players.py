import click
from models.player import Player

def manage_players():
    while True:
        click.echo("1. Add Player")
        click.echo("2. View All Players")
        click.echo("3. Delete Player")
        click.echo("4. Back to Main Menu")
        choice = click.prompt("Select an option", type=int)
        if choice == 1:
            name = click.prompt("Enter player name")
            team_id = click.prompt("Enter team ID")
            player = Player.create(name, team_id)
            click.echo(f"Added player: {player}")
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
