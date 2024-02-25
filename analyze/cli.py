#################################################################################
# Track Analyzer CLI
#################################################################################
import click
import os
from tabulate import tabulate
from .analyzer import librosa, get_bpm, get_root_note, get_track_length

#################################################################################
# Functions                
#################################################################################
def analyze_track(audio_file):
    """
    Analyze a single track.
    """
    try:
        y, sr = librosa.load(audio_file)
        tempo = get_bpm(audio_file)
        root_note = get_root_note(audio_file)
        duration = get_track_length(audio_file)
        minutes, seconds = divmod(duration, 60)

        click.echo(f"Analysis for {audio_file}:")
        click.echo(f"  BPM: {tempo:.2f}")
        click.echo(f"  Key: {root_note}")
        click.echo(f"  Track Length: {int(minutes)}min {int(seconds)}s")

    except Exception as e:
        click.echo(f"Error analyzing {audio_file}: {str(e)}", err=True)
        raise

def analyze_directory(directory):
    """
    Analyze all tracks in a directory and print a table grouped by root note key.
    """
    tracks_info = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp3', '.wav')):
                file_path = os.path.join(root, file)
                try:
                    # Load the audio file using librosa
                    y, sr = librosa.load(file_path)

                    root_note = get_root_note(file_path)
                    duration = get_track_length(file_path)
                    minutes, seconds = divmod(duration, 60)

                    tracks_info.append({
                        'Track Name': file,
                        'Key': root_note,
                        'BPM': get_bpm(file_path),
                        'Duration': f"{int(minutes)}min {int(seconds)}s"
                    })

                except Exception as e:
                    click.echo(f"Error analyzing {file_path}: {str(e)}", err=True)

    # Sort tracks by key and then by track name
    tracks_info.sort(key=lambda x: (x['Key'], x['Track Name']))

    # Define the order of headers based on your preference
    headers = ['Track Name', 'Key', 'BPM', 'Duration']

    # Print the table
    table = tabulate([info.values() for info in tracks_info], headers=headers, tablefmt='grid')
    click.echo(table)

def helper_function():
    click.echo("This is a helper command. You can add your helper functionality here.")


@click.command()
@click.argument('audio_file', type=click.Path(exists=True))
def analyze(audio_file):
    analyze_track(audio_file)

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
def analyze_playlist(directory):
    analyze_directory(directory)

@click.command()
def helper():
    helper_function()    

cli = click.Group()
cli.add_command(analyze)
cli.add_command(analyze_playlist)
cli.add_command(helper)