import sqlite3

CONN = sqlite3.connect('soccer.db')
CURSOR = CONN.cursor()

from lib.models.player import Player
from lib.models.team import Team

def seed_database():
    Player.drop_table()
    Team.drop_table()
    Team.create_table()
    Player.create_table()

    # Create seed data
    arsenal = Team.create("Arsenal", "Mikel Arteta")
    liverpool = Team.create("Liverpool", "Arne Slot")
    real_madrid = Team.create("Real Madrid", "Carlo Ancelotti")
    manchester_city = Team.create("Manchester City", "Pep Guardiola")
    manchester_united = Team.create("Manchester United", "Erik Ten Hag")
    fulham = Team.create("Fulham", "Marco Silva")
    everton = Team.create("Everton", "Sean Dyche")
    chelsea = Team.create("Chelsea", "Enzo Maresca")
    fc_barcelona = Team.create("FC Barcelona", "Hansi Flick")
    juventus = Team.create("Juventus", "Massimilliano Allegri")
    napoli = Team.create("Napoli", "Luciano Spalletti")
    inter_milan = Team.create("Inter Milan", "Simone Inzaghi")
    atletico_madrid = Team.create("Atletico de Madrid", "Diego Simeone")
    Player.create("Bukayo Saka", "Arsenal", 7, 1)
    Player.create("Gabriel Jesus", "Arsenal", 9, 1)
    Player.create("Mohammad Salah", "Liverpool", 11, 2)
    Player.create("Vergil Van Dijk", "Liverpool", 4, 2)
    Player.create("Toni Kroos", "Real Madrid", 8, 3)
    Player.create("Luka Madric", "Real Madrid", 10, 3)
    Player.create("Rodrygo", "Real Madrid", 9, 3)
    Player.create("Haaland", "Manchester City", 9, 4)
    Player.create("Phil Foden", "Manchester City", 47, 4)
    Player.create("Casemiro", "Manchester United", 18, 5)
    Player.create("Garnacho", "Manchester United", 49, 5)
    Player.create("Tim Reem", "Fulham", 64, 6)
    Player.create("Kenny Tete", "Fulham", 2, 6)
    Player.create("Bernd Leno", "Fulham", 16, 6)
    Player.create("Dominic Calvert-Lewin", "Everton", 9, 7)
    Player.create("Cole Palmer", "Chelsea", 20, 8)
    Player.create("Robert Lewandowski", "FC Barcelona", 9, 9)
    Player.create("Pedri", "FC Barcelona", 8, 9)
    Player.create("Gavi", "FC Barcelona", 6, 9)
    Player.create("Dusan Vlahovic", "Juventus", 9, 10)
    Player.create("Oshimen", "Napoli", 9, 11)
    Player.create("Dimarco", "Inter Milan", 32, 12)
    Player.create("Alvaro Marata", "Atletico de Madrid", 7, 13)
    Player.create("Antoine Griezmann", "Atletico de Madrid", 12, 13)



seed_database()
print("Seeded database")