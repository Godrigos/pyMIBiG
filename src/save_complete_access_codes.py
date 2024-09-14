"""
Save target's complete BGCs access codes.
"""

import sys
import json
from src.console import console

def save_complete_access_codes(target:str, json_files: list) -> list:
    '''
    Create a txt file listing json filenames
    '''
    console.print('[bold green]Saving target access codes...[/bold green]')
    access_codes: list = []

    try:
        for file in json_files:
            with open(f'./mibig_json_3.1/{file}', encoding='utf-8') as handle:
                data = json.load(handle)
                if (data['cluster']['loci']['completeness'] == "complete" and
                    target in data['cluster']['organism_name']):
                    access_codes.append(data['cluster']['mibig_accession'])

        with open(f'{target}_access_codes.txt', 'wt', encoding='utf-8') as  codes:
            codes.write('\n'.join(str(i) for i in access_codes))
        return access_codes
    except PermissionError:
        console.print(
            '[bold red]Permission to read directory or write file denied.[/bold red]'
            )
        sys.exit()
    except FileNotFoundError:
        console.print(f'[bold red]{file} not found.[/bold red]')
        sys.exit()
