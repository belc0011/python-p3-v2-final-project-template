
from models.__init__ import CONN, CURSOR

class Player:
    #Dictionary to store all player objects
    players = {}
    def __init__(self, name, team, jersey_number=None, team_id=None, id=None):
        self.name = name
        self.team = team
        self.team_id = team_id
        self.jersey_number = jersey_number
        self.id = id
    
    def __repr__(self):
        return (
            f"<Player {self.id}: {self.name}, #{self.jersey_number} from {self.team}"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
    
    @property
    def team(self):
        return self._team
    
    @team.setter
    def team(self, team):
        self._team = team 
    
    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, team_id):
        self._team_id = team_id

    @classmethod
    def create_table(cls):
        """ Create a new table so Player objects are persisted in db """
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            team TEXT,
            jersey_number INTEGER,
            team_id INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Delete table when no longer needed """
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert a new row with the attributes of the current player object.
        Update object's id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO players (name, team, jersey_number, team_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.team, self.jersey_number, self.team_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).players[self.id] = self

    @classmethod
    def create(cls, name, team, jersey_number=None, team_id=None):
        """ Initialize a new player object and save the object to the database """
        from .team import Team
        teams = Team.get_all()
        for instance in teams:
            if instance.name == team:
                team_id = instance.id
        player = cls(name, team, jersey_number, team_id)
        player.save()
        return player
    
    def update(self):
        """Update the table row corresponding to the current player object."""
        sql = """
            UPDATE players
            SET name = ?, team = ?, jersey_number = ?, team_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.team, self.jersey_number, 
                             self.team_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current player object,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).players[self.id]

        # Set the id to None
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        player = cls.players.get(row[0])
        if player:
            # ensure attributes match row values in case local instance was modified
            player.name = row[1]
            player.team = row[2]
            player.jersey_number = row[3]
            player.team_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            player = cls(row[1], row[2], row[3], row[4])
            player.id = row[0]
            cls.players[player.id] = player
        return player
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Player object per table row"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return Player object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM players
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_team(cls, team):
        """Return list of Player objects that have the matching specified team"""
        sql = """
            SELECT *
            FROM players
            WHERE team is ?
        """
        
        rows = CURSOR.execute(sql, (team,)).fetchall()
        teams = [cls.instance_from_db(row) for row in rows]
        return teams
    