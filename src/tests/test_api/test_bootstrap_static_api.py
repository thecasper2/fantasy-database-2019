from .expected_api_structure import bootstrap_static_keys
from src.fantasy.api.bootstrap_static_api import BootstrapStaticAPI

from json import loads


def assert_keys_equal(observed, expected):
	"""
	Checks if the received keys of the API response match that which is expected
	:param observed: Observed API keys
	:param expected: Expected API keys
	"""
	for key in expected:
		assert key in observed.keys()


def test_api_response():
	"""
	Tests that:
	- The API receives a 200 response
	- The response keys are as expected
	"""
	api_response = BootstrapStaticAPI().response
	api_content = loads(api_response.content)
	assert api_response.status_code == 200
	assert_keys_equal(api_content, bootstrap_static_keys["base"])
	assert_keys_equal(api_content["elements"][0], bootstrap_static_keys["elements"])
	assert_keys_equal(api_content["teams"][0], bootstrap_static_keys["teams"])
