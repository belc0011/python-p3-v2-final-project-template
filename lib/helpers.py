# lib/helpers.py
from db.player import Player
from db.team import Team

def create_team():
    team = input("Enter the team name, or type 0 to exit: ").title()
    if team == "0":
        exit_program()
    coach = input("Enter name of coach: ").title()
    Team.create(team, coach)
    print("Team successfully created")
def players_by_team():
    ## prints list of players on team
    team = input("Enter team name: ").title()
    team_list = Player.find_by_team(team) ## method returns a list of player objects
    for team in team_list: ## cycles through list of player objects one by one
        if team[1] == team:
            print(team[0])

def print_all_teams():
    teams = Team.get_all()
    for (index, team) in enumerate(teams):
        print(f"{index + 1}. {team.name}")

def get_all_players(id):
    team = Team.find_by_id(id)
    players = Player.find_by_team(team.name)
    player_dict = {}
    for (index, player) in enumerate(players):
        print(f"{index + 1}. {player.name}")
        player_dict[index + 1] = player.name
    return player_dict
def exit_program():
    print("Goodbye!")
    exit()

def team_info_printer(id):
    team = Team.find_by_id(id)
    print(f"Menu for {team.name}")

def add_new_player(team_id):
    player_name = input("Enter player's name: ").title()
    jersey_number = int(input("Enter player's jersey number: "))
    team_name = Team.find_by_id(team_id).name
    Player.create(player_name, team_name, jersey_number)
    print("Player created!")

def coach_info(team_id):
    print(Team.find_by_id(team_id).coach)

def delete_player(name_list, index):
    player = Player.find_by_name(name_list[index])
    print(player)

