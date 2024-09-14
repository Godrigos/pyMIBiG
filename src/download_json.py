"""
Download JSON metadta files from MIBiG
"""

import sys
import requests
from src.console import console
from src.constants import JSON

def download_json() -> None:
    '''
    Download JSON files tar.gz compressed.
    '''
    console.print('[bold green]Downloading MIBiG metadata...[/bold green]')
    
    try:
        resp = requests.get(JSON, stream=True, timeout=60)
        with open('mibig_json_3.1.tar.gz', mode='wb') as file:
            for chunk in resp.iter_content(chunk_size=10*1024):
                file.write(chunk)
    except PermissionError:
        console.print('[bold red]File can not be writen.[/bold red]')
        sys.exit()
    except requests.exceptions.RequestException:
        console.print('[bold red]Connection error or timed out.[/bold red]')
