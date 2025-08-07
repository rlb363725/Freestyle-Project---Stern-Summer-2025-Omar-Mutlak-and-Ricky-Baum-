def plot_player_comparison(player_stats, stat_type="passingYards", top_n=5):
    filtered_players = [p for p in player_stats if p.get("statType") == stat_type]
    print(f"Found {len(filtered_players)} players with stat type: {stat_type}")

    if not filtered_players:
        print("No data to display for this stat type.")
        return

    sorted_players = sorted(filtered_players, key=lambda p: float(p.get("stat", 0) or 0), reverse=True)[:top_n]
    names = [p.get("player", "Unknown") for p in sorted_players]
    stats = [float(p.get("stat", 0)) for p in sorted_players]

    print(f"Players: {names}")
    print(f"Stats: {stats}")

    fig = go.Figure([go.Bar(x=names, y=stats)])
    fig.update_layout(
        title=f"Top {top_n} Players by {stat_type}",
        xaxis_title="Player",
        yaxis_title=stat_type,
        template="plotly_white"
    )
    fig.show()




