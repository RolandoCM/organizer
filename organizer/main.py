import sys
import os
import typer

app = typer.Typer()

photos_extensions = ('.jpg','.jpeg', '.png')

@app.command()
def organize(type: str):
    if type == "photos":
        typer.echo("Organizing photos...")
        # Add logic to organize photos here
    elif type == "documents":
        typer.echo("Organizing documents...")
        # Add logic to organize documents here
@app.command()
def organize_folders(source: str):
    typer.echo("Organizing folders...")
    # Add logic to organize folders here
    """read folder structure from source path and organize files into subfolders based on file types"""
    files = os.listdir(source)
    for file in files:
        if file.endswith(photos_extensions):
            typer.echo(f"Moving photo file: {file}")
            # Logic to move photo files into a 'Photos' subfolder
            if not os.path.exists(os.path.join(source, 'Photos')):
                os.makedirs(os.path.join(source, 'Photos'))
            os.rename(os.path.join(source, file), os.path.join(source, 'Photos', file))
            typer.echo(f"Moved {file} to Photos folder.")
        else:
            typer.echo(f"Skipping non-photo file: {file}")
@app.command()
def organize_with_pattern(source: str, pattern: str):
    typer.echo(f"Organizing files in {source} with pattern {pattern}...")
    # Add logic to organize files based on the given pattern here

@app.command()
def organize_ends_with(source: str, suffix: str):
    typer.echo(f"Organizing files in {source} that end with {suffix}...")
    # Add logic to organize files that end with the given suffix here
@app.command()
def organize_starts_with(source: str, target: str, prefix: str):
    typer.echo(f"Organizing files in {source} that start with {prefix}...")
    # Add logic to organize files that start with the given prefix here}
    files = os.listdir(source)
    for file in files:
        if file.startswith(prefix):
            typer.echo(f"Moving file: {file}")
            # Logic to move files that start with the given prefix into a subfolder
            target_folder = os.path.join(source, target)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            os.rename(os.path.join(source, file), os.path.join(target_folder, file))
            typer.echo(f"Moved {file} to {target_folder}.")
        else:
            typer.echo(f"Skipping file: {file}")
    
    

if __name__ == "__main__":
    app()
