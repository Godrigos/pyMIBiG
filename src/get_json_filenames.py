"""
List the JSON filenames
"""

import sys
import os
from src.console import console

def get_json_filenames() -> list:
    '''
    Return a list of JSON filenames
    '''
    console.print('[bold green]Generating target access codes...[/bold green]')

    try:
        return [file for file in os.listdir('mibig_json_3.1') if file.endswith('.json')]
    except PermissionError:
        console.print(
            '[bold red]Permission to read directory denied.[/bold red]'
            )
        sys.exit()
    except FileNotFoundError:
        console.print('[bold red]File not found.[/bold red]')
        sys.exit()
