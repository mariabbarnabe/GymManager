"""
This class maps the Modality information from database and transforms in a response
to the API.
"""


class Modality(object):
    def __init__(self, modality_id, name):
        self.id = modality_id
        self.name = name

    def to_response(self):
        """ Transforms the database information in a response to the API.

        :return:  a JSON containing the information to be answered in the API.
        """
        return {
            'id': self.id,
            'name': self.name
        }
