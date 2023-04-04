import requests
import json

api_key = "67387dc6939746e1a2d795435e2ac8c9"

# Define the endpoints
game_results_endpoint = f"https://api.sportsdata.io/v3/mlb/scores/json/Games/2023?key={api_key}"
player_stats_endpoint = f"https://api.sportsdata.io/v3/mlb/stats/json/PlayerSeasonStats/2023?key={api_key}"
team_standings_endpoint = f"https://api.sportsdata.io/v3/mlb/scores/json/Standings/2023?key={api_key}"
schedule_endpoint = f"https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/2023-04-01?key={api_key}"

# Fetch data from the API
try:
    game_results_data = requests.get(game_results_endpoint).json()
except ValueError as e:
    print("Error fetching game results data:", e)

try:
    player_stats_data = requests.get(player_stats_endpoint).json()
except ValueError as e:
    print("Error fetching player stats data:", e)

try:
    team_standings_data = requests.get(team_standings_endpoint).json()
except ValueError as e:
    print("Error fetching team standings data:", e)

try:
    schedule_data = requests.get(schedule_endpoint).json()
except ValueError as e:
    print("Error fetching schedule data:", e)

# Save data to JSON files
with open("game_results.json", "w") as f:
    json.dump(game_results_data, f)

with open("player_stats.json", "w") as f:
    json.dump(player_stats_data, f)

with open("team_standings.json", "w") as f:
    json.dump(team_standings_data, f)

with open("schedule.json", "w") as f:
    json.dump(schedule_data, f)

