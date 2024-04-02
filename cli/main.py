import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()

def version_callback(value: bool):
    if value:
        typer.echo('CPM Version: v1.23')
        raise typer.Exit()

@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(None, '--version', callback=version_callback),
): 
    pass

@app.command("list")
def sample_func():
    subprocess.run("dir", shell=True)

@app.command('hello')
def sample_func():
    rprint('[red bold]Hi[/red bold] [yellow]World![/yellow]')


if __name__ == '__main__':
    app()
