from handlers.sqlite_handler import create_connection
from config.constants import DATABASE_PATH

"""
This class implements all database operations for the Modality entity.
"""


class ModalityDao(object):
    def __init__(self):
        """Creates the connection to perform database operations."""
        self.conn = create_connection(DATABASE_PATH)

    def get_modality_list(self):
        """ Gets a list of all the modalities and its information.

        :return:a list of all the modalities and its information
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM MODALITY""")
        return cursor.fetchall()

    def get_modality_gyms(self, modality_id):
        """ Gets a list containing all gyms that offer a specific modality.

        :param modality_id: the modality's id number
        :return: a list containing all gyms that offer a specific modality.
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT g.* 
                          FROM GYM_MODALITY AS gm
                          JOIN GYM AS g ON gm.gym_id=g.id
                          WHERE gm.modality_id={}""".format(modality_id))
        return cursor.fetchall()

