# lol-coach-cli
![team banner](team-banner.png)

Request league of legends champion counter picks or tips for playing against them. Get responses over CLI + Audio.

Uses crowdsourced data scraped from [championselect.net](http://www.championselect.net/)

Built at the 2017 Riot Hackathon


## To run:

`$ python3 lol-coach.py`

### Example - Counterpicks
```
walsh-mbp:lol-coach-cli nwalsh$ python3 lol-coach.py
Enter: What champion are you having trouble with?
Ahri
Would you like a Counter pick or a tip? Type `counter` or `tip`
counter
Strong counters for Ahri are: Annie, Diana, Kassadin, Talon, Swain
```

### Example - Tips
```
walsh-mbp:lol-coach-cli nwalsh$ python3 lol-coach.py
Enter: What champion are you having trouble with?
Teemo
Would you like a Counter pick or a tip? Type `counter` or `tip`
tip
Teemo is weak against gap closers, as his Move Quick is on a long cooldown.
```

### Future

- Computer Vision algorithm for auto-detecting champions/items (`tabled-features/cv-hero-item-detection/`)
- Transition input from CLI to Voice using Amazon Polly (`tabled-features/amazon-polly-voice-interface/`)
- Host as a public API or Discord Bot, since most gamers already use this as a natural VX interface
