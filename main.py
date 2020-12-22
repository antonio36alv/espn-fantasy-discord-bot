import requests

leagueID = 582628976
# leagueID = 835952
year = 2021
url = f"https://fantasy.espn.com/apis/v3/games/fba/seasons/{str(year)}/segments/0/leagues/{str(leagueID)}"
# url = f"https://fantasy.espn.com/apis/v3/games/fba/seasons/2020/segments/0/leagues/{leagueID}?rosterForTeamId={1}&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav"
# + \
#    "?seasonId=" + str(year)

# find player endpoint
# "https://site.api.espn.com/apis/fantasy/v2/games/fba/news/players?days=30&playerId=4277847"

r = requests.get(url, cookies = { "swid":"{23A4936D-D6C7-4DE4-81D9-9188358D2F69}",
"espn_s2":"AECb%2F6kEWSUPzUA1BEQB9DyFnpFwAucrxLZpHQvim4x%2BaUpNiZ2Azgd9EmZFk09B%2BlKACKtqYAl6FWk%2BGicGf4LMMYnHR0Nl9gU1L4jO2iNxIOZSL0%2B4Blgd%2BKqzOkzbsUn1YkzEhflxt%2FD1RNGYHutwoUPocda2XCJCkIYoyS9ZjDMOVg9E10c%2FTUqc7Z76NQPzVMlmvmDc0UCT7FS7tkcLgglu2oSudTM60AREtsKVvVFgRAvprTUl02PRjV1rWgfFDbwdifDGbHOyQ1a%2FMW9S"})

d = r.json()
# print(url)
print(d)

jawn = requests.get("https://fantasy.espn.com/apis/v3/games/fba/seasons/2021/players?scoringPeriodId=0&view=players_wl")
print("jawn")
print(jawn.json())
"""
espnAuth:"{"swid":"{23A4936D-D6C7-4DE4-81D9-9188358D2F69}"}"
espn_s2:"AECb%2F6kEWSUPzUA1BEQB9DyFnpFwAucrxLZpHQvim4x%2BaUpNiZ2Az
        gd9EmZFk09B%2BlKACKtqYAl6FWk%2BGicGf4LMMYnHR0Nl9gU1L4jO2iN
        xIOZSL0%2B4Blgd%2BKqzOkzbsUn1YkzEhflxt%2FD1RNGYHutwoUPocda
        2XCJCkIYoyS9ZjDMOVg9E10c%2FTUqc7Z76NQPzVMlmvmDc0UCT7FS7tkc
        Lgglu2oSudTM60AREtsKVvVFgRAvprTUl02PRjV1rWgfFDbwdifDGbHOyQ
        1a%2FMW9S"
"""