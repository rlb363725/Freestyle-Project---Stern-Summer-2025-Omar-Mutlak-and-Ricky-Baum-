import os
import requests

API_KEY = os.getenv("CFB_API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def get_roster(team, year):
    url = f"https://api.collegefootballdata.com/roster?team={team}&year={year}"
    return requests.get(url, headers=HEADERS).json()


def get_team_stats(team, year):
    url = f"https://api.collegefootballdata.com/stats/season?team={team}&year={year}"
    return requests.get(url, headers=HEADERS).json()


def get_player_stats(year, category="passing"):
    url = f"https://api.collegefootballdata.com/stats/player/season?year={year}&category={category}"
    return requests.get(url, headers=HEADERS).json()









