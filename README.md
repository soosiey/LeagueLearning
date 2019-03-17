# League Learning

League Learning is a python tool that will allow you to see stats of League of Legends players as well as make educated guesses about outcomes of games. Work in progress.

## Currently finished:

    * Basic W/L statistic for recent games

## Need to do:

    * Get ability to poll player game status (in game or not)
    * Perform a learning test on test data set -> logistic regression
    * Perform a test on the fly at various points throughout a game
    * Wrap up project into a simple user interface
## Extras:

    * Possibly data visualization of various stats
    * Bayesian Inferencing in real-time for players in game (need a thorough GUI for ease of input, API does not allow for spectator mode in real-time)


# Usage:

To use, run the lol script in app/bin. You will need a developer key from the Riot API website which can be found [here](https://developer.riotgames.com/), and you have to put it into app/src/api_keys/keys.py as follows:

```python
api_token = <key>
```

This process must change. Maybe ask user to input? (This is not great either, keys must be private).
