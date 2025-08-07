import plotly.graph_objects as go
from utils import extract_stat

def plot_team_comparison(team1, team2, stats1, stats2):
    # Extract key stats
    team1_off_yards = extract_stat(stats1, "totalYards")
    team2_off_yards = extract_stat(stats2, "totalYards")

    team1_def_yards = extract_stat(stats1, "totalYardsOpponent")
    team2_def_yards = extract_stat(stats2, "totalYardsOpponent")

    categories = ["Offensive Yards", "Defensive Yards Allowed"]
    team1_values = [team1_off_yards, team1_def_yards]
    team2_values = [team2_off_yards, team2_def_yards]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=team1_values,
        name=team1
    ))

    fig.add_trace(go.Bar(
        x=categories,
        y=team2_values,
        name=team2
    ))

    fig.update_layout(
        title=f"{team1} vs {team2} - Yardage Comparison",
        xaxis_title="Category",
        yaxis_title="Yards",
        barmode='group'
    )

    fig.show()


def plot_player_comparison(player_stats, stat_type="passingYards", top_n=5):
    """
    Plot comparison of top N players by a specific stat.

    Args:
        player_stats (list of dict): Each dict should have the following keys:
    sorted_players = sorted(
        filtered_players,
        key=lambda p: float(p.get("stat", 0)) if str(p.get("stat", "0")).replace('.', '', 1).isdigit() else 0,
        reverse=True
    )[:top_n]
            - "statType" (str): The type of stat (e.g., "passingYards").
            - "stat" (str or float): The value of the stat.
        stat_type (str): The stat type to compare (default "passingYards").
        top_n (int): Number of top players to display (default 5).

    `player_stats` should be the result of get_team_players(team, year).
    """
    filtered_players = [p for p in player_stats if p.get("statType") == stat_type]
    sorted_players = sorted(filtered_players, key=lambda p: float(p["stat"]), reverse=True)[:top_n]

    names = [p.get("player", "Unknown") for p in sorted_players]
    stats = [float(p.get("stat", 0)) for p in sorted_players]

    fig = go.Figure([go.Bar(x=names, y=stats)])

    fig.update_layout(
        title=f"Top {top_n} Players by {stat_type}",
        xaxis_title="Player",
        yaxis_title=stat_type,
        template="plotly_white"
    )

    fig.show()



