import plotly.graph_objects as go
from utils import extract_stat



def plot_team_comparison(team1, team2, stats1, stats2):
    categories = ["totalYards", "netPassingYards", "rushingYards", "turnovers"]
    labels = ["Total Yards", "Passing Yards", "Rushing Yards", "Turnovers"]

    from utils import extract_stat

    y1 = [extract_stat(stats1, name) for name in categories]
    y2 = [extract_stat(stats2, name) for name in categories]


    fig = go.Figure()
    fig.add_trace(go.Bar(x=labels, y=y1, name=team1))
    fig.add_trace(go.Bar(x=labels, y=y2, name=team2))
    fig.update_layout(title="Team Stats Comparison", barmode="group")
    fig.show()


def plot_win_probability(team1, team2, stats1, stats2):
    def get_yards(stats):
     return extract_stat(stats, "totalYards")

    y1 = get_yards(stats1)
    y2 = get_yards(stats2)

    fig = go.Figure(data=[
        go.Pie(labels=[team1, team2], values=[y1, y2], hole=0.4)
    ])
    fig.update_layout(title="Win Probability Estimate (by Yardage)")
    fig.show()


def plot_top_players(title, player_stats, stat_key, top_n=5):
    sorted_players = sorted(player_stats, key=lambda x: float(x.get("stat", 0)), reverse=True)[:top_n]
    names = [f'{p["player"]["firstName"]} {p["player"]["lastName"]}' for p in sorted_players]
    values = [float(p["stat"]) for p in sorted_players]

    fig = go.Figure(data=[
        go.Bar(x=names, y=values)
    ])
    fig.update_layout(title=title, xaxis_title="Player", yaxis_title=stat_key)
    fig.show()
