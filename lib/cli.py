# lib/cli.py

from helpers import (
    exit_program,
    create_team,
    team_info_printer,
    print_all_teams,
    get_all_players,
    add_new_player,
    coach_info,
    delete_player,
    update_player,
    set_coach,
    team_size,
    player_search,
    print_all_divisions,
    create_division,
    team_search,
    division_info_printer
)
from models.player import Player
from models.team import Team

def main():
    while True:
        menu1()
        choice1 = int(input("> ")) 
        if choice1 == 0:
            exit_program()
        elif choice1 == 1:
            print_all_divisions()
            division_id = int(input("Select the number next to the division in the list: "))
            division_info_printer(division_id)
            menu2()
            choice2 = int(input("> "))
            if choice2 == 0:
                exit_program()
            elif choice2 == 1:
                print_all_teams(division_id)
                menu3()
                choice3 = int(input("> ")) ##choice3 holds team id
                if choice3 == 0:
                    exit_program()
                else:
                    choice3 = team_info_printer(choice3)
                    menu4()
                    choice4 = int(input("> "))
                    if choice4 == 0:
                        exit_program()
                    elif choice4 == 1:
                        players = get_all_players(choice3)
                        if(players):
                            team_info_printer(choice3)
                            menu5()
                            choice5 = int(input("> "))
                            if choice5 == 0:
                                exit_program()
                            elif choice5 == 1:
                                choice6 = int(input("Select the number for the player to delete, or press 0 to exit: "))
                                if choice6 == 0:
                                    exit_program()
                                else:
                                    delete_player(players, choice6)
                            elif choice5 == 2:
                                choice6 = int(input("Select the number for the player to update, or press 0 to exit: "))
                                if choice6 == 0:
                                    exit_program()
                                else:
                                    update_player(players, choice6)
                            else:
                                print("Invalid choice")
                        else:
                            print("This team currently has no players.")
                    elif choice4 == 2:
                        add_new_player(choice3)
                    elif choice4 == 3:
                        coach_info(choice3)
                    elif choice4 == 4:
                        set_coach(choice3)
                    elif choice4 == 5:
                        team_size(choice3)
                    else:
                        print("Invalid choice")
            elif choice2 == 2:
                create_team(division_id)
                exit_program()
            elif choice2 == 3:
                player_search()
            else:
                print("Invalid choice")
        elif choice1 == 2:
            create_division()
        elif choice1 == 3:
            team_search()
        

def menu1():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List available divisions")
    print("2. Add a division")
    print("3. Search for a team")

def menu2():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List available teams")
    print("2. Add a team")
    print("3. Search for a player")

def menu3():
    print("Select the number for the team to diplay, or press 0 to exit the program: ")

def menu4():
    print("1. List current players on team")
    print("2. Add a new player to the team")
    print("3. List current coach info")
    print("4. Update coach info")
    print("5. Display total number of players on team")
    print("0. Exit the program")

def menu5():
    print("1. Delete Player")
    print("2. Update player name")
    print("0. Exit the program")

if __name__ == "__main__":
    main()
