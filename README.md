# MSoccer League Manager

## Introduction
This project is a Command Line Interface designed for the purpose of organizing a soccer league. This CLI is useful for keeping rack of the teams in a particular league, information about those teams (such as the current coach), as well as all of the players on each of the teams. Currently the only information capable of being stored for each player is the team they play for and their jersey number. However, future implementations may include the ability to store additional stats for each player (such as goals scored, assists, and yellow/red cards received), as well as the ability to search by coach's name.

## Important Files

### cli.py

The CLI is designed to print specific menus in response to user input. The main menu gives the user the option to generate a list of all available teams, add a new team, or search by player name to see which team they belong to. Depending on which option is selected, the CLI will then display the appropriate new menu related to their option. If the user chooses to display all available teams, they will then be prompted to select a team from the list, which will in turn display a new menu providing them with options for that team (display current players, add a new player, display current coach information, or update the coach information). Any options related to updating existing information or adding new information will result in a confirmation message to let the user know the changes were successful. At any point in the process, the user may exit the program by typing "0" followed by the enter key. The CLI is designed to automatically title case team names, coach names and player names, regardless of how they are entered by the user.


### helpers.py

The helpers.py file holds all of the methods responsible for carrying out the requests made by the user when prompted. A brief description of each method is provided below.

- create_team: Creates a new Team object and persist the changes to the database. It prompts the user for the team name as well as the coach's name, then utilizes the create method to ensure the changes are persisted to the backend.
- print_all_teams: Generates an ordered list of all available teams, which allows the user to use a number in order to select a specific team.
- get_all_players: Generates an ordered list of all players belonging to the specified team, which allows the user to use a number in order to select a specific player.
- exit_program: Calls the built-in exit() function provided by Python to stop the script and return to the terminal.
- team_info_printer: Displays the name and current coach for a team based on the user input. Includes logic to handle invalid selections, re-prompting the user to choose a number corresponding to a team in the list or to choose "0" to exit the program.
- add_new_player: Provides the appropriate user prompts to gather the information necessary to create a new Player object and persist it to the database by calling the create method for the Player class.
- coach_info: Prints the coach's name for the selected team.
- set_coach: Allows the user to change the coach's name for the selected team, then persists the changes to the database by calling the update method for the Team class.
- delete_player: Allows the user to delete a player from a team by selecting the number corresponding to the player they wish to delete in the list. Permanently deletes in the backend by calling the delete method in the Player class.
- update_player: Allows the user to change the spelling of the name of a player on the team (method included to make correcting typos more easily). Persists changes to the backend by calling the update method in the Player class.
- team_size: Displays the total number of players on the team currently.
- player_search: Allows user to search for a player by name rather than having to select each team and generate a list of players one team at a time. Set to automatically title case the user's input so they do not have to worry about capitalization.

### init.py

The init model imports the sqlite3 module from Python to allow the CLI to connect to and interact with a database. It also holds the connection object (named CONN) and the cursor object (named CURSOR). 

### player.py

This is the Player class which holds all of the logic necessary for creating new instances of the Player class. This CLI models a one-to-many relationship, where one team has many players. As a result, the Player class has an additional attribute "team_id" which serves as the foreign key in the database table, linking each player to a specific team. This model holds modules necessary for creating a new member of the Player class and saving it to the database, updating existing Player objects and persisting those changes, deleting existing Player objects (and removing them from the database), as well as finding players using various attributes.

### team.py

This is the Team class which holds all of the logic necessary for creating new instances of the Team class, storing them in a dictionary, and persisting them to the database. It has modules responsible for saving (saving a new Team object to the database and adding it to the dictionary), updating (allowing changes to an existing Team object to be persisted to the database), deleting (removing an existing team object from the database, as well as the dictionary), as well as many modules useful for finding Team objects using different attributes.

### seed.py

This file provides seed data to showcase the functionality of the CLI without the user having to first enter a bunch of teams and players.


## Usage

The project is available using the following steps:
- git clone https://github.com/belc0011/soccer-league-manager
- pipenv install (to install dependencies)
- pipenv shell (to enter virtual environment)
- python lib/seed.py (optional, if you want to seed the database prior to usage)
- python lib/cli.py

