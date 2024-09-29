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
            'Key': f"{result['root_note'][0]} ({result['root_note'][1]})",
            'BPM': f"{result['bpm']:.2f}",
            'Duration': format_duration(result['duration'])
        }
    return None

def organize_track(file_path, result, base_dir):
    if result and 'root_note' in result:
        camelot_key = result['root_note'][1]
        target_dir = os.path.join(base_dir, camelot_key)
        os.makedirs(target_dir, exist_ok=True)
        new_path = os.path.join(target_dir, os.path.basename(file_path))
        shutil.move(file_path, new_path)
        return f"Moved {os.path.basename(file_path)} to {camelot_key}/"
    return None

@click.command()
@click.argument('path', type=click.Path(exists=True), required=False)
@click.option('--organize', is_flag=True, help='Organize tracks into subdirectories by Camelot key')
@click.option('--threads', default=4, help='Number of threads to use for processing')
def cli(path, organize, threads):
    """Analyze audio files in the current directory or a specific file/directory."""
    if path and os.path.isfile(path):
        # Analyze single file
        result = analyze_and_format(path)
        if result:
            click.echo(f"Analysis for {path}:")
            for key, value in result.items():
                click.echo(f"  {key}: {value}")
        else:
            click.echo(f"Failed to analyze {path}", err=True)
    else:
        # Analyze directory
        directory = path if path and os.path.isdir(path) else os.getcwd()
        audio_files = [os.path.join(root, file) 
                       for root, _, files in os.walk(directory) 
                       for file in files if file.lower().endswith(('.mp3', '.wav'))]

        tracks_info = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            future_to_file = {executor.submit(analyze_and_format, file): file for file in audio_files}
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                result = future.result()
                if result:
                    tracks_info.append(result)
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