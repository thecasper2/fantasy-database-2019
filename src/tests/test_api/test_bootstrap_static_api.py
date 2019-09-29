from .functions import assert_keys_equal
from .expected_api_structure import bootstrap_static_keys
from src.fantasy.api.bootstrap_static_api import BootstrapStaticAPI


api_connection = BootstrapStaticAPI()


def test_api_response():
	"""
	Tests that:
	- The API receives a 200 response
	- The response keys are as expected
	"""
	api_response = api_connection.response
	api_content = api_connection.content
	assert api_response.status_code == 200
	assert_keys_equal(api_content, bootstrap_static_keys["base"])
	assert_keys_equal(api_content["elements"][0], bootstrap_static_keys["elements"])
	assert_keys_equal(api_content["teams"][0], bootstrap_static_keys["teams"])


def test_player_ids(min_players: int = 100):
	"""
	Tests that:
	- We receive at least the minimum number of player id values
	"""
	player_ids = api_connection.player_ids()
	assert len(player_ids) >= min_players
