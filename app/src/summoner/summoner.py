from . import constants
import requests
import sys
import json





class summoner():

    def __init__(self, uname):

        self.data = {}
        self.data['username']= uname
        api_url = constants.usernameGrabBase + uname
        req = requests.get(api_url, headers = constants.headers)
        if(req.status_code == 200):
            self.data['accountID'] = json.loads(req.content.decode('utf-8'))['accountId']
        else:
            print("GET username failed, error code" + str(req.status_code))
            sys.exit()

    def getMatches(self):
        api_url = constants.MatchGrabBase + self.data['accountID']
        for index in range(1):
            if(index != 0):
                api_url += '?beginIndex=' + str(index)
            api_url += '&queue=400&queue=420&queue=430&queue=440'
            req = requests.get(api_url, headers = constants.headers)
            if(req.status_code == 200):
                self.data['matchlist'] = json.loads(req.content.decode('utf-8'))
            else:
                print(api_url)
                print("GET matchlist failed, error code" + str(req.status_code))
                sys.exit()



