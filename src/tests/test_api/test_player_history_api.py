from .functions import assert_keys_equal
from .expected_api_structure import player_history_keys
from src.fantasy.api.player_history_api import PlayerHistoryAPI


api_connection = PlayerHistoryAPI()


def test_api_response():
	"""
	Tests that:
	- The API receives a 200 response
	- The response keys are as expected
	"""
	api_response = api_connection.response
	api_content = api_connection.content
	assert api_response.status_code == 200
	assert_keys_equal(api_content, player_history_keys["base"])
	assert_keys_equal(api_content["fixtures"][0], player_history_keys["fixtures"])
	assert_keys_equal(api_content["history"][0], player_history_keys["history"])
	assert_keys_equal(api_content["history_past"][0], player_history_keys["history_past"])
