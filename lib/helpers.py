# lib/helpers.py
from models.player import Player
from models.team import Team
from models.division import Division

def create_team(division_id=None):
    team = input("Enter the team name, or type 0 to exit: ").title()
    if team == "0":
        exit_program()
    coach = input("Enter name of coach: ").title()
    division = Division.find_by_id(division_id).name
    Team.create(team, coach, division)
    print("Team successfully created")

def print_all_teams(division_id):
    teams = Team.get_all()
    at_least = False
    for (index, team) in enumerate(teams):
        if team.division_id == division_id:
            print(f"{index + 1}. {team.name}")
            at_least = True
    if (not at_least):
        team_print_choice = int(input("No teams currently in this division. Press 1 to add a new team or 0 to exit: "))
        if team_print_choice == 0:
            exit_program()
        elif team_print_choice == 1:
            create_team(division_id)
        else:
            print("Invalid selection, exiting program")
            exit_program()
            

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
    team_found = False
    if (team):
        print(f"Menu for {team.name}")
        team_found = True
        return id
    else:
        while (not team_found):
            team_id = int(input("Invalid choice, please select a number from the list above, or enter 0 to exit the program> "))
            if team_id == 0:
                exit_program()
            else:
                team = Team.find_by_id(team_id)
                if (team):
                    print(f"Menu for {team.name}")
                    team_found = True
                    return team_id

def division_info_printer(division_id):
    division = Division.find_by_id(division_id)
    division_found = False
    if (division):
        print(f"Menu for {division.name}")
        division_found = True
        return division_id
    else:
        while (not division_found):
            division_id = int(input("Invalid choice, please select a number from the list above, or enter 0 to exit the program> "))
            if division_id == 0:
                exit_program()
            else:
                division = Division.find_by_id(division_id)
                if (division):
                    print(f"Menu for {division.name}")
                    division_found = True
                    return division_id
def add_new_player(team_id):
    player_name = input("Enter player's first and last name: ").title()
    jersey_number = int(input("Enter player's jersey number: "))
    team_name = Team.find_by_id(team_id).name
    Player.create(player_name, team_name, jersey_number)
    print("Player created!")

def coach_info(team_id):
    print(Team.find_by_id(team_id).coach)

def set_coach(team_id):
    team = Team.find_by_id(team_id)
    new_coach = input("Enter name of new coach: ")
    team.coach = new_coach.title()
    Team.update(team)
    print("Coach successfully updated!")

def delete_player(name_list, index):
    player = Player.find_by_name(name_list[index])
    Player.delete(player)
    print("Player successfully deleted!")

def update_player(name_list, index):
    player = Player.find_by_name(name_list[index])
    new_name = input("Enter the updated name, or press 0 to exit: ")
    if new_name == "0":
        exit_program()
    else:
        player.name = new_name.title()
        Player.update(player)
        print("Player name successfully updated!")

def team_size(team_id):
    team = Team.find_by_id(team_id)
    player_list = Team.players(team)
    print(f"There is/are {len(player_list)} total player(s) on {team.name}")

def player_search():
    player_name = input("Enter the player's first and last name: ").title()
    player_list = Player.get_all()
    player_found = False
    for player in player_list:
        if player.name == player_name:
            print(f"{player_name} plays for {player.team}")
            player_found = True
    if (not player_found):
        print("Player not found. Please check the spelling and ensure you include the first and last name separated by a space.")

def print_all_divisions():
    divisions = Division.get_all()
    for (index, division) in enumerate(divisions):
        print(f"{index + 1}. {division.name}")

def create_division():
    name = input("Enter the division name, or type 0 to exit: ").title()
    if name == "0":
        exit_program()
    Division.create(name)
    print("Division successfully created")

def team_search():
    team_name = input("Enter the team name: ").title()
    team_list = Team.get_all()
    team_found = False
    for team in team_list:
        if team.name == team_name:
            print(f"{team_name} is in the {team.division} Division")
            team_found = True
    if (not team_found):
        print("Team not found. Please check the spelling and try again.")