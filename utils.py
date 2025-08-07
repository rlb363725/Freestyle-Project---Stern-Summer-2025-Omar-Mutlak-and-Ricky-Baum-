def extract_stat(stat_list, stat_name):
    """
    Extracts a float stat value from a list of stat dictionaries using the statName key.
    Returns 0.0 if not found or if input is invalid.
    """
    if not isinstance(stat_list, list):
        print(f"[extract_stat] Expected list, got {type(stat_list)}")
        return 0.0

    for stat in stat_list:
        if isinstance(stat, dict) and stat.get("statName") == stat_name:
            try:
                return float(stat.get("statValue", 0.0))
            except (ValueError, TypeError):
                print(f"[extract_stat] Could not convert statValue to float for '{stat_name}'")
                return 0.0

    print(f"[extract_stat] Stat '{stat_name}' not found.")
    return 0.0


def predict_score(stats1, stats2):
    """
    Predicts a basic score estimate based on average offensive and defensive yards per game.
    Returns a tuple: (team1_score, team2_score)
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

        return max(team1_score, 0), max(team2_score, 0)

    except Exception as e:
        print("[predict_score] ERROR:", e)
        return 0, 0  # Always safe fallback


def calculate_win_probability(score1, score2):
    """
    Converts predicted scores into basic win probabilities.
    Returns a tuple: (team1_prob, team2_prob) as floats between 0 and 1.
    """
    total = score1 + score2
    if total == 0:
        return 0.5, 0.5
    team1_prob = round(score1 / total, 3)
    team2_prob = round(score2 / total, 3)
    return team1_prob, team2_prob













