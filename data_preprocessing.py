import pandas as pd
import numpy as np

# Load data
game_results_df = pd.read_json("game_results.json")
player_stats_df = pd.read_json("player_stats.json")
team_standings_df = pd.read_json("team_standings.json")
schedule_df = pd.read_json("schedule.json")

# Handle missing or inconsistent data
player_stats_df.fillna(0, inplace=True)

# Convert data types (example, adjust according to your data)

# Create new features or aggregations
print("Player Stats Columns:", player_stats_df.columns)
player_stats_df['AveragePointsPerGame'] = player_stats_df['FantasyPointsBatting'] / player_stats_df['Games']

# Merge DataFrames (example, adjust according to your data)
merged_df = game_results_df.merge(schedule_df, on='GameID', suffixes=('_results', '_schedule'))

# Save preprocessed data
game_results_df.to_json("cleaned_game_results.json")
player_stats_df.to_json("cleaned_player_stats.json")
team_standings_df.to_json("cleaned_team_standings.json")
schedule_df.to_json("cleaned_schedule.json")

print("Game Results Data:\n", game_results_df.head())
print("\nPlayer Stats Data:\n", player_stats_df.head())
print("\nTeam Standings Data:\n", team_standings_df.head())
print("\nSchedule Data:\n", schedule_df.head())
