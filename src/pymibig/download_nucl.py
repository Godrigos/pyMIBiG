"""
Download FASTa file from MIBiG
"""

import os
import sys
import requests
from rich.progress import track
from src.pymibig.console import console
from src.pymibig.constants import GBK_LINK, DATABASE, CHUNK_SIZE

def download_nucl(basedir: str) -> None:
    '''
    Download FASTa file.
    '''
    if not os.path.exists(f'{basedir}/src/db/{DATABASE}'):
        try:
            resp = requests.get(GBK_LINK, stream=True, timeout=60)
            total_size = int(resp.headers.get('content-length', 0))
            with open(f'{basedir}/src/db/{DATABASE}', mode='wb') as file:
                for chunk in track(resp.iter_content(chunk_size=CHUNK_SIZE),
                description='[bold green]Downloading sequences as GBK...[/bold green]',
                total=total_size / CHUNK_SIZE):
                    file.write(chunk)
        except PermissionError:
            console.print('[bold red]File can not be writen.[/bold red]')
            sys.exit()
        except requests.exceptions.RequestException:
            console.print('[bold red]Connection error or timed out.[/bold red]')
    else:
        console.print('[bold green]Loading GBK sequences...[/bold green]')
