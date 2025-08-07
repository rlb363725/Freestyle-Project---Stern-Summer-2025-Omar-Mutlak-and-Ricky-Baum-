from data_fetcher import get_team_stats, get_team_roster
from utils import predict_score, calculate_win_probability
from visuals import plot_team_comparison, plot_team_roster

def simulate_matchup(team1, team2, year):
    stats1 = get_team_stats(team1, year)
    stats2 = get_team_stats(team2, year)
    roster1 = get_team_roster(team1, year)
    roster2 = get_team_roster(team2, year)

    score1, score2 = predict_score(stats1, stats2)
    prob1, prob2 = calculate_win_probability(score1, score2)

    winner = "Tie"
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2

    plot_team_comparison(team1, team2, stats1, stats2)
    plot_team_roster(team1, roster1)
    plot_team_roster(team2, roster2)

    return (
        f"\n{team1} ({prob1}%) vs. {team2} ({prob2}%)\n"
        f"Predicted Score: {team1} {score1} - {score2} {team2} → Winner: {winner}"
    )








