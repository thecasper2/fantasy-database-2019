# This contains the URLs required to access the APIs

api_dict = {
	"bootstrap_static": {
		"url": "https://fantasy.premierleague.com/api/bootstrap-static/",
		"subdirs": [
			"events", "game_settings", "phases", "teams", "total_players", "elements", "element_stats", "element_types"
		]
	},
	"fixtures": {
		"url": "https://fantasy.premierleague.com/api/fixtures/",
		"description": """
			A list of Premier League fixtures and their outcomes
		"""
	},
	"player_history": {
		"url": "https://fantasy.premierleague.com/api/element-summary/{player_id}/",
		"subdirs": ["fixtures", "history", "history_past"],
		"description": """
			fixtures: A list of fixtures for the given player, the fixture stats, and the player minutes
			history: A list of fixtures for the given player with detailed stats on the player's involvement and
				status at the time
			history_past: A list of previous seasons for the player, and summary statistics
		"""
	}
}
