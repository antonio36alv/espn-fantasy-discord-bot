import requests

leagueID = 582628976
year = 2020
url = f"https://fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{str(leagueID)}"
# + \
#    "?seasonId=" + str(year)

r = requests.get(url)
d = r.json()
print(url)
print(d)

"""
espnAuth:"{"swid":"{23A4936D-D6C7-4DE4-81D9-9188358D2F69}"}"
espn_s2:"AECb%2F6kEWSUPzUA1BEQB9DyFnpFwAucrxLZpHQvim4x%2BaUpNiZ2Az
        gd9EmZFk09B%2BlKACKtqYAl6FWk%2BGicGf4LMMYnHR0Nl9gU1L4jO2iN
        xIOZSL0%2B4Blgd%2BKqzOkzbsUn1YkzEhflxt%2FD1RNGYHutwoUPocda
        2XCJCkIYoyS9ZjDMOVg9E10c%2FTUqc7Z76NQPzVMlmvmDc0UCT7FS7tkc
        Lgglu2oSudTM60AREtsKVvVFgRAvprTUl02PRjV1rWgfFDbwdifDGbHOyQ
        1a%2FMW9S"
"""