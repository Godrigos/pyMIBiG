"""
Create a prefix for resulting filenames.
"""

def create_filename_prefix(args) -> str:
    '''
    Take user arguments and compose filenames prefix with them.
    '''
    return (
        f'{args.organism if args.organism else ""}_'
        f'{args.product if args.product else ""}_'
        f'{args.biosynt if args.biosynt else ""}_'
        f'{args.completeness}_'
        f'{"minimal" if args.minimal else ""}'
    )
