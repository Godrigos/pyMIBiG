"""
Save target's BGCs access codes.
"""

import sys
import json
import tarfile
from itertools import islice
import pandas as pd
from rich.progress import track
from src.pymibig.console import console
from src.pymibig.treat_args import treat_args
from src.pymibig.constants import METADATA

def save_access_codes(args, basedir) -> list:
    '''
    Create a txt file listing BGCs codes

    Arguments:
    args -- object of class Args containing user inputs
    basedir -- main module path
    '''
    df = pd.DataFrame(
        columns=['Code', 'Organism', 'Compounds', 'Biosynthetic Class',
                 'Completeness', 'Minimal']
        )

    try:
        with tarfile.open(f'{basedir}/src/db/{METADATA}') as tar:
            for member in track(islice(tar, 1, None),
            description='[bold green]Searching target access '
                        'codes...[/bold green]',
            total=len(tar.getmembers())-1):
                with tar.extractfile(member) as handle:
                    data = json.load(handle)
                if treat_args(data, args):
                    df.loc[member, 'Code'] = data['cluster']['mibig_accession']
                    df.loc[member, 'Organism'] = data['cluster']['organism_name']
                    df.loc[member, 'Compounds'] = ', '.join(
                        [c.get('compound') for c in data['cluster']['compounds']]
                        )
                    df.loc[member, 'Biosynthetic Class'] = ', '.join(
                        data['cluster']['biosyn_class']
                        )
                    df.loc[member, 'Completeness'] = data['cluster']['loci']['completeness']
                    df.loc[member, 'Minimal'] = data['cluster']['minimal']
        if df.empty:
            console.print('[bold yellow]Your search had no '
                          'match[/bold yellow]')
            sys.exit()
        df.to_csv(
            f'{args.create_prefix}_codes.tsv', sep='\t', index=False
            )
        return df['Code'].to_list()
    except PermissionError:
        console.print(
            '[bold red]Permission to read directory or write '
            'file denied.[/bold red]'
            )
        sys.exit()
    except FileNotFoundError:
        console.print(f'[bold red]{tar.name} not found.[/bold red]')
        sys.exit()
