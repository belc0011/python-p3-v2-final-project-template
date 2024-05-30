# MSoccer League Manager

## Introduction
This project is a Command Line Interface designed for the purpose of organizing a soccer league. This CLI is useful for keeping rack of the teams in a particular league, information about those teams (such as the current coach), as well as all of the players on each of the teams. Currently the only information capable of being stored for each player is the team they play for and their jersey number. However, future implementations may include the ability to store additional stats for each player (such as goals scored, assists, and yellow/red cards received), as well as the ability to search by coach's name.

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## cli.py

The CLI is designed to print specific menus in response to user input. The main menu gives the user the option to generate a list of all available teams, add a new team, or search by player name to see which team they belong to. Depending on which option is selected, the CLI will then display the appropriate new menu related to their option. If the user chooses to display all available teams, they will then be prompted to select a team from the list, which will in turn display a new menu providing them with options for that team (display current players, add a new player, display current coach information, or update the coach information). Any options related to updating existing information or adding new information will result in a confirmation message to let the user know the changes were successful. At any point in the process, the user may exit the program by typing "0" followed by the enter key. The CLI is designed to automatically title case team names, coach names and player names, regardless of how they are entered by the user.


## helpers.py

The helpers.py file holds all of the methods responsible for carrying out the requests made by the user when prompted. A brief description of each method is provided below.

- create_team: This method will create a new Team object and persist the changes to the database. It prompts the user for the team name as well as the coach's name, then utilizes the create method to ensure the changes are persisted to the backend.
- print_all_teams: This method generates an ordered list of all available teams.
- 

## player.py



## team.py


## seed.py



This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
