"""
Find complete cluster of target species
"""

import sys
from src.download_json import download_json
from src.download_fasta import download_fasta
from src.uncompress_json import uncompress_json
from src.get_json_filenames import get_json_filenames
from src.save_complete_access_codes import save_complete_access_codes
from src.save_sequences import save_sequences
from src.console import console

def main(target:str = "Streptomyces") -> None:
    '''
    Execute MIBiG search
    '''

    download_json()
    download_fasta()

    uncompress_json()
    json_files = get_json_filenames()

    access_codes = save_complete_access_codes(target, json_files)
    save_sequences(target, access_codes)

    console.print(
        '[bold blue]Task completed! Check your result files.[/bold blue]'
        )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nExecution interrupted by the user.')
