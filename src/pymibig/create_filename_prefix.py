"""
Create a prefix for resulting filenames.
"""

def create_filename_prefix(args) -> str:
    '''
    Take user arguments and compose filenames prefix with them.
    '''

    org = f'{args.organism}_' if args.organism else ""
    prod = f'{args.product}_' if args.product else ""
    bio = f'{args.biosynt}_' if args.biosynt else ""
    comp = f'{args.completeness}'
    mini = f'{"_minimal" if args.minimal else ""}'

    prefix = org + prod + bio + comp + mini

    return prefix
