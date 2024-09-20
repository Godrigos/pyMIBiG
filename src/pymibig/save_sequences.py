"""
Save the matched sequences in GBK format.
"""

import sys
import tarfile
import io
from itertools import islice
from Bio import SeqIO
from src.pymibig.console import console
from src.pymibig.constants import DATABASE

def save_sequences(target: str, access_codes: str, basedir: str,
                   completeness: str, minimal: bool) -> None:
    '''
    Save the desired sequences in a FASTa file.
    '''
    #console.print('[bold green]Saving desired sequences...[/bold green]')
    desired_seqs: list = []

    try:
        with console.status(
            '[bold green]Saving desired sequences...[/bold green]'
            ):
            with tarfile.open(f'{basedir}/src/db/{DATABASE}') as tar:
                for member in islice(tar, 1, None):
                    with tar.extractfile(member) as handle:
                        seq = SeqIO.read(
                            io.TextIOWrapper(handle),
                            'genbank')
                        if any(code in seq.id for code in access_codes):
                            desired_seqs.append(seq)

        SeqIO.write(
            desired_seqs,
            f'{target}_{completeness}{"_minimal" if minimal else ""}.fasta',
            'fasta')
    except PermissionError:
        console.print(
            '[bold red]Permission to read directory or write file denied.[/bold red]'
            )
        sys.exit()
