import librosa
import numpy as np

def get_bpm(audio_file):
    try:
        # Load audio file
        y, sr = librosa.load(audio_file)

        # Get bpm
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        return tempo
    except librosa.util.exceptions.ParameterError as pe:
        print(f"Error loading audio file: {str(pe)}")
        raise  # Re-raise the exception to stop further processing
    except Exception as e:
        print(f"Error analyzing the track: {str(e)}")
        raise

def get_root_note(audio_file):
    try:
        # Load the audio file using librosa
        y, sr = librosa.load(audio_file)

        # Calculate chromagram
        chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

        # Find the most prominent pitch class
        root_pitch_class = np.argmax(np.mean(chromagram, axis=1))

        # Define key mappings
        chroma_to_key = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # Find the key by selecting the maximum chroma feature
        estimated_key = chroma_to_key[root_pitch_class]

        # Convert to Camelot value
        camelot = midi_to_camelot(root_pitch_class)
        return estimated_key, camelot
    except Exception as e:
        print(f"Error analyzing the root note: {str(e)}")
        raise

def get_track_length(audio_file):
    try:
        # Get track duration
        duration = librosa.get_duration(path=audio_file)
        return duration
    except Exception as e:
        print(f"Error getting track length: {str(e)}")
        raise

def get_camelot_key_from_root(root_note):
    # Map note name to Camelot key
    camelot_key = {'C': 1, 'C#': 2, 'D': 3, 'D#': 4, 'E': 5, 'F': 6, 'F#': 7, 'G': 8, 'G#': 9, 'A': 10, 'A#': 11, 'B': 12}

    # Determine major or minor
    mode = "major" if "major" in root_note else "minor"

    # Get the Camelot key
    key_number = camelot_key[root_note[:-1]]
    camelot_key_str = f"{key_number}{mode}"
    return camelot_key_str

def midi_to_camelot(midi_note):
    # Define the pitch classes and their corresponding Camelot keys
    pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    camelot_keys = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A', '12A', '1B', '2B', '3B', '4B', '5B', '6B', '7B', '8B', '9B', '10B', '11B', '12B']

    # Extract the pitch class and octave from the MIDI note
    pitch_class = pitch_classes[midi_note % 12]
    octave = (midi_note // 12) - 1  # MIDI octave numbering starts from -1

    # Find the Camelot key
    camelot_key = camelot_keys[(midi_note % 12) + (12 if pitch_class in ['A', 'A#', 'B'] else 0)]
    return camelot_key

#################################################################################
# Beta Functions - Coming Soon!                
#################################################################################
# def get_beat_locations(audio_file):
#     try:
#         # Load audio file
#         y, sr = librosa.load(audio_file)

#         # Get beat locations
#         _, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#         beat_locations = librosa.frames_to_time(beat_frames, sr=sr)

#         return beat_locations
#     except Exception as e:
#         print(f"Error extracting beat locations: {str(e)}")
#         raise

# def get_onset_envelopes(audio_file):
#     try:
#         # Load audio file
#         y, sr = librosa.load(audio_file)

#         # Get onset envelopes
#         onset_env = librosa.onset.onset_strength(y=y, sr=sr)

#         return onset_env
#     except Exception as e:
#         print(f"Error extracting onset envelopes: {str(e)}")
#         raise

# def get_tempo_changes(audio_file):
#     try:
#         # Load audio file
#         y, sr = librosa.load(audio_file)

#         # Get tempo changes
#         onset_env = librosa.onset.onset_strength(y=y, sr=sr)
#         tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, trim=False)

#         return tempo
#     except Exception as e:
#         print(f"Error extracting tempo changes: {str(e)}")
#         raise

# def get_key_changes(audio_file):
#     try:
#         # Load audio file
#         y, sr = librosa.load(audio_file)

#         # Calculate chromagram
#         chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

#         # Sum the chroma features to get key changes
#         key_changes = np.sum(chromagram, axis=1)

#         # Get the index of the maximum key change
#         key_index = np.argmax(key_changes)

#         # Get the corresponding key name
#         key_name = librosa.midi_to_note(key_index)

#         return key_name
#     except Exception as e:
#         print(f"Error extracting key changes: {str(e)}")
#         raise
#################################################################################
