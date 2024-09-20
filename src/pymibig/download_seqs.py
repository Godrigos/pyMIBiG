"""
Download FASTa file from MIBiG
"""

import os
import sys
import requests
from rich.progress import track
from src.pymibig.console import console
from src.pymibig.constants import GBK_LINK, DATABASE

def download_seqs(basedir: str) -> None:
    '''
    Download FASTa file.
    '''
    if not os.path.exists(f'{basedir}/src/db/{DATABASE}'):
        try:
            resp = requests.get(GBK_LINK, stream=True, timeout=60)
            total_size = int(resp.headers.get('content-length', 0))
            chunk_size = 10*1024
            with open(f'{basedir}/src/db/{DATABASE}', mode='wb') as file:
                for chunk in track(resp.iter_content(chunk_size=chunk_size),
                description='[bold green]Downloading sequences as GBK...[/bold green]',
                total=total_size / chunk_size):
                    file.write(chunk)
        except PermissionError:
            console.print('[bold red]File can not be writen.[/bold red]')
            sys.exit()
        except requests.exceptions.RequestException:
            console.print('[bold red]Connection error or timed out.[/bold red]')
    else:
        console.print('[bold green]Loading GBK sequences...[/bold green]')
