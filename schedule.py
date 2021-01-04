import requests
from bs4 import BeautifulSoup
# from datetime import date
import datetime

# date = str(date.today()).replace("-", "")
date = "20201225"
URL = f"https://www.cbssports.com/nba/scoreboard/{date}/"

# TODO mimic headers from other projs
r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")

tb = soup.find_all("tbody")
live = soup.find_all("div", class_ = "live-update")
print(len(tb))
print(str(date).replace("-", ""))
print(URL)
print(len(live))
print(live[0])

# team1 = 
print("Today's games:")
for x in live:
    aS = x.find_all("a")
    sp = x.find_all("span")
    print(f"{sp[0].text.strip()} {aS[1].text} @ {aS[3].text}")

for x in range(6):
    nextDate = date + datetime.timedelta(days = x)