import argparse
import helpers.infoRequests as infoRequests
import time
import sys

parser = argparse.ArgumentParser(description = 'Get LoL user information')
parser.add_argument('filename', metavar='f', type=str, help='name of the file holding json data')
args = parser.parse_args()

"""
success, info = infoRequests.getSumInfo(args.username)

if(not success):
    print(info)
    sys.exit(0)

accountID = info['accountId']
getMatchesSuccess,matchesinfo = infoRequests.getMatchlist(accountID)
if(not getMatchesSuccess):
    print(matchesinfo)
    sys.exit(0)

w,m = breakMatches(matchesinfo)
print("Recent W/L Ratio in", m, "games:",float(w)/float(m))"""

import helpers.dataMove as dataMove

dataMove.move()
