#################################################################################
# Track Analyzer CLI
#################################################################################
import click
import os
import shutil
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor, as_completed
from .analyzer import analyze_track

#################################################################################
# Functions                
#################################################################################
def format_duration(duration):
    minutes, seconds = divmod(duration, 60)
    return f"{int(minutes)}min {int(seconds)}s"

def analyze_and_format(file_path):
    result = analyze_track(file_path)
    if result:
        return {
            'Track Name': os.path.basename(file_path),
            'Key': result['root_note'],
            'BPM': f"{result['bpm']:.2f}",
            'Duration': format_duration(result['duration'])
        }
    return None

def organize_track(file_path, result, base_dir):
    if result and 'root_note' in result:
        camelot_key = result['root_note'][1]  # Assuming root_note is a tuple ('C', '8B')
        target_dir = os.path.join(base_dir, camelot_key)
        os.makedirs(target_dir, exist_ok=True)
        new_path = os.path.join(target_dir, os.path.basename(file_path))
        shutil.move(file_path, new_path)
        return f"Moved {os.path.basename(file_path)} to {camelot_key}/"
    return None

@click.group()
def cli():
    """Song Analyzer CLI"""
    pass

@cli.command()
@click.argument('audio_file', type=click.Path(exists=True))
def analyze(audio_file):
    result = analyze_and_format(audio_file)
    if result:
        click.echo(f"Analysis for {audio_file}:")
        for key, value in result.items():
            click.echo(f"  {key}: {value}")
    else:
        click.echo(f"Failed to analyze {audio_file}", err=True)

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
@click.option('--threads', default=4, help='Number of threads to use for processing')
@click.option('--organize', is_flag=True, help='Organize tracks into subdirectories by Camelot key')
def analyze_playlist(directory, threads, organize):
    tracks_info = []
    audio_files = [os.path.join(root, file) 
                   for root, _, files in os.walk(directory) 
                   for file in files if file.lower().endswith(('.mp3', '.wav'))]

    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_file = {executor.submit(analyze_track, file): file for file in audio_files}
        for future in as_completed(future_to_file):
            file_path = future_to_file[future]
            result = future.result()
            if result:
                formatted_result = {
                    'Track Name': os.path.basename(file_path),
                    'Key': f"{result['root_note'][0]} ({result['root_note'][1]})",
                    'BPM': f"{result['bpm']:.2f}",
                    'Duration': format_duration(result['duration'])
                }
                tracks_info.append(formatted_result)
                
                if organize:
                    organize_message = organize_track(file_path, result, directory)
                    if organize_message:
                        click.echo(organize_message)

    if tracks_info:
        tracks_info.sort(key=lambda x: (x['Key'], x['Track Name']))
        headers = ['Track Name', 'Key', 'BPM', 'Duration']
        table = tabulate([info.values() for info in tracks_info], headers=headers, tablefmt='grid')
        click.echo(table)
    else:
        click.echo("No tracks were successfully analyzed.", err=True)

    if organize:
        click.echo("Tracks have been organized into subdirectories based on their Camelot keys.")
    else:
        click.echo("Tracks were analyzed but not organized. Use --organize flag to move files into Camelot key subdirectories.")

if __name__ == '__main__':
    cli()