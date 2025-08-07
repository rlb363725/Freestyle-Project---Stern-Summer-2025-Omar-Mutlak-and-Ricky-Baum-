from data_fetcher import get_team_stats, get_player_stats
from utils import predict_score, extract_stat, calculate_win_probability
from visuals import (
    plot_team_comparison,
    plot_win_probability,
    plot_top_players
)

def simulate_matchup(team1, team2, year):
    # Get team stats
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)

    # Predict score & win probability
    score1, score2 = predict_score(stats1, stats2)
    win_prob1, win_prob2 = calculate_win_probability(score1, score2)

    # Determine winner
    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    # --- Terminal Summary ---
    print(f"\n--- Stat Summary ---")
    print(f"{team1} - Total Yards: {extract_stat(stats1, 'totalYards')}, Passing: {extract_stat(stats1, 'netPassingYards')}, Rushing: {extract_stat(stats1, 'rushingYards')}")
    print(f"{team2} - Total Yards: {extract_stat(stats2, 'totalYards')}, Passing: {extract_stat(stats2, 'netPassingYards')}, Rushing: {extract_stat(stats2, 'rushingYards')}")
    print(f"\n--- Matchup Result ---")
    print(f"{team1} {score1} - {score2} {team2} → Winner: {winner}")
    print(f"\nWin Probability: {team1} {win_prob1}% | {team2} {win_prob2}%")

    # --- Visuals ---
    plot_team_comparison(team1, team2, stats1, stats2)
    plot_win_probability(team1, team2, stats1, stats2)

    # --- Real Top Players ---
    passing = get_player_stats(year, category="passing")
    rushing = get_player_stats(year, category="rushing")
    receiving = get_player_stats(year, category="receiving")

    plot_top_players("Top 5 Passers", passing, "Passing Yards")
    plot_top_players("Top 5 Rushers", rushing, "Rushing Yards")
    plot_top_players("Top 5 Receivers", receiving, "Receiving Yards")

    return score1, score2


