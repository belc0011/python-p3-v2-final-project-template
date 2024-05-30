import sqlite3

CONN = sqlite3.connect('soccer.db')
CURSOR = CONN.cursor()

class Division:

    # Dictionary of objects saved to the database.
    divisions = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.name} division>"

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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Division instances """
        sql = """
            CREATE TABLE IF NOT EXISTS divisions (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Division instances """
        sql = """
            DROP TABLE IF EXISTS divisions;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name of the current division instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO divisions (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).divisions[self.id] = self


    @classmethod
    def create(cls, name):
        """ Initialize a new Division instance and save the object to the database """
        division = cls(name)
        division.save()
        return division

    def update(self):
        """Update the table row corresponding to the current Division instance."""
        sql = """
            UPDATE divisions
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Division instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM divisions
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).divisions[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Division object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        division = cls.divisions.get(row[0])
        if division:
            # ensure attributes match row values in case local instance was modified
            division.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            division = cls(row[1])
            division.id = row[0]
            cls.divisions[division.id] = division
        return division

    @classmethod
    def get_all(cls):
        """Return a list containing a Division object per row in the table"""
        sql = """
            SELECT *
            FROM divisions
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Division object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM divisions
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Division object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM divisions
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def players(self):
        """Return list of teams associated with current division object"""
        from models.team import Team
        sql = """
            SELECT * FROM teams
            WHERE division = ?
        """
        CURSOR.execute(sql, (self.name,),)

        rows = CURSOR.fetchall()
        return [
            Team.instance_from_db(row) for row in rows
        ]
    
    