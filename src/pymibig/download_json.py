"""
Download JSON metadta files from MIBiG
"""

import os
import sys
import requests
from src.pymibig.console import console
from src.pymibig.constants import JSON_LINK, METADATA

def download_json(basedir: str) -> None:
    '''
    Download JSON files tar.gz compressed.
    '''
    if not os.path.exists(f'{basedir}/src/db/{METADATA}'):
        console.print('[bold green]Downloading MIBiG metadata...[/bold green]')
        try:
            resp = requests.get(JSON_LINK, stream=True, timeout=60)
            with open(f'{basedir}/src/db/{METADATA}', mode='wb') as file:
                for chunk in resp.iter_content(chunk_size=10*1024):
                    file.write(chunk)
        except PermissionError:
            console.print('[bold red]File can not be writen.[/bold red]')
            sys.exit()
        except requests.exceptions.RequestException:
            console.print('[bold red]Connection error or timed out.[/bold red]')
    else:
        console.print('[bold green]Loading JSON metadata...[/bold green]')
