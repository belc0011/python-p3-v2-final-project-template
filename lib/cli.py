# lib/cli.py

from helpers import (
    exit_program,
    create_team,
    team_info_printer,
    players_by_team,
    print_all_teams,
    get_all_players,
    add_new_player,
    coach_info,
    delete_player,
    update_player
)
from db.player import Player
from db.team import Team

def main():
    while True:
        menu1()
        choice1 = int(input("> "))
        if choice1 == 0:
            exit_program()
        elif choice1 == 1:
            print_all_teams()
            menu2()
            choice2 = int(input("> ")) ##choice2 should hold team id
            if choice2 == 0:
                exit_program()
            else:
                team_info_printer(choice2)
                menu3()
                choice3 = int(input("> "))
                if choice3 == 0:
                    exit_program()
                elif choice3 == 1:
                    players = get_all_players(choice2)
                    if(players):
                        team_info_printer(choice2)
                        menu4()
                        choice4 = int(input("> "))
                        if choice4 == 0:
                            exit_program()
                        elif choice4 == 1:
                            choice5 = int(input("Select the number for the player to delete, or press 0 to exit: "))
                            if choice5 == 0:
                                exit_program()
                            else:
                                delete_player(players, choice5)
                        elif choice4 == 2:
                            choice5 = int(input("Select the number for the player to update, or press 0 to exit: "))
                            if choice5 == 0:
                                exit_program()
                            else:
                                update_player(players, choice5)
                    else:
                        print("This team currently has no players.")
                elif choice3 == 2:
                    add_new_player(choice2)
                elif choice3 == 3:
                    coach_info(choice2)
        elif choice1 == 2:
            create_team()
        else:
            print("Invalid choice")
def menu1():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List available teams")
    print("2. Add a team")

def menu2():
    print("Select the number for the team to diplay, or press 0 to exit the program: ")

def menu3():
    print("1. List current players on team")
    print("2. Add a new player to the team")
    print("3. List current coach info")
    print("0. Exit the program")

def menu4():
    print("1. Delete Player")
    print("2. Update player name")
    print("0. Exit the program")

if __name__ == "__main__":
    main()
