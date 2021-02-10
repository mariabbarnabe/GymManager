from handlers.sqlite_handler import create_connection
from config.constants import DATABASE_PATH

"""
This class implements all database operations for Client entity.
"""


class ClientDao(object):
    def __init__(self):
        """Initialize objects to perform database operations."""
        self.conn = create_connection(DATABASE_PATH)

    def get_client_by_id(self, client_id):
        """ Gets the client information based on its id.

        :param client_id: the client's id number
        :return: the client's information
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM CLIENT WHERE id={}""".format(client_id))
        return cursor.fetchall()

    def get_client_list(self):
        """ Gets a list containing all the clients and its information

        :return: a list containing all the clients and its information
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM CLIENT""")
        return cursor.fetchall()

    def get_client_gyms(self, client_id):
        """ Gets the gyms' names frequented by the client

        :param client_id: the client's id number
        :return: a list containing the name of the gyms frequented by the client
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT g.* 
                          FROM CLIENT_GYM AS cg
                          JOIN GYM AS g ON cg.gym_id=g.id
                          WHERE cg.client_id={}""".format(client_id))
        return cursor.fetchall()

    def get_client_modalities(self, client_id):
        """ Gets the modalities names frequented by the client

        :param client_id: the client's id number
        :return: a list containing the name of the modalities frequented by the
        client
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT m.* 
                          FROM CLIENT_MODALITY AS cm
                          JOIN MODALITY AS m ON cm.modality_id=m.id
                          WHERE cm.client_id={}""".format(client_id))
        return cursor.fetchall()
