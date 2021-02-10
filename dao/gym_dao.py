from handlers.sqlite_handler import create_connection
from config.constants import DATABASE_PATH

"""
This class implements all database operations for Gym entity.
"""


class GymDao(object):
    def __init__(self):
        """Initialize objects to perform database operations."""
        self.conn = create_connection(DATABASE_PATH)

    def get_gym_list(self):
        """ Gets a list containing all the gyms and its information

        :return: a list containing all the gyms and its information
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM GYM""")
        return cursor.fetchall()

    def get_gym_clients(self, gym_id):
        """ Gets a list containing all the gym's client names

        :param gym_id: the gym's id number
        :return: a list containing the gym's client names
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT c.*
                          FROM CLIENT_GYM as cg
                          JOIN CLIENT AS c ON cg.client_id=c.id 
                          WHERE cg.gym_id={}""".format(gym_id))
        return cursor.fetchall()

    def get_gym_modalities(self, gym_id):
        """ Gets a list containing all the gym's modalities names

        :param gym_id: the gym's id number
        :return: a list containing the gym's modalities names
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT m.* 
                          FROM GYM_MODALITY AS gm 
                          JOIN MODALITY AS m ON gm.modality_id=m.id 
                          WHERE gm.gym_id={}""".format(gym_id))
        return cursor.fetchall()
