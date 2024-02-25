# song-analyzer
MP3 and WAV file analyzer for audio mixing/production


## Usage:
### Analyze individual .mp3 or .wav files:
```
❯ python main.py analyze /Users/jkolluru/Desktop/tracks/test.mp3
Welcome to the song-analyzer!
Analysis for /Users/jkolluru/Desktop/tracks/test.mp3:
  BPM: 129.20
  Key: ('E', '5A')
  Track Length: 8min 22s
```

### Analyze entire directory containing .mp3 or .wav files:
```
❯ python main.py analyze-playlist /Users/jkolluru/Desktop/tracks
Welcome to the song-analyzer!
+-------------------------+--------------+---------+------------+
| Track Name              | Key          |     BPM | Duration   |
+=========================+==============+=========+============+
| dreamcatcher.mp3        | ('B', '12B') | 129.199 | 7min 45s   |
+-------------------------+--------------+---------+------------+
| test.mp3                | ('E', '5A')  | 129.199 | 8min 22s   |
+-------------------------+--------------+---------+------------+
| presto-you-are-mine.mp3 | ('G', '8A')  | 198.768 | 9min 15s   |
+-------------------------+--------------+---------+------------+
```