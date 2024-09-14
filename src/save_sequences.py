"""
Save the matched sequences in FASTa format.
"""

import sys
from Bio import SeqIO
from src.console import console

def save_sequences(target: str, access_codes: str) -> None:
    '''
    Save the desired sequences in a FASTa file.
    '''
    console.print('[bold green]Saving desired sequences...[/bold green]')
    desired_seqs: list = []

    try:
        with open('mibig_prot_seqs_3.1.fasta', 'rt', encoding='utf-8') as fasta:
            for record in SeqIO.parse(fasta, 'fasta'):
                if any(code in record.id for code in access_codes):
                    desired_seqs.append(record)

        SeqIO.write(desired_seqs, f'{target}_complete.fasta', 'fasta')
    except PermissionError:
        console.print(
            '[bold red]Permission to read directory or write file denied.[/bold red]'
            )
        sys.exit()
