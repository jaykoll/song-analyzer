# song-analyzer
MP3 and WAV file analyzer for audio mixing/production

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/song-analyzer.git
   cd song-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Analyze individual .mp3 or .wav files:
```
python main.py analyze /path/to/your/audio/file.mp3
```

Example output:
```
Welcome to the song-analyzer!
Analysis for /path/to/your/audio/file.mp3:
  Track Name: file.mp3
  Key: ('E', '5A')
  BPM: 129.20
  Duration: 8min 22s
```

### Analyze entire directory containing .mp3 or .wav files:
```
python main.py analyze-playlist /path/to/your/audio/directory
```

Example output:
```
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

### Using multiple threads for faster processing:

You can use the `--threads` option to specify the number of threads for parallel processing:

```
python main.py analyze-playlist /path/to/your/audio/directory --threads 8
```

This will use 8 threads for processing, which can significantly speed up the analysis of large directories.

## Features

- Analyzes MP3 and WAV files
- Extracts BPM (Beats Per Minute)
- Determines the musical key and its Camelot notation
- Calculates track duration
- Supports multi-threaded processing for faster analysis of multiple files

## Requirements

See `requirements.txt` for a list of Python dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.