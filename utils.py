def extract_stat(stat_list, stat_name):
    """
    Extracts a stat value from a list of stat dictionaries based on stat name.
    Returns 0.0 if the stat is not found.
    """
    if not isinstance(stat_list, list):
        print(f"DEBUG: Expected list for stat_list, got {type(stat_list)}")
        return 0.0

    for stat in stat_list:
        if isinstance(stat, dict) and stat.get("statName") == stat_name:
            return float(stat.get("statValue", 0.0))

    print(f"DEBUG: Stat '{stat_name}' not found in list.")
    return 0.0


def predict_score(stats1, stats2):
    """
    Predicts a realistic score for each team based on total yards and opponent defense.
    Returns a tuple of (score1, score2). Will NEVER return None.
    """
    try:
        games1 = extract_stat(stats1, "games") or 1
        games2 = extract_stat(stats2, "games") or 1

        team1_off_yards_pg = extract_stat(stats1, "totalYards") / games1
        team2_off_yards_pg = extract_stat(stats2, "totalYards") / games2

        team1_def_yards_pg = extract_stat(stats1, "totalYardsOpponent") / games1
        team2_def_yards_pg = extract_stat(stats2, "totalYardsOpponent") / games2

        team1_score = int(((team1_off_yards_pg + team2_def_yards_pg) / 2) * 0.1)
        team2_score = int(((team2_off_yards_pg + team1_def_yards_pg) / 2) * 0.1)

        return team1_score, team2_score

    except Exception as e:
        print("ERROR in predict_score:", e)
        return 0, 0  # Always return a tuple to avoid unpacking error


def calculate_win_probability(score1, score2):
    """
    Calculates win probabilities based on predicted scores.
    Returns a tuple of percentages (team1, team2).
    """
    total = score1 + score2
    if total == 0:
        return 50.0, 50.0  # default if tied at 0

    prob1 = (score1 / total) * 100
    prob2 = (score2 / total) * 100
    return round(prob1, 1), round(prob2, 1)


def generate_roster_html(team1, roster1, team2, roster2):
    """Generates an HTML file to display rosters and opens it in a browser."""
    html_content = f"""
    <html>
    <head>
        <title>Team Rosters</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ color: #333; }}
            table {{ width: 50%; float: left; border-collapse: collapse; margin-right: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>{team1} Roster</h1>
        <table>
            <tr><th>Name</th><th>Position</th><th>Jersey</th></tr>
            {''.join([f"<tr><td>{p.get('first_name', '')} {p.get('last_name', '')}</td><td>{p.get('position', 'N/A')}</td><td>{p.get('jersey', 'N/A')}</td></tr>" for p in roster1])}
        </table>
        <h1>{team2} Roster</h1>
        <table>
            <tr><th>Name</th><th>Position</th><th>Jersey</th></tr>
            {''.join([f"<tr><td>{p.get('first_name', '')} {p.get('last_name', '')}</td><td>{p.get('position', 'N/A')}</td><td>{p.get('jersey', 'N/A')}</td></tr>" for p in roster2])}
        </table>
    </body>
    </html>
    """
    with open("rosters.html", "w") as f:
        f.write(html_content)














