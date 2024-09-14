"""
Uncompress the downloaded tar.gz file containing the JSON metadata.
"""

import sys
import os
import tarfile
from src.console import console

def uncompress_json() -> None:
    '''
    Uncompress downloaded tar.gz file.
    '''
    console.print('[bold green]Uncompressing metadata...[/bold green]')

    try:
        with tarfile.open('mibig_json_3.1.tar.gz') as tar:
            tar.extractall()
        os.remove('mibig_json_3.1.tar.gz')
    except FileNotFoundError:
        console.print('[bold red]mibig_json_3.1.tar.gz not found.[/bold red]')
        sys.exit()
    except PermissionError:
        console.print(
            '[bold red]Permission to uncompress file denied.[/bold red]'
            )
        sys.exit()
