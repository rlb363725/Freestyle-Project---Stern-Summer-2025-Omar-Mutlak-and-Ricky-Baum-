from data_fetcher import get_team_stats, get_team_roster
from utils import predict_score, extract_stat, display_roster
from visuals import plot_team_comparison

def simulate_matchup(team1, team2, year):
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)

    roster1 = get_team_roster(team1, year)
    print(f"\n--- {team1} Roster ---")
    display_roster(roster1)

    roster2 = get_team_roster(team2, year)
    print(f"\n--- {team2} Roster ---")
    display_roster(roster2)

    score1, score2 = predict_score(stats1, stats2)

    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    plot_team_comparison(team1, team2, stats1, stats2)

    return f"\n{team1} {score1} - {score2} {team2} → Winner: {winner}"








