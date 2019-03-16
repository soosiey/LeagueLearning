import argparse
import json
import requests


parser = argparse.ArgumentParser(description = 'Get LoL user information')
parser.add_argument('username', metavar='uname', type=str, help='username of the user')
args = parser.parse_args()


def getSumInfo(username):

    api_url_base = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    headers={
        "Origin": None,
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": "RGAPI-92b42658-cacf-48dd-976f-a6381290854a",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
    }
    api_url = api_url_base + username
    req = requests.get(api_url, headers=headers)
    if req.status_code == 200:
        return True, json.loads(req.content.decode('utf-8'))
    else:
        return False ,"fail: " + str(req.status_code)

def getMatchlist(accountID):
    api_url_base = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
    headers={
        "Origin": None,
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": "RGAPI-92b42658-cacf-48dd-976f-a6381290854a",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
    }
    api_url = api_url_base + accountID
    req = requests.get(api_url, headers=headers)
    if req.status_code == 200:
        return True, json.loads(req.content.decode('utf-8'))
    else:
        return False ,"fail: " + str(req.status_code)

success, info = getSumInfo(args.username)
if(not success):
    print(info)
else:
    accountID = info['accountId']
    getMatchesSuccess,matchesinfo = getMatchlist(accountID)

