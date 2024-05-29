import sqlite3

CONN = sqlite3.connect('soccer.db')
CURSOR = CONN.cursor()

from lib.db.player import Player
from lib.db.team import Team

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
    Player.create("Bukayo Saka", "Arsenal", 1, 7)
    Player.create("Gabriel Jesus", "Arsenal", 1, 9)
    Player.create("Mohammad Salah", "Liverpool", 2, 11)
    Player.create("Vergil Van Dijk", "Liverpool", 2, 4)
    Player.create("Toni Kroos", "Real Madrid", 3, 8)
    Player.create("Luka Madric", "Real Madrid", 3, 10)
    Player.create("Rodrygo", "Real Madrid", 3, 9)
    Player.create("Haaland", "Manchester City", 4, 9)
    Player.create("Phil Foden", "Manchester City", 4, 47)
    Player.create("Casemiro", "Manchester United", 5, 18)
    Player.create("Garnacho", "Manchester United", 5, 49)
    Player.create("Tim Reem", "Fulham", 6, 64)
    Player.create("Kenny Tete", "Fulham", 6, 2)
    Player.create("Bernd Leno", "Fulham", 6, 16)
    Player.create("Dominic Calvert-Lewin", "Everton", 7, 9)
    Player.create("Cole Palmer", "Chelsea", 8, 20)
    Player.create("Robert Lewandowski", "FC Barcelona", 9, 9)
    Player.create("Pedri", "FC Barcelona", 9, 8)
    Player.create("Gavi", "FC Barcelona", 9, 6)
    Player.create("Dusan Vlahovic", "Juventus", 10, 9)
    Player.create("Oshimen", "Napoli", 11, 9)
    Player.create("Dimarco", "Inter Milan", 12, 32)
    Player.create("Alvaro Marata", "Atletico de Madrid", 13, 7)
    Player.create("Antoine Griezmann", "Atletico de Madrid", 13, 7)



seed_database()
print("Seeded database")