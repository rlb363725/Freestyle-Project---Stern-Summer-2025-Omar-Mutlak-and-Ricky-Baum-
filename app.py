from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_rosters():
    # Simulated API data: list of dictionaries with full player info
    ohio_state_roster = [
        {"name": "Marvin Harrison Jr.", "position": "WR", "jersey": 18},
        {"name": "Tommy Eichenberg", "position": "LB", "jersey": 35},
        {"name": "Kyle McCord", "position": "QB", "jersey": 6},
        # ...more players
    ]

    rutgers_roster = [
        {"name": "Samuel Brown V", "position": "RB", "jersey": 27},
        {"name": "Gavin Wimsatt", "position": "QB", "jersey": 2},
        {"name": "Tyreem Powell", "position": "LB", "jersey": 22},
        # ...more players
    ]

    return render_template("rosters.html",
                           team1_name="Ohio State",
                           team2_name="Rutgers",
                           team1_roster=ohio_state_roster,
                           team2_roster=rutgers_roster)

if __name__ == "__main__":
    app.run(debug=True)

