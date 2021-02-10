"""
This class maps the Client information from database and transforms in a response
to the API.
"""


class Client(object):
    def __init__(self, client_id, name, email):
        self.id = client_id
        self.name = name
        self.email = email

    def to_response(self):
        """ Transforms the database information in a response to the API.

        :return:  a JSON containing the information to be answered in the API.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
