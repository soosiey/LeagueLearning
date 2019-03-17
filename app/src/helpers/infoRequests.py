import json
import requests
from helpers.constants import *

def getSumInfo(username):

    api_url = usernameGrabBase + username
    req = requests.get(api_url, headers=headers)
    if req.status_code == 200:
        return True, json.loads(req.content.decode('utf-8'))
    else:
        return False ,"GET username failed, error code" + str(req.status_code)

def getMatchlist(accountID):

    api_url = MatchGrabBase + accountID
    req = requests.get(api_url, headers=headers)
    if req.status_code == 200:
        return True, json.loads(req.content.decode('utf-8'))
    else:
        return False ,"GET matchlist failed, error code" + str(req.status_code)


def processMatch(matchID):
    api_url = MatchInfoGrab + str(matchID)
    req = requests.get(api_url, headers=headers)

    if(req.status_code == 200):
        return True, json.loads(req.content.decode('utf-8'))
    else:
        return False, "GET match info failed, error code", str(req.status_code)
