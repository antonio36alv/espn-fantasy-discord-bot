import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.espn.com/nba/team/roster/_/name/lal/los-angelos-lakers"
# find out if second element is two words or one or just split and loop through that list
# baseUrl = f"https://www.espn.com/nba/team/roster/_/name/{abbr}/{arr[]}

r = requests.get(f"{baseUrl}/lal/los-angelos-lakers")
soup = BeautifulSoup(r.content, "html.parser")

# anchors with following criteria (anchor class is explicitly AnchorLink) conatins double for players
unfilteredPlayersList = soup.find_all(lambda x: x.name == 'a' and ''.join(x.get('class', list())) == 'AnchorLink')
# filter array, take every even index
filteredPlayersList = unfilteredPlayersList[1::2]
# then loop through remaining
for x in filteredPlayersList:
    # get href, split by /
    # /id/firstName-lastName
    deliHref = x["href"].split("/")
    playerId = deliHref[-2]
    # split full name by -
    playerFullNameSplit = deliHref[-1].split("-")
    # as of now we assume first is the first name
    playerFistName = playerFullNameSplit[0]
    # the last is the last name, which could be a two part last name either way join it
    playerLastName = " ".join(playerFullNameSplit[1:])
