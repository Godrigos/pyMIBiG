"""
Get arguments from user.
"""

import argparse


def get_args() -> argparse.Namespace:
    '''
    Recieve user arguments and return them to main function.
    '''
    parser = argparse.ArgumentParser(
        prog='pyMIBiG',
        description='A small tool to download, match and save target sequences from MIBiG.'
    )
    parser.add_argument('organism', help='Organism to query in database',
        type=str)
    parser.add_argument('-c', '--completeness', help='Loci completeness.',
        type=str, choices=['complete', 'incomplete', 'Unknown'],
        default='complete')
    parser.add_argument('-m', '--minimal', action="store_true",
                        help='Minimal annotation.')
    return parser.parse_args()
