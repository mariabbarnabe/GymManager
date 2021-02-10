"""
This class maps the Gym information from database and transforms in a response
to the API.
"""


class Gym(object):
    def __init__(self, gym_id, name, address):
        self.id = gym_id
        self.name = name
        self.address = address

    def to_response(self):
        """ Transforms the database information in a response to the API.

        :return:  a JSON containing the information to be answered in the API.
        """
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
