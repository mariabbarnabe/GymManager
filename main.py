import flask
from handlers.workout_handler import get_client_from_db
from handlers.workout_handler import get_client_list_from_db
from handlers.workout_handler import get_client_gym_from_db
from handlers.workout_handler import get_client_modality_from_db
from handlers.workout_handler import get_gym_list_from_db
from handlers.workout_handler import get_gym_clients_from_db
from handlers.workout_handler import get_gym_modalities_from_db
from handlers.workout_handler import get_modality_list_from_db
from handlers.workout_handler import get_modality_gyms_from_db

app = flask.Flask(__name__)


@app.route('/')
def index():
    """ This method defines the default URL."""
    return "Welcome to the Gym"


@app.route('/client/list')
def get_client_list():
    """ This method defines an API that returns the client list."""
    return get_client_list_from_db()


@app.route('/client/id/<int:client_id>')
def get_client_by_id(client_id):
    """ This method defines an API that returns the client information by id."""
    return get_client_from_db(client_id)


@app.route('/client/<int:client_id>/gyms')
def get_client_gyms(client_id):
    """ This method defines an API that returns all gyms visited by the client."""
    return get_client_gym_from_db(client_id)


@app.route('/client/<int:client_id>/modalities/')
def get_client_modalities(client_id):
    """ This method defines an API that returns all modalities used by the client."""
    return get_client_modality_from_db(client_id)


@app.route('/gym/list')
def get_gym_list():
    """ This method defines an API that returns the gym list."""
    return get_gym_list_from_db()


@app.route('/gym/<int:gym_id>/clients')
def get_gym_clients(gym_id):
    """ This method defines a API that returns all the clients of a gym"""
    return get_gym_clients_from_db(gym_id)


@app.route('/gym/<int:gym_id>/modalities')
def get_gym_modalities(gym_id):
    """ This method defines a API that returns all the modalities of a gym"""
    return get_gym_modalities_from_db(gym_id)


@app.route('/modality/list')
def get_modality_list():
    """ This method defines a API that returns the modalities list"""
    return get_modality_list_from_db()


@app.route('/modality/<int:modality_id>/gyms')
def get_modality_gyms(modality_id):
    """ This method defines a API that returns all the gyms that offer a modality"""
    return get_modality_gyms_from_db(modality_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
