from src.fantasy.api.bootstrap_static_api import BootstrapStaticAPI


def test_api_response():
	"""
	Tests that the API receives a 200 response
	"""
	assert BootstrapStaticAPI().response.status_code == 200
