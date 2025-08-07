from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def team_rosters():
    florida_roster = [
        {"name": "John Doe", "position": "QB", "jersey": 15},
        {"name": "Mike Smith", "position": "RB", "jersey": 27}
        # ... your dynamically fetched data
    ]

    alabama_roster = [
        {"name": "Jane Taylor", "position": "WR", "jersey": 5},
        {"name": "Tom White", "position": "DL", "jersey": 96}
        # ... your dynamically fetched data
    ]

    return render_template("rosters.html",
                           team1_name="Florida",
                           team2_name="Alabama",
                           team1_roster=florida_roster,
                           team2_roster=alabama_roster)

if __name__ == '__main__':
    app.run(debug=True)
