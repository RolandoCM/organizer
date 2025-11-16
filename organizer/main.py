import sys
import typer

app = typer.Typer()

@app.command()
def hello(name:str):
    # Add your main logic here
    
    ## exit when press Enter
    input("Press Enter to exit...")

@app.command()
def goodbye(name:str):
    # Add your main logic here
    
    ## exit when press Enter
    input("Press Enter to exit...")
if __name__ == "__main__":
    app()
