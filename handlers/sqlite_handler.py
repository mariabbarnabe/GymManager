import sqlite3
from sqlite3 import Error

"""
This module provides a handler for all sqlite3 operations.
"""


def create_connection(db_file):
    """ Creates a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
