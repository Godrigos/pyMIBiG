"""
Download FASTa file from MIBiG
"""

import os
import sys
import gzip
import requests
from rich.progress import track
from src.pymibig.console import console
from src.pymibig.constants import FASTA_LINK, PROTEIN, CHUNK_SIZE

def download_prot(basedir: str) -> None:
    '''
    Download FASTa file.
    '''
    if not os.path.exists(f'{basedir}/src/db/{PROTEIN}'):
        try:
            resp = requests.get(FASTA_LINK, stream=True, timeout=60)
            total_size = int(resp.headers.get('content-length', 0))
            with gzip.open(f'{basedir}/src/db/{PROTEIN}', mode='wb') as file:
                for chunk in track(resp.iter_content(chunk_size=CHUNK_SIZE),
                description='[bold green]Downloading amino acids as FASTa...[/bold green]',
                total=total_size / CHUNK_SIZE):
                    file.write(chunk)
        except PermissionError:
            console.print('[bold red]File can not be writen.[/bold red]')
            sys.exit()
        except requests.exceptions.RequestException:
            console.print('[bold red]Connection error or timed out.[/bold red]')
    else:
        console.print('[bold green]Loading protein sequences...[/bold green]')
