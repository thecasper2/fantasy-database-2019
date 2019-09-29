bootstrap_static_keys = {
	"base": [
		'events', 'game_settings', 'phases', 'teams', 'total_players', 'elements', 'element_stats', 'element_types'
	],
	"elements": [
		'chance_of_playing_next_round', 'chance_of_playing_this_round', 'code', 'cost_change_event',
		'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'dreamteam_count',
		'element_type', 'ep_next', 'ep_this', 'event_points', 'first_name', 'form', 'id', 'in_dreamteam', 'news',
		'news_added', 'now_cost', 'photo', 'points_per_game', 'second_name', 'selected_by_percent', 'special',
		'squad_number', 'status', 'team', 'team_code', 'total_points', 'transfers_in', 'transfers_in_event',
		'transfers_out', 'transfers_out_event', 'value_form', 'value_season', 'web_name', 'minutes', 'goals_scored',
		'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards',
		'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index'
	],
	"teams": [
		'code', 'draw', 'form', 'id', 'loss', 'name', 'played', 'points', 'position', 'short_name', 'strength',
		'team_division', 'unavailable', 'win', 'strength_overall_home', 'strength_overall_away',
		'strength_attack_home', 'strength_attack_away', 'strength_defence_home', 'strength_defence_away'
	]
}

player_history_keys = {
	"base": [
		'fixtures', 'history', 'history_past'
	],
	"fixtures": [
		'code', 'team_h', 'team_h_score', 'team_a', 'team_a_score', 'event', 'finished', 'minutes',
		'provisional_start_time', 'kickoff_time', 'event_name', 'is_home', 'difficulty'
	],
	"history": [
		'element', 'fixture', 'opponent_team', 'total_points', 'was_home', 'kickoff_time', 'team_h_score',
		'team_a_score', 'round', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals',
		'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence',
		'creativity', 'threat', 'ict_index', 'value', 'transfers_balance', 'selected', 'transfers_in', 'transfers_out'
	],
	"history_past": [
		'season_name', 'element_code', 'start_cost', 'end_cost', 'total_points', 'minutes', 'goals_scored', 'assists',
		'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards',
		'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 'threat', 'ict_index'
	]
}