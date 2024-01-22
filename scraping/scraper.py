import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# TODO: Implement scraper functionalities
# Looks like ESPN starting from this page has the best match reports so far
# https://www.espn.com/soccer/fixtures?league=eng.1
# Example game https://www.espn.com/soccer/report/_/gameId/671070
# For each URL, I will have a selector and a URL

# Use this URL: https://www.espn.com/soccer/schedule/_/date/20230902/league/eng.1
# Where this is the previous day to today: 20230902
# Convert to this format Saturday, September 2, 2023
# Search for hrefs game ids that are a child of that date
# Send requests to these endpoints https://www.espn.com/soccer/report/_/gameId/671070
# Retrieve and print

# in actuality i may just want to get all the gameids
# then check if i have already scraped them
# if not, then scrape them

# so for now lets just scrape one game id


# Constants for URLs
INDEX_URL = "https://www.espn.com/soccer/schedule/_/date/{}/league/eng.1"
GAME_REPORT_URL = "https://www.espn.com/soccer/report/_/gameId/{}"

def fetch_and_parse(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Error fetching {url}: Status code {response.status_code}")
        return None

def scrape_game_report(game_id):
    url = GAME_REPORT_URL.format(game_id)
    print(f"Visiting {url}")
    soup = fetch_and_parse(url)
    if soup:
        report = soup.find('div', class_='Story__Body t__body')
        if report:
            return report.get_text()

def fetch_html_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error fetching {url}: Status code {response.status_code}")
        return None

def scrape_schedule(date):
    url = INDEX_URL.format(date.strftime('%Y%m%d'))
    print(f"Visiting {url}")

    # later this may get all of the game ids in the index page and scrape them
    # html_content = fetch_html_content(url)
    return "671070"




