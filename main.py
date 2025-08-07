from data_fetcher import get_team_stats, get_roster, get_player_stats
from visuals import plot_team_comparison, plot_win_probability, plot_top_players

year = 2024
team1 = "Florida"
team2 = "Alabama"

# Get team stats
stats1 = get_team_stats(team1, year)
stats2 = get_team_stats(team2, year)

# Plot stats
plot_team_comparison(team1, team2, stats1, stats2)
plot_win_probability(team1, team2, stats1, stats2)

# Get top player data by category
passing_stats = get_player_stats(year, category="passing")
rushing_stats = get_player_stats(year, category="rushing")
receiving_stats = get_player_stats(year, category="receiving")

# Plot top players
plot_top_players("Top 5 Passers", passing_stats, "Passing Yards")
plot_top_players("Top 5 Rushers", rushing_stats, "Rushing Yards")
plot_top_players("Top 5 Receivers", receiving_stats, "Receiving Yards")









