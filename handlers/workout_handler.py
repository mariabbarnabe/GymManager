from dao.client_dao import ClientDao
from dao.gym_dao import GymDao
from dao.modality_dao import ModalityDao
from model.client import Client
from model.gym import Gym
from model.modality import Modality
from flask import abort

"""
This module provides handlers to create the API responses.
"""


def get_client_from_db(client_id):
    """ Gets the client information from database and creates the JSON response.

    :param client_id: the client's id to get information
    :return: A JSON containing the client's information
    """
    client_dao = ClientDao()
    client_query = client_dao.get_client_by_id(client_id)
    client_list = row_to_dict(client_query)
    if len(client_list) == 0:
        abort(404)
    if len(client_list) > 1:
        raise Exception("Database error: two clients with the same id")
    client_list = client_list[0]
    return Client(client_list["id"], client_list["name"],
                  client_list["email"]).to_response()


def get_client_list_from_db():
    """ Gets the client list from database and creates the JSON response.

    :return: A JSON containing list of all the client's information
    """
    client_dao = ClientDao()
    client_query = client_dao.get_client_list()
    client_list = row_to_dict(client_query)
    response_list = list()
    response = {}
    for row in client_list:
        response_list.append(
            Client(row["id"], row["name"], row["email"]).to_response())
    response["client_list"] = response_list
    return response


def get_client_gym_from_db(client_id):
    """ Gets the client's gym list from database and creates the JSON response.

    :param client_id: the client's id
    :return: a JSON containing a list of all gyms of this client
    """
    client_dao = ClientDao()
    gym_query = client_dao.get_client_gyms(client_id)
    gym_list = row_to_dict(gym_query)
    response_list = list()
    response = {}
    for row in gym_list:
        response_list.append(
            Gym(row["id"], row["name"], row["address"]).to_response())
    response["client_gyms"] = response_list
    return response


def get_client_modality_from_db(client_id):
    """ Gets the client's modality list from database and creates the JSON response.

    :param client_id: the client's id
    :return: a JSON containing a list of all modalities of this client
    """
    client_dao = ClientDao()
    modality_query = client_dao.get_client_modalities(client_id)
    modality_list = row_to_dict(modality_query)
    response_list = list()
    response = {}
    for row in modality_list:
        response_list.append(Modality(row["id"], row["name"]).to_response())
    response["client_modalities"] = response_list
    return response


def get_gym_list_from_db():
    """ Gets the gym list from database and creates the JSON response

    :return: a JSON containing a list of all the gym's information
    """
    gym_dao = GymDao()
    gym_query = gym_dao.get_gym_list()
    gym_list = row_to_dict(gym_query)
    response_list = list()
    response = {}
    for row in gym_list:
        response_list.append(
            Gym(row["id"], row["name"], row["address"]).to_response())
    response["gym_list"] = response_list
    return response


def get_gym_clients_from_db(gym_id):
    """ Gets the gym's client list from database and creates the JSON response.

    :param gym_id: the gym's id
    :return: a JSON containing a list of all clients of this gym
    """
    gym_dao = GymDao()
    client_query = gym_dao.get_gym_clients(gym_id)
    client_list = row_to_dict(client_query)
    response_list = list()
    response = {}
    for row in client_list:
        response_list.append(
            Client(row["id"], row["name"], row["email"]).to_response())
    response["gym_clients"] = response_list
    return response


def get_gym_modalities_from_db(gym_id):
    """ Gets the gym's modality list from database and creates the JSON response

    :param gym_id: the gym's id
    :return: a JSON containing a list of all modalities of this gym
    """
    gym_dao = GymDao()
    modality_query = gym_dao.get_gym_modalities(gym_id)
    modality_list = row_to_dict(modality_query)
    response_list = list()
    response = {}
    for row in modality_list:
        response_list.append(Modality(row["id"], row["name"]).to_response())
    response["gym_modalities"] = response_list
    return response


def get_modality_list_from_db():
    """ Gets the modality list from database and creates the JSON response

    :return: a JSON containing a list of all the modalities' information
    """
    modality_dao = ModalityDao()
    modality_query = modality_dao.get_modality_list()
    modality_list = row_to_dict(modality_query)
    response_list = list()
    response = {}
    for row in modality_list:
        response_list.append(
            Modality(row["id"], row["name"]).to_response())
    response["modality_list"] = response_list
    return response


def get_modality_gyms_from_db(modality_id):
    """ Gets the modality's gyms list from database and creates the JSON response

    :param modality_id: the modality's id
    :return: a JSON containing a list of all gyms of this modality
    """
    modality_dao = ModalityDao()
    gym_list = modality_dao.get_modality_gyms(modality_id)
    gym_list = row_to_dict(gym_list)
    response_list = list()
    response = {}
    for row in gym_list:
        response_list.append(
            Gym(row["id"], row["name"], row["address"]).to_response())
    response["modality_gyms"] = response_list
    return response


def row_to_dict(query_row):
    """ Transforms a list of Row objects to a list of Dictionary

    :param query_row: the Row object obtained through a query in database
    :return: a list of dictionaries
    """
    if query_row is None:
        abort(404)
    return [dict(row) for row in query_row]
