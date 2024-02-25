# song-analyzer
MP3 and WAV file analyzer for audio mixing/production


## Usage:
### Analyze individual .mp3 or .wav files:
```
~/github/jaykoll/song-analyzer main* 13s
❯ python main.py analyze /Users/jkolluru/Downloads/tose-naina.mp3
Analysis for /Users/jkolluru/Downloads/tose-naina.mp3:
  BPM: 129.20
  Key: ('E', '5A')
  Track Length: 8min 22s
```

### Analyze entire directory containing .mp3 or .wav files:
```
❯ python main.py analyze-playlist /Users/jkolluru/Desktop/tracks
+-----------------------------------------------------------------+--------------+---------+------------+
| Track Name                                                      | Key          |     BPM | Duration   |
+=================================================================+==============+=========+============+
| Bahramji_Maneesh_De_Moor_-_Dreamcatcher_Buddha_Bar_(mp3.pm).mp3 | ('B', '12B') | 129.199 | 7min 45s   |
+-----------------------------------------------------------------+--------------+---------+------------+
| tose-naina.mp3                                                  | ('E', '5A')  | 129.199 | 8min 22s   |
+-----------------------------------------------------------------+--------------+---------+------------+
| presto-you-are-mine.mp3                                         | ('G', '8A')  | 198.768 | 9min 15s   |
+-----------------------------------------------------------------+--------------+---------+------------+
```