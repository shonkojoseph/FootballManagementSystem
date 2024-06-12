import click
from models.team import Team

def manage_teams():
    while True:
        click.echo("1. Create Team")
        click.echo("2. View All Teams")
        click.echo("3. Delete Team")
        click.echo("4. Back to Main Menu")
        choice = click.prompt("Select an option", type=int)
        if choice == 1:
            name = click.prompt("Enter team name")
            team = Team.create(name)
            click.echo(f"Created team: {team}")
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
