import sqlite3

CONN = sqlite3.connect('soccer.db')
CURSOR = CONN.cursor()

class Team:

    # Dictionary of objects saved to the database.
    teams = {}

    def __init__(self, name, coach, id=None):
        self.id = id
        self.name = name
        self.coach = coach

    def __repr__(self):
        return f"{self.name}, {self.coach}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name.title()
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def coach(self):
        return self._coach

    @coach.setter
    def coach(self, coach):
        if isinstance(coach, str) and len(coach):
            self._coach = coach.title()
        else:
            raise ValueError(
                "Cach name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Team instances """
        sql = """
            CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT,
            coach TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Team instances """
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and league values of the current team instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO teams (name, coach)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.coach))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).teams[self.id] = self

        print("Saved team:", self.name, self.coach)
        print("Teams dictionary:", type(self).teams)

    @classmethod
    def create(cls, name, coach):
        """ Initialize a new Team instance and save the object to the database """
        team = cls(name, coach)
        team.save()
        return team

    def update(self):
        """Update the table row corresponding to the current Team instance."""
        sql = """
            UPDATE teams
            SET name = ?, coach = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.coach, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Team instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM teams
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).teams[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Team object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        team = cls.teams.get(row[0])
        if team:
            # ensure attributes match row values in case local instance was modified
            team.name = row[1]
            team.coach = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            team = cls(row[1], row[2])
            team.id = row[0]
            cls.teams[team.id] = team
        return team

    @classmethod
    def get_all(cls):
        """Return a list containing a Team object per row in the table"""
        sql = """
            SELECT *
            FROM teams
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Team object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM teams
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Team object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM teams
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def players(self):
        """Return list of players associated with current team"""
        from db.player import Player
        sql = """
            SELECT * FROM players
            WHERE team = ?
        """
        CURSOR.execute(sql, (self.team,),)

        rows = CURSOR.fetchall()
        return [
            Player.instance_from_db(row) for row in rows
        ]
    
    