import keys

usernameGrabBase = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
headers={
        "Origin": None,
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": keys.api_token,
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
    }

MatchGrabBase = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
MatchInfoGrab = "https://na1.api.riotgames.com/lol/match/v4/matches/"
