# song-analyzer

A CLI tool for analyzing audio files (MP3 and WAV) to extract information such as BPM, key, and duration.

## Installation

You can install song-analyzer directly from PyPI:

```
pip install song-analyzer
```

## Usage

After installation, you can use the `song-analyzer` command directly:

### Analyze all tracks in the current directory:

```
song-analyzer
```

### Analyze and organize tracks in the current directory:

```
song-analyzer --organize
```

### Analyze a specific file:

```
song-analyzer path/to/your/audio/file.mp3
```

### Analyze all tracks in a specific directory:

```
song-analyzer path/to/your/audio/directory
```

### Analyze and organize tracks in a specific directory:

```
song-analyzer path/to/your/audio/directory --organize
```

### Specify the number of threads for processing:

```
song-analyzer --threads 8
```

## Features

- Analyzes MP3 and WAV files
- Extracts BPM (Beats Per Minute)
- Determines the musical key and its Camelot notation
- Calculates track duration
- Supports multi-threaded processing for faster analysis of multiple files
- Option to organize tracks into subdirectories based on Camelot keys

## Requirements

See `requirements.txt` for a list of Python dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.