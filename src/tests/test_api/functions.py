def assert_keys_equal(observed, expected):
	"""
	Checks if the received keys of the API response match that which is expected
	:param observed: Observed API keys
	:param expected: Expected API keys
	"""
	for key in expected:
		assert key in observed.keys()
