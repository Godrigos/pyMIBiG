"""
Download FASTa file from MIBiG
"""

import os
import sys
import requests
from src.console import console
from src.constants import FASTA

def download_fasta(basedir: str) -> None:
    '''
    Download FASTa file.
    '''
    if not os.path.exists(f'{basedir}/db/mibig_prot_seqs_3.1.fasta'):
        console.print(
            '[bold green]Downloading sequences as FASTa...[/bold green]'
            )
        try:
            resp = requests.get(FASTA, stream=True, timeout=60)
            with open(f'{basedir}/db/mibig_prot_seqs_3.1.fasta', mode='wb') as file:
                for chunk in resp.iter_content(chunk_size=10*1024):
                    file.write(chunk)
        except PermissionError:
            console.print('[bold red]File can not be writen.[/bold red]')
            sys.exit()
        except requests.exceptions.RequestException:
            console.print('[bold red]Connection error or timed out.[/bold red]')
    else:
        console.print('[bold green]Loading FASTa sequences...[/bold green]')
