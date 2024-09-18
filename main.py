"""
Find complete cluster of target species
"""

import sys
import os
from src.download_json import download_json
from src.download_seqs import download_seqs
from src.save_access_codes import save_access_codes
from src.save_sequences import save_sequences
from src.console import console
from src.get_args import get_args

basedir: str = os.path.dirname(__file__)

def main() -> None:
    '''
    Execute MIBiG search
    '''
    args = get_args()

    download_json(basedir)
    download_seqs(basedir)

    access_codes = save_access_codes(args.target, basedir, args.completeness,
                                     args.minimal)
    save_sequences(args.target, access_codes, basedir, args.completeness,
                   args.minimal)

    console.print(
        '[bold blue]Task completed! Check your result files.[/bold blue]'
        )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nExecution interrupted by the user.')
