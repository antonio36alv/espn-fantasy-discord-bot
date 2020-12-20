import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.espn.com/nba/team/roster/_/name/lal/los-angelos-lakers"
# find out if second element is two words or one or just split and loop through that list
# baseUrl = f"https://www.espn.com/nba/team/roster/_/name/{abbr}/{arr[]}

r = requests.get(f"{baseUrl}/lal/los-angelos-lakers")