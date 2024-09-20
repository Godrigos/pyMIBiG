"""
Download FASTa file from MIBiG
"""

import os
import sys
import requests
from src.pymibig.console import console
from src.pymibig.constants import GBK_LINK, DATABASE

def download_seqs(basedir: str) -> None:
    '''
    Download FASTa file.
    '''
    if not os.path.exists(f'{basedir}/src/db/{DATABASE}'):
        try:
            resp = requests.get(GBK_LINK, stream=True, timeout=60)
            with console.status(
                '[bold green]Downloading sequences as GBK...[/bold green]'
                ):
                with open(f'{basedir}/src/db/{DATABASE}', mode='wb') as file:
                    for chunk in resp.iter_content(chunk_size=10*1024):
                        file.write(chunk)
        except PermissionError:
            console.print('[bold red]File can not be writen.[/bold red]')
            sys.exit()
        except requests.exceptions.RequestException:
            console.print('[bold red]Connection error or timed out.[/bold red]')
    else:
        console.status('[bold green]Loading GBK sequences...[/bold green]')
