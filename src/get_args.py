"""
Get arguments from user.
"""

import argparse


def get_args() -> argparse.Namespace:
    '''
    Recieve user arguments and return them to main function.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Search term to query in database',
        type=str)
    return parser.parse_args()
